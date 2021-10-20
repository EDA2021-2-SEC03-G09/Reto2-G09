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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import compareElements
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from datetime import datetime
from datetime import timedelta
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'artworks': None,
               'authors': None}

    catalog["artworks"] = lt.newList("SINGLE_LINKED")

    catalog['authors'] = mp.newMap(800,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareAuthorsByName)
    catalog["authors_info"] = mp.newMap(800,
                                        maptype="CHAINING",
                                        loadfactor=4.0)
    
    catalog["years"] = mp.newMap(10000,
                                 maptype="PROBING",
                                 loadfactor=0.5,
                                 comparefunction=compareMapyear)

    catalog["techniques"] = mp.newMap(500,
                                      maptype="CHAINING",
                                      loadfactor= 0.5,
                                      comparefunction=compareReps)


    return catalog

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

def addAuthor(id):
    author = {"id": "", 
              "artworks": None}
    author["id"] = id
    author["artworks"] = lt.newList("SINGLE_LINKED", compareAuthorsByName)
    
    return author

def newinfo(catalog, authorinfo):
    mp.put(catalog["authors_info"], authorinfo["ConstituentID"], authorinfo)
    addAuthoryear(catalog, authorinfo)

def addArtwork(catalog, artwork):
    lt.addLast(catalog["artworks"], artwork)
    addArtworkyear(catalog, artwork)
    authors = artwork["ConstituentID"].split(",")
    for value in authors:
        author = value.strip("[").strip("]").strip(" ")
        addArtworkAuthor(catalog, author.strip(), artwork)

def addArtworkAuthor(catalog, authorid, artwork):
    authors = catalog["authors"]
    existauthor = mp.contains(authors, authorid)
    if existauthor:
        entry = mp.get(authors, authorid)
        author = me.getValue(entry)
    else:
        author = addAuthor(authorid)
        mp.put(authors, authorid, author)
        authorinfo = addAuthorinfo(catalog, authorid)
    lt.addLast(author["artworks"], artwork)

def addAuthorinfo(catalog, authorid):
    authors = catalog["authors"]
    authors_info = catalog["authors_info"]
    entry = mp.get(authors, authorid)
    valor = me.getValue(entry)
    entrada = mp.get(authors_info, authorid)
    valor2 = me.getValue(entrada)
    valor.update(valor2)
    del valor["ConstituentID"]
    mp.put(authors, valor["DisplayName"], valor)
 

def addAuthoryear(catalog, author):
    
    try:
        years = catalog['years']
        if (author['BeginDate'] != ''):
            bornyear = author['BeginDate']
            bornyear = int(float(bornyear))
        else:
            pubyear = 2020
        existyear= mp.contains(years, bornyear)
        if existyear:
            entry = mp.get(years, bornyear)
            year = me.getValue(entry)
        else:
            year = newYear(bornyear)
            mp.put(years, bornyear, year)
        lt.addLast(year["authors"], author)
    except Exception:
        return None

def addNationalityReps(catalog):

    authors = catalog["authors"]
    authors_info = catalog["authors_info"]
    llaves = mp.keySet(authors)
    len_llaves = lt.size(llaves)
    nacionalidades = mp.newMap(20000, loadfactor=0.5, maptype="PROBING")
    for i in range(1, len_llaves+1):
        author_name = lt.getElement(llaves, i)
        pos = mp.get(authors, author_name)
        llave = me.getKey(pos)
        author = mp.get(authors_info, llave)
        if author:
            valor = me.getValue(author)
            exist = mp.contains(nacionalidades, valor["Nationality"])
            if exist:
                pareja = mp.get(nacionalidades, valor["Nationality"])
                llave = me.getKey(pareja)
                nuev_valor = int(me.getValue(pareja)) + 1
                nuev_pareja = me.setValue(pareja, nuev_valor)
                mp.remove(nacionalidades, llave)
                mp.put(nacionalidades, llave, nuev_valor)
            else:
                mp.put(nacionalidades,valor["Nationality"], 1)

    return nacionalidades

