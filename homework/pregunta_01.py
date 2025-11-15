# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
from zipfile import ZipFile
import os # Interactuar con el sistema operativo 
import glob # Buscar archivos en directorios
from pathlib import Path # Manipulacion de rutas de archivos
import pandas as pd # Manipulacion de datos
import csv # Leer y escribir archivos CSV


def extract_file(zip_file,file_path):
    with ZipFile(zip_file,"r") as zipFile:
        zipFile.extractall(file_path)

def read_text_file(file_path):
    lista=[]
    c=0
    for file in glob.glob(f"{file_path}/**/*.txt"):
        key = Path(file).parent.name
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                lista.append([c,line,key])
                c+=1
    return lista


def create_output_directory(output_path):

    #Delete output directory if exists
    if os.path.exists(output_path):
        for file in glob.glob(f"{output_path}/*"):
            os.remove(file)
        os.rmdir(output_path)

    #Create output directory 
    os.makedirs(output_path)
    return output_path


    

def generate_csv_format(file_path,rows):

    fields=["","phrase","target"]

    max_phrase_length = max(len(row[1]) for row in rows)
    
    with open(file_path, "w", newline="",encoding="utf-8") as file:
        writer_csv = csv.writer(file)
        writer_csv.writerow([f"|{fields[0]:>3} | {fields[1]:<{max_phrase_length}} | {fields[2]:<8} |"])
        writer_csv.writerow([f"|{'---:':>3}|:{'-'*(max_phrase_length+1)}|:{'-'*9}|"])
        
        for row in rows:
            id, phrase, target = row
            phrase = phrase.strip().replace("\n", " ")
            file.write(f"| {id:<2} | {phrase:<{max_phrase_length}} | {target:<8} |\n")




def generate_csv(file_path, rows):
    
    p = Path(file_path)
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["phrase", "target"])
        for r in rows:
            _, phrase, target = r
            writer.writerow([phrase, target])



def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    #
    extract_file("files/input.zip","files")
    # Lista con lineas de train y test
    train = read_text_file("files/input/train")
    test = read_text_file("files/input/test")

    out_dir = create_output_directory("files/output")
    
    file_train = os.path.join(out_dir, "train_dataset.csv")
    file_test = os.path.join(out_dir, "test_dataset.csv")
    
    generate_csv(file_train, train)
    generate_csv(file_test, test)





pregunta_01()
       


