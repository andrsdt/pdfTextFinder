import PyPDF2
import re
import os

filesDir = './data/'

if filesDir[-1] != '/':
    filesDir += '/'

listaFicheros = [filesDir+f for f in os.listdir(filesDir) if f.endswith(".pdf")]

stringFilter = input("Introduzca la palabra a buscar: ")

def encontrarPalabras(listaFicheros,stringFilter):
    encontrado = False
    for fichero in listaFicheros:
        myObject = PyPDF2.PdfFileReader(fichero)
        numPages = myObject.getNumPages()
        for i in range(0, numPages):
            PageObj = myObject.getPage(i)
            Text = PageObj.extractText().replace("\n","")
            ReSearch = re.search(stringFilter, Text)
            if ReSearch != None:
                print("\'{}' aparece en la pagina {} del fichero {}.".format(
                    stringFilter, i+1, fichero.split("/")[-1]))
                encontrado = True

    if encontrado == False:
        print("No se han encontrado coincidencias")


if __name__ == "__main__":
    encontrarPalabras(listaFicheros,stringFilter)