def addTechniqueReps(catalog, authorname):
    try:
        
        techniques = catalog["techniques"]
        authors = catalog["authors"]
        exists = mp.contains(authors, authorname)
        if exists:
            
            entry = mp.get(authors, authorname)
            info_author = me.getValue(entry)
            for i in range(0, lt.size(info_author["artworks"])):
                artwork = lt.getElement(info_author["artworks"], i)
                artexist = mp.contains(techniques, artwork["Medium"])
                
                if artexist:
                    entrada = mp.get(techniques, artwork["Medium"])
                    llave = me.getKey(entrada)
                    valor = me.getValue(entrada)
                    valor["repetitions"] += 1
                    lt.addLast(valor["artworks"], artwork)
                    mp.remove(techniques, llave)
                    mp.put(techniques, llave, valor)
                else: 
                    valor = newTechnique(artwork)
                    mp.put(techniques, artwork["Medium"], valor)

        ord_reps = lt.newList("SINGLE_LINKED", compareReps)
        llaves = mp.keySet(techniques)
        for i in range(1, lt.size(llaves)+1):

            entry = mp.get(techniques, lt.getElement(llaves, i))
            valor = me.getValue(entry)
            nuv_par = me.setKey(entry, valor["repetitions"])
            nuv_par = me.setValue(nuv_par, valor["artworks"])
            lt.addLast(ord_reps, nuv_par)
        return ord_reps
    except Exception:
        return None

def newTechnique(artwork):
    entry = {"technique": "", "artworks": None, "repetitions": 0}
    entry["technique"] = artwork["Medium"]
    entry["artworks"] = lt.newList("SINGLE_LINKED")
    entry["repetitions"] = 1
    lt.addFirst(entry["artworks"], artwork)
    return entry

def addArtworkyear(catalog, artwork):
    
    try:
        years = catalog['years']
        if (artwork['DateAcquired'] != ''):
            pubyear = artwork['DateAcquired']
            pubyear = datetime.strptime(pubyear, "%Y-%m-%d")
        else:
            pubyear = 2020
        existyear= mp.contains(years, pubyear)
        if existyear:
            entry = mp.get(years, pubyear)
            year = me.getValue(entry)
        else:
            year = newYear(pubyear)
            mp.put(years, pubyear, year)
        lt.addLast(year["artworks"], artwork)

    except Exception:
        return None

def newYear(bornyear):
    entry = {"year": "", "authors": None, "artworks": None}
    entry["year"] = bornyear
    entry["authors"] = lt.newList("SINGLE_LINKED", compareYears)
    entry["artworks"] = lt.newList("SINGLE_LINKED", compareYears)
    return entry

    
   
# Funciones de consulta


def artworksSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['artworks'])


def authorsSize(catalog):
    """
    Numero de autores en el catalogo
    """
    return mp.size(catalog['authors_info'])

def search(catalog, id):
    return mp.get(catalog["authors"], id)

def yearsSize(catalog):
    return mp.size(catalog["years"])

def getAuthorsByYear(catalog, start, end):
    authors = lt.newList()
    rango = end - (start-1)
    for i in range(0, rango):
        year = mp.get(catalog['years'], start+i)
        if year:
            elementos = me.getValue(year)['authors']
            lt.addLast(authors, elementos)
    return authors

def getArtworkByYear(catalog, start, end):
    cont = 0
    artworks = lt.newList()
    start = datetime.strptime((start).strip(" "), "%Y-%m-%d")
    end = datetime.strptime(end.strip(" "), "%Y-%m-%d")  
    date_generated = [start + timedelta(days=x) for x in range(0, (end-start).days)]
    for i in range(0, len(date_generated)): 
        year = mp.get(catalog["years"], date_generated[i])
        if year:
            elementos = me.getValue(year)["artworks"]
            lt.addLast(artworks, elementos)
    return artworks

def getArtworkByNationality(catalog):
    autores = catalog["authors"]
    
# Funciones utilizadas para comparar elementos dentro de una lista

def compareAuthorsByName(keyname, author):
    authentry = me.getKey(author)

    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def compareReps(reps, list):
    tagentry = me.getKey(list)
    if (reps == tagentry):
        return 0
    elif (reps > tagentry):
        return 1
    else: 
        return -1
    

def compareMapyear(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else: 
        return -1

def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return 0


# Funciones de ordenamiento
