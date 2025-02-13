﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from typing import ForwardRef



import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me

sys.setrecursionlimit(5000)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def printAuthorData(author):
    if author:
        print("Autor encontrado: " + author["name"])
        print("Total Obras de arte: " + str(lt.size(author["artworks"])))
        for artwork in lt.iterator(author["artworks"]):
            print("Titulo: " + artwork["title"])
        print("\n")
    else:   
        print("No se encontro el autors")

def printAuthorbyYear(authors):

    if(authors):
        tamano = 0
        primeros = 0
        ultimos = 0
        authors_1 = lt.getElement(authors, 0)
        authors_2 = lt.getElement(authors, lt.size(authors))
        for i in range(0, lt.size(authors)):
            tamano += (lt.size(lt.firstElement(authors)))
            while primeros < 3:
                print(lt.firstElement(authors_1))
                lt.removeFirst(authors_1)
                primeros += 1
            while ultimos < 3:
                print(lt.lastElement(authors_2))
                lt.removeLast(authors_2)
                ultimos += 1
        print("Se encontraron " + str(tamano) + " autores")
    else:
        print("No se encontraron autores.\n")

def printArtworksbyYear(artworks):

    if(artworks):
        tamano = 0
        primeros = 0
        ultimos = 0
        artworks_1 = artworks
        artworks_2 = artworks
        for i in range(0, lt.size(artworks)):
            tamano += (lt.size(lt.firstElement(artworks_1)))
            while primeros < 3:
                print(lt.firstElement(artworks_1))
                lt.removeFirst(artworks_1)
                primeros += 1
            while ultimos < 3:
                print(lt.lastElement(artworks_2))
                lt.removeLast(artworks_2)
                ultimos += 1
        print("Se encontraron " + str(tamano) + " autores")
    else:
        print("No se encontraron autores.\n")


def printArtworkstech(catalog, ord_obras):
    tamano = 0
    list_max = lt.newList()
    techniques = catalog["techniques"]
    max = 0
    valores = mp.valueSet(techniques)
    x = lt.size(valores)
    for i in range(1,x+1):
        valor = lt.size(lt.getElement(valores, i))
        tamano += valor
        if valor > max:
            max = valor
    x = lt.size(ord_obras)
    for i in range(1, x+1):
        entry = lt.getElement(ord_obras, i)
        llave = me.getKey(entry)
        valor = me.getValue(entry)
        y = lt.size(valor)
        for j in range(1, y+1):
            if llave == max:
                entry = lt.getElement(valor, j)
                lt.addLast(list_max, entry)
    print("\n")
    if not lt.isEmpty(list_max):
        print("Total de obras encontradas: " + str(tamano) + "\n")
        print("Técnica más utilizada: " + (lt.firstElement(list_max))["Medium"] + " con " + str(lt.size(list_max)) + " obras")
        primeros = 0
        print("-"*100)
        while primeros < max:
            print("-"*100)
            print(lt.firstElement(list_max))
            
            lt.removeFirst(list_max)
            primeros += 1
        print("-"*100)
        print("-"*100)
    else:
        print("El autor no ha sido encontrado\n")
    
def printMostNationalities(catalog, listNations):
    nationalities = listNations
    llaves = mp.keySet(nationalities)
    values_size = lt.size(llaves)
    top = 0
    topnations = lt.newList()
    max = 0
    max = 0
    for i in range(1, values_size+1):
        exists = mp.contains(nationalities, lt.getElement(llaves, i))
        if exists:
            pareja = mp.get(nationalities, lt.getElement(llaves, i))
            llave = me.getKey(pareja)
            actual = me.getValue(pareja)
            entry = {"Nationality": llave, "Amount": actual}
            lt.addLast(topnations, entry)
    print("\n")
    print("Top 10 nacionalidades\n")
    print("-"*50)
    print("-"*50)
    print(lt.firstElement(sortNation(topnations)))
    print("-"*50)
    top = 0
    while top < 10:
        lt.removeFirst(topnations)
        print(lt.firstElement(sortNation(topnations)))
        print("-"*50)
        top += 1
    print("-"*50)
    NationArtworks(catalog, "American")
    

def NationArtworks(catalog, nation):
    authors = catalog["authors"]
    artworks = lt.newList()
    keys = mp.keySet(authors)
    mpsize = mp.size(keys)
    for i in range(1, mpsize+1):
        par = mp.get(authors, lt.getElement(keys, i))
        valor = me.getValue(par)
        nationality = valor["Nationality"]
        if nationality != "":
            if nationality == nation:
                natartworks = {"Amount": lt.size(valor["artworks"]), "Artworks": valor["artworks"]}
                lt.addLast(artworks, natartworks)
    most = lt.removeFirst(sortNation(artworks))
    obras = most["Artworks"]

    print("Obras encontradas de nacionalidad: " + str(nation)+ "\n")
    for j in range(1, 4):
                    
        
        
        authorid = lt.getElement(obras,j)["ConstituentID"].strip("[").strip("]")
        for k in range(1, mpsize):
            pareja = mp.get(authors, lt.getElement(keys, k))
            valor = me.getValue(pareja)

            if authorid == valor["id"]:
                name = valor["DisplayName"]
                
                
        print("-"*50)
        print(lt.getElement(obras, j))
        print("\n")
        print("Por " + str(name))
        print("-"*50) 
                    


