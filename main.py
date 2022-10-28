#importación de modulos, con comandos particulares para Mac

from pip._vendor import requests
import csv
import json
import time
import string
import os.path

# Creación de carpeta "General"
if not os.path.isdir("General/"):
    os.mkdir("General/")
## Quitar signos de punctuación
dictPunct = str.maketrans("","", string.punctuation)
del dictPunct[ord("'")]
# Funcción de contar palabras para crear diccionario
counts = dict()
def word_count(str, counts):
    words = str.split()
    for word in words:
        word = word.translate(dictPunct).lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

#Bucle para realizar los GET al API cada 30 segundos, obteniendo quotes e imagenes
while True:
    response_API = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    data_JSON = response_API.json()
    datos = {"Autor": data_JSON[0]["character"], "Frase": data_JSON[0]["quote"]}

    image = requests.get(data_JSON[0]["image"]).content
    fileName = datos["Autor"].translate(dictPunct).replace(" ", "_") + ".png"
    directory = datos["Autor"].translate(dictPunct).replace(" ", "_")+"/"
    filePath = os.path.join(directory, fileName)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open (filePath, "wb") as f:
        f.write(image)

    pathGeneral = "General/general.csv"
    with open(pathGeneral, 'a', newline='') as f:
        w = csv.DictWriter(f, datos.keys())
        w.writerow(datos)

    fileName2 = datos["Autor"] + ".csv"
    filePath2 = os.path.join(directory, fileName2)
    with open(filePath2, 'a', newline='') as f:
        w = csv.DictWriter(f, datos.keys())
        w.writerow(datos)
# crear y añadir conteos al diccionario
    word_count(datos["Frase"], counts)
    with open("cuentas.csv", "w", newline='') as csvfile:
        headerKey = ["Palabra", "Cuenta"]
        newVal = csv.DictWriter(csvfile, headerKey)
        newVal.writeheader()
        for newK in counts:
            newVal.writerow({"Palabra": newK, "Cuenta": counts[newK]})

    time.sleep(1)