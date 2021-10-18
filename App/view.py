"""
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
        authors_1 = authors
        authors_2 = authors
        for i in range(0, lt.size(authors)):
            tamano += (lt.size(lt.firstElement(authors_1)))
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

def printMenu():
    print("Bienvenido")
    print("0- Inicializar catálogo")
    print("1- Cargar información en el catálogo")
    print("2- Buscar obras en un rango de fechas")

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
        print(cont["authors"])

    
    elif int(inputs[0]) == 2:
        syear = input("Que fecha de inicio: ")
        eyear = input("Que fecha de finalización: ")
        authors = controller.getAuthorsByYear(cont, int(syear), int(eyear))
        printAuthorbyYear(authors)
    else:
        sys.exit(0)
sys.exit(0)