def sortNation(list):
    max = 0
    list_size = lt.size(list)
    for i in range(1, list_size + 1):
        artwork = lt.getElement(list, i)
        if artwork["Amount"] > max:
            max = artwork["Amount"]
    

    for i in range(1, list_size + 1):
        artwork = lt.getElement(list, i)
        if artwork["Amount"] == max:
        
            lt.exchange(list,1, i)
    return list      
  
   

    



def printmoveArtworks(catalog, artworks):
    list = lt.newList("SINGLE_LINKED")
    llaves = mp.keySet(artworks)
    llaves_size = mp.size(llaves)
    peso = 0.0
    precio = 0
    for i in range(1, llaves_size+1):
        
        par = mp.get(artworks, lt.getElement(llaves, i))
        price = (me.getValue(par))["Price"] 
        value = (me.getValue(par))["info"]
        if value["Weight (kg)"] != "":
            peso += float(value["Weight (kg)"])
        year = (me.getValue(par))["Date"]
        precio += float(price)
        lt.addLast(list, me.getValue(par))
    print("Se encontraron " + str(llaves_size) + " obras" + "\n")
    print("El peso total aproximado es de " + str(peso) + " kg\n")
    print("El precio total aproximado es de " + str(round(precio,2)) + " USD\n")
    print("Obras más costosas de transportar\n")
    list_2 = list
    print(lt.firstElement(sortPrice(list)))
    print("-"*50)
    top = 0
    while top < 5:

        lt.removeFirst(list)
        print(lt.firstElement(sortPrice(list)))
        print("-"*50)
        top += 1
    print("-"*50)
    print("Obras más antiguas a transportar\n")
    print(lt.firstElement(sortYear(list_2)))
    print("-"*50)
    bot = 0 
    while bot < 5:
        lt.removeFirst(list_2)
        print(lt.firstElement(sortYear(list_2)))
        print("-"*50)
        bot += 1
    print("-"*50)
    


def sortPrice(list):
    max = 0
    list_size = lt.size(list)
    for i in range(1, list_size + 1):
        artwork = lt.getElement(list, i)
        if artwork["Price"] > max:
            max = artwork["Price"]
    for i in range(1, list_size + 1):
        artwork = lt.getElement(list, i)
        if artwork["Price"] == max:
        
            lt.exchange(list,1, i)
    return list

def sortYear(list):
    min = 2020
    list_size = lt.size(list)
    for i in range(1, list_size + 1):
        artwork = lt.getElement(list, i)
        if artwork["Date"] != "":
            if int(artwork["Date"]) < min:
             min = int(artwork["Date"])
    for i in range(1, list_size + 1):
        artwork = lt.getElement(list, i)
        if artwork["Date"] != "":
            if int(artwork["Date"]) == min:
                lt.exchange(list,1, i)
    return list

    
    

    
                
        
    

    




def printMenu():
    print("Bienvenido")
    print("0- Inicializar catálogo")
    print("1- Cargar información en el catálogo")
    print("2- Buscar autores en un rango de fechas")
    print("3- Buscar obras adquiridas en un rango de fechas")
    print("4- Buscar tecnicas de un autor")
    print("5- Buscar Top nacionalidades")
    print("6- Transportar obras de un departamento")
    print("7- Salir")
def initCatalog():
    return controller.initCatalog

def loadData(catalog):
    return controller.loadData(catalog)




"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("Inicializando catálogo ....")
        cont = controller.initCatalog()

    elif int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        controller.loadData(cont)
        print('Obras cargadas: ' + str(controller.artworksSize(cont)))
        print('Autores cargados: ' + str(controller.authorsSize(cont)))
       

    elif int(inputs[0]) == 2:
        syear = input("Que fecha de inicio: ")
        eyear = input("Que fecha de finalización: ")
        authors = controller.getAuthorsByYear(cont, int(syear), int(eyear))
        printAuthorbyYear(authors)
    
    elif int(inputs[0]) == 3:
        syear = input("Que fecha de inicio1: ")
        eyear = input("Que fecha de finalización1: ")
        artworks = controller.getArtworkByYear(cont, (syear), (eyear))
    

    elif int(inputs[0]) == 4:
        authorname = input("Nombre de autor a buscar: ")
        artworks = controller.ArtworkstechByAuthor(cont, authorname)
        printArtworkstech(cont, artworks)

    elif int(inputs[0]) == 5:
        artworks = controller.addNationalityReps(cont)
        printMostNationalities(cont, artworks)

    elif int(inputs[0]) == 6:
        departamento = input("De qué departamento desea transportar obras?: \n")
        artworks = controller.moveArtworks(cont, departamento)
        printmoveArtworks(cont,artworks)
    elif int(inputs[0]) == 7:
        sys.exit(0)
sys.exit(0)
