"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    catalog = model.newCatalog()
    return catalog
# Funciones para la carga de datos
def loadData(catalog):
    loadAuthors(catalog)
    loadArtworks(catalog)
 


def loadArtworks(catalog):
    artworksfile = cf.data_dir + "Artworks-utf8-small.csv"
    input_file = csv.DictReader(open(artworksfile, encoding = "utf-8"))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

def loadAuthors(catalog):
    authorsfile = cf.data_dir + "Artists-utf8-small.csv"
    input_file = csv.DictReader(open(authorsfile, encoding = "utf-8"))
    for authorinfo in input_file:
        model.newinfo(catalog, authorinfo)
# Funciones de ordenamiento
def artworksSize(catalog):
    """
    Numero de libros cargados al catalogo
    """
    return model.artworksSize(catalog)


def authorsSize(catalog):
    """
    Numero de autores cargados al catalogo
    """
    return model.authorsSize(catalog)
def yearsSize(catalog):
    return model.yearsSize(catalog)
# Funciones de consulta sobre el catálogo
def search(catalog, id):
    return model.search(catalog, id)

def getAuthorsByYear(catalog, syear, eyear):
    """
    Retorna los libros que fueron publicados
    en un año
    """
    authors = model.getAuthorsByYear(catalog, syear, eyear)
    return authors

def getArtworkByYear(catalog, syear, eyear):
    artworks = model.getArtworkByYear(catalog, syear, eyear)
    return artworks

def ArtworkstechByAuthor(catalog, authorname):
    artworkstech = model.addTechniqueReps(catalog, authorname)
    return artworkstech

def addNationalityReps(catalog):
    nationalities = model.addNationalityReps(catalog)
    return nationalities
