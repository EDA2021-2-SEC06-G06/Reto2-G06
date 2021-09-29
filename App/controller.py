"""
Reto 2 - controller.py

Carlos Arturo Holguín Cárdenas
Daniel Hernández Pineda

 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de obras

def initCatalog():
    """
    Llama la funcion de inicializació del catálogo del modelo
    """
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos

def loadData(catalog, file_size):
    """
    Carga los datos de los archivos y los ordena
    """
    #loadArtists(catalog, file_size)
    loadArtworks(catalog, file_size)

    #sortArtists(catalog, model.cmpArtistByBeginDate)
    #sortArtworks(catalog, model.cmpArtworkByDateAcquired)


"""
def loadArtists(catalog, file_size):
    
    artistsfile = cf.data_dir + 'Artists-utf8-' + file_size + '.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)
"""

def loadArtworks(catalog, file_size):
    """
    Carga las obras del archivo
    """
    #sortArtists(catalog, model.cmpArtistByAuthorID)
    artworksfile = cf.data_dir + 'Artworks-utf8-' + file_size + '.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.AddMediumLab5(catalog, artwork)


# Funciones de ordenamiento

#def sortArtists(catalog, cmpfunction=model.cmpArtistByBeginDate):
    """
    Ordena los artistas según la función de comparación dada
    """
    #model.sortArtists(catalog, cmpfunction)


#def sortArtworks(catalog, cmpfunction):
    """
    Ordena las obras según la función de comparación dada
    """
    #model.sortArtworks(catalog, cmpfunction)

#Funciones de Lab 5
def REQLab5(catalog,Medium):
    return model.REQLab5(catalog,Medium)
# Funciones de consulta sobre el catálogo


"""
FUNCIONES DEL RETO 1

def REQ1getArtistsRange(catalog, date_initial, date_final):
    return model.getArtistsRangeReq1(catalog, date_initial, date_final)


def REQ2getArtworksRange(catalog, date_initial, date_final):
    return model.getArtworksInfoReq2(catalog, date_initial, date_final)


def REQ3get_techniquees(catalog,Name):
    return model.getTechniquesReq3(catalog,Name)


def REQ4getNationalityCount(catalog):
    final_list = model.getNationalityCountReq4(catalog)
    model.sortReq4(final_list)
    return final_list


def REQ5moveArtworks(catalog, department):
    return model.moveArtworksReq5(catalog, department)
"""