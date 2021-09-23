"""
Reto 2 - model.py

Carlos Arturo Holguín Cárdenas
Daniel Hernández Pineda

 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import queue
from DISClib.ADT import stack
from DISClib.Algorithms.Sorting import shellsort as sso
from DISClib.Algorithms.Sorting import mergesort as mso
assert cf


# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de obras y artistas
    """
    catalog = {"artists": None,
               "artworks": None}

    catalog["artists"] = lt.newList("ARRAY_LIST")
    catalog["artworks"] = lt.newList("ARRAY_LIST")

    return catalog


# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    """
    Se adiciona el artista a la lista de artistas
    """
    Arti_r=artists_required(artist["ConstituentID"],
                            artist["DisplayName"],
                            artist["BeginDate"],
                            artist["EndDate"],
                            artist["Nationality"],
                            artist["Gender"])
    lt.addLast(catalog['artists'], Arti_r)
    

def addArtwork(catalog, artwork):
    """
    Se adiciona la obra a la lista de obras
    """
    Artw_r=artworks_required(artwork["ObjectID"],
                            artwork["Title"],
                            artwork["ConstituentID"],
                            artwork["Date"],
                            artwork["Medium"],
                            artwork["Dimensions"],
                            artwork["Classification"],
                            artwork["Department"],
                            artwork["DateAcquired"],
                            artwork['CreditLine'],
                            artwork["URL"],
                            artwork["Depth (cm)"],
                            artwork["Diameter (cm)"],
                            artwork["Height (cm)"],
                            artwork["Length (cm)"],
                            artwork["Weight (kg)"],
                            artwork["Width (cm)"])

    addArtistsNames(catalog, Artw_r)

    lt.addLast(catalog['artworks'], Artw_r)


# Funciones para creacion de datos

def splitAuthorsIDs(authorsIDs):
    """
    Separa los IDs de los autores de una obra en una lista
    """
    authors=authorsIDs.replace(",","")
    authors = authors.replace("[","")
    authors=authors.replace("]","")

    authorsIDs_list = lt.newList()
    centinela = True

    while centinela:
        if " " in authors:
            pos = authors.find(" ")
            lt.addLast(authorsIDs_list, authors[0:pos])
            authors = authors[pos + 1:]

        if " " not in authors:
            lt.addLast(authorsIDs_list, authors)
            centinela = False

    return authorsIDs_list


def addArtistsNames(catalog, artwork):
    """
    Añade en la información de cada obra los nombres de sus autores
    """
    artists = catalog["artists"]
    authors_IDs = artwork["ArtistID"]
    authors_IDs = splitAuthorsIDs(authors_IDs)
    authors = ""

    #Revisar cada elemento de la cola de IDs de autores         
    while lt.size(authors_IDs)>0: #No realiza más de X ciclos
        authorID = lt.firstElement(authors_IDs)    
        j = binary_search(artists, authorID, AuthorIDLowerThanGivenID, AuthorIDGreaterThanGivenID)
        artist = lt.getElement(artists, j)
        author=artist["Name"]

        if authors == "":                
            authors = author
        else:
            authors += ", " + author

        lt.removeFirst(authors_IDs)

    artwork["ArtistName"] = authors


def artists_required(artistID,name,begindate,end,nationality,gender):
    """
    Define la información útil para cargar en el catálogo de artistas
    """
    artist={"ArtistID":artistID,
            'Name':name,
            'BeginDate':begindate,
            'EndDate':end,
            'Nationality':nationality,
            'Gender':gender}
    return artist


def artworks_required(artworkID,title,artistID,date,medium,dimensions,
                    classification,department,dateacquired,creditline, url,
                    depth, diameter, height, length, weight, width):
    """
    Define la información útil para cargar en el catálogo de obras
    """
    artwork={"ArtworkID":artworkID,
            "Title": title,
            "ArtistID":artistID,
            "ArtistName": "",
            "Date":date,
            "Medium": medium,
            "Dimensions": dimensions,
            "Classification": classification,
            "Department": department,
            "DateAcquired": dateacquired,
            "CreditLine": creditline,
            "URL": url,
            "Depth": depth,
            "Diameter": diameter,
            "Height": height,
            "Length": length,
            "Weight": weight,
            "Width": width}

    return artwork


# Funciones de consulta

def binary_search(lst, value, lowercmpfunction, greatercmpfunction):
    """
    Se basó en este código en el que se encuentra en la siguiente página web:
    https://www.geeksforgeeks.org/python-program-for-binary-search/
    """

    size = lt.size(lst)
    low = 0
    high = size - 1
 
    while low <= high:
        mid = (high + low) // 2
        indexed_element = lt.getElement(lst, mid)
        
        if lowercmpfunction(indexed_element, value):
            low = mid + 1
 
        elif greatercmpfunction(indexed_element, value):
            high = mid - 1

        else:
            return mid
 
    return -1



"""
FUNCIONES DEL RETO 1

"Requerimiento 1"
def getInitPosReq1(artists, date_initial):
    pos1 = binary_search(artists, date_initial, BeginDateLowerThanGivenDate, BeginDateGreaterThanGivenDate) 
    index1 = pos1-1
    found_pos1 = False

    while (not found_pos1) and index1>0:
        prev_element = lt.getElement(artists, index1)

        if int(prev_element["BeginDate"]) == date_initial:
            pos1 -= 1
            index1 -= 1
        else:
            found_pos1 = True

    return pos1


def getArtistsRangeReq1(catalog, date_initial, date_final):
    artists = catalog['artists']
    pos = getInitPosReq1(artists, date_initial)
    artists_range = lt.newList()
    size = lt.size(artists)

    artists_count = 0

    while pos<=size:
        artist = lt.getElement(artists, pos)

        if (int(artist["BeginDate"])>=date_initial) and (int(artist["BeginDate"])<=date_final):
            lt.addLast(artists_range, artist)
            artists_count += 1
        
        elif int(artist["BeginDate"]) > date_final:
            break

        pos += 1

    return artists_range, artists_count


"Requerimiento 2"
def binary_searchReq2(lst, value, lowercmpfunction, greatercmpfunction):
    """
    #Se basó en este código en el que se encuentra en la siguiente página web:
    #https://www.geeksforgeeks.org/python-program-for-binary-search/
"""

    size = lt.size(lst)
    low = 0
    high = size - 1
 
    while low <= high:
        mid = (high + low) // 2
        indexed_element = lt.getElement(lst, mid)
        
        if lowercmpfunction(indexed_element, value):
            low = mid + 1
 
        elif greatercmpfunction(indexed_element, value):
            high = mid - 1

        else:
            return mid

        if (low==(high-1)) or (low==high): #Se halla el primer elemento del rango así no haya coincidencia exacta
            return low
 
    return -1


def getArtworksInfoReq2(catalog, date_initial, date_final):
    artworks = catalog["artworks"]
    Artworks_final=lt.newList("ARRAY_LIST") #ARRAY_LIST para acceder a cada posición con tiempo constante
    
    pos = binary_searchReq2(artworks, date_initial, DateAcquiredLowerThanGivenDate, DateAcquiredGreaterThanGivenDate) #log(n)
    size = lt.size(artworks)
    artworks_count = 0
    purchase_count = 0
    
    #Se parte de la posición inicial encontrada y se recorre hasta que se encuentra una fecha fuera del rango
    while pos<=size: #Recorre n veces en el peor caso
        artwork = lt.getElement(artworks,pos)

        if (artwork['DateAcquired']>=date_initial) and (artwork['DateAcquired']<=date_final):
            artworks_count += 1

            #Almacenar la información relevante
            data_necessary=lt.newList("ARRAY_LIST") 
            lt.addLast(data_necessary, artwork["ArtworkID"])          #pos 1: ID de la obra
            lt.addLast(data_necessary, artwork["Title"])              #pos 2: Título de la obra
            lt.addLast(data_necessary, artwork["ArtistName"])         #pos 3: Nombres de los autores
            lt.addLast(data_necessary, artwork["Medium"])             #pos 4: Técnica de la obra
            lt.addLast(data_necessary, artwork["Dimensions"])         #pos 5: Dimensiones de la obra
            lt.addLast(data_necessary, artwork["Date"])               #pos 6: Fecha de la obra
            lt.addLast(data_necessary,artwork["DateAcquired"])        #pos 7: Fecha de adquisición de la obra
    
            lt.addLast(Artworks_final,data_necessary)    

            if artwork["CreditLine"]=="Purchase":
                purchase_count+=1

        elif artwork['DateAcquired']>date_final:
            break

        pos+=1

    return Artworks_final,artworks_count,purchase_count


"Requerimiento 3"
def eliminar_repetidos(lista_count):
    "Esta funcion se encarga de eliminar los elementos repetidos despues de  clasificar el mayor"
    largo_no_tec=lt.size(lista_count)
    i=1
    while i<largo_no_tec:
        valor_i=lt.getElement(lista_count,i)
        j=1+i

        while j<=largo_no_tec:
            valor_j=lt.getElement(lista_count,j)
            valor_ai=lt.getElement(valor_i,2)
            valor_ji=lt.getElement(valor_j,2)
            if valor_ai==valor_ji:
                lt.deleteElement(lista_count,j)
                largo_no_tec-=1
                j-=1
                
            j+=1
        i+=1


def getTechniquesReq3(catalog,Name):
    "Funcion pincipal"
    ArtistAndTechniques=lt.newList("ARRAY_LIST") #ARRAY_LIST para acceder a cada posición con tiempo constante
    Artworks_WID=catalog["artworks"]
    large_Artworks_WID=lt.size(Artworks_WID)
    IteracionesI=1
    while IteracionesI<large_Artworks_WID:
        data_necessary=lt.newList("ARRAY_LIST") 
        ArtworkAtMoment=lt.getElement(Artworks_WID,IteracionesI)
        NameArtist=ArtworkAtMoment["ArtistName"]
        if NameArtist==Name:
            lt.addLast(data_necessary, ArtworkAtMoment["Title"])          #pos 1: Titulo de la obra
            lt.addLast(data_necessary, ArtworkAtMoment["Date"])           #pos 2: Fecha de la obra
            lt.addLast(data_necessary, ArtworkAtMoment["Medium"])         #pos 3: Medio de la obra
            lt.addLast(data_necessary, ArtworkAtMoment["Dimensions"])     #pos 4: Dimensiones de la obra
            lt.addLast(ArtistAndTechniques,data_necessary)
        IteracionesI+=1
    NumberOfArtworks=lt.size(ArtistAndTechniques)
    OrderMediums,TechniqueMoreUsed=operaciones_req3(ArtistAndTechniques)
    NumberOfTechniques=lt.size(OrderMediums)
    ListOfArtists=encontrar_obras_con_tec(ArtistAndTechniques,TechniqueMoreUsed)
    return NumberOfArtworks,TechniqueMoreUsed,NumberOfTechniques,ListOfArtists


def operaciones_req3(ArtistAndTechniques):
    datos_tecnicas_art=ArtistAndTechniques
    iteraciones_data_art=1
    lista_count_tec=lt.newList("ARRAY_LIST")
    large_data_art=lt.size(datos_tecnicas_art)
    while iteraciones_data_art<=large_data_art:
        count=1
        lista_count_tec1=lt.newList("ARRAY_LIST")
        tecnica_m=lt.getElement(datos_tecnicas_art,iteraciones_data_art)
        iteraciones_dm=iteraciones_data_art+1
        while iteraciones_dm<=large_data_art:
            
            tecnica_m1=lt.getElement(datos_tecnicas_art,iteraciones_dm)
            tecnica_c=lt.getElement(tecnica_m1,3)
            tecnica_p=lt.getElement(tecnica_m,3)
            if tecnica_p==tecnica_c:
                count+=1
            iteraciones_dm+=1  
           
        lt.addLast(lista_count_tec1, count)        
        lt.addLast(lista_count_tec1, lt.getElement(tecnica_m,3))       ## Date  ## Dimensions
        
        lt.addLast(lista_count_tec,lista_count_tec1) 
        iteraciones_data_art+=1
    lista_sin_repetidos=eliminar_repetidos(lista_count_tec)
    "Ordenar de mayor a menor"
    lista_ordenada=sso.sort(lista_count_tec,compare_cantidad)
    tecnica_usa_ve=lt.getElement(lista_ordenada,1)
    tecnica_mas_usada=lt.getElement(tecnica_usa_ve,2)
  
    return lista_ordenada,tecnica_mas_usada


def encontrar_obras_con_tec(ArtistAndTechniques,tecnica_mas_usada):
    "Encontrar las obras de la tecnica que mas usa el artista"
    "Exportar finalmente los datos"
    i=1
    data_tecnicas=ArtistAndTechniques
    large_data_tecnicas=lt.size(data_tecnicas)
    lista_pf=lt.newList("ARRAY_LIST")
    while i<=large_data_tecnicas:
        lista_s=lt.newList("ARRAY_LIST")
        artwork_at=lt.getElement(data_tecnicas,i)
        artwork_at_moment=lt.getElement(artwork_at,3)
        if tecnica_mas_usada==artwork_at_moment:
            lt.addLast(lista_s, lt.getElement(artwork_at,1))      #pos 1: Título de la obra
            lt.addLast(lista_s, lt.getElement(artwork_at,2))       #pos 3: Fecha de la obra
            lt.addLast(lista_s, lt.getElement(artwork_at,3))      #pos 4: Técnica de la obra
            lt.addLast(lista_s, lt.getElement(artwork_at,4))  #pos 5: Dimensiones de la obra  
            lt.addLast(lista_pf,lista_s)
        i+=1
    return lista_pf


"Requerimiento 4"
def nationalityListReq4(catalog):
    """
    #Crea una lista, cuyos elementos son listas que tienen en la posición 1 una nacionalidad y en sus 
    #demás posiciones los IDs de los artistas que pertenecen a esa nacionalidad. Devuelve esta lista 
    #junto con un directorio. Complejidad O(m)
"""
    artists = catalog["artists"]
    nationalities = lt.newList("ARRAY_LIST") #Lista que guarda los nombres de las nacionalidades (sin IDs)
    nationality_list = lt.newList("ARRAY_LIST") #Lista de listas de nacionalidades-IDs

    pos_artists = 1
    size_artists = lt.size(artists)

    while pos_artists <= size_artists: #size(artists) ciclos
        artist = lt.getElement(artists, pos_artists)
        nationality = artist["Nationality"]
        artistID = artist["ArtistID"]

        if (nationality == "") or (nationality=="Nationality unknown"):
            nationality = "Unknown"

        pos_nationality = lt.isPresent(nationalities, nationality) #Peor caso: #nacionalidades ciclos

        if pos_nationality==0:
            country = lt.newList("ARRAY_LIST") #Lista que guarda la nacionalidad y los IDs de sus artistas

            lt.addLast(country, nationality) #En pos 1 se guarda la nacionalidad
            lt.addLast(country, artistID)    #En pos>1 se guardan los IDs de los artistas correspondientes

            lt.addLast(nationalities, nationality) #Se agrega la nacionalidad al haber sido operada por 1ra vez
            lt.addLast(nationality_list, country) #Se guarda country en la misma posición que en nationalities

        else:
            country = lt.getElement(nationality_list, pos_nationality)
            lt.addLast(country, artistID)
        
        pos_artists += 1

    return nationality_list, nationalities


def getNationalityCountReq4(catalog):
    artworks = catalog["artworks"]
    nationality_list, nationalities = nationalityListReq4(catalog)
    final_list = lt.newList("ARRAY_LIST")

    while lt.size(nationalities)>0:  # size(nationalities) ciclos
        nationality = lt.removeFirst(nationalities)
        country_stack = stack.newStack()
        artworks_info = lt.newList("ARRAY_LIST")

        stack.push(country_stack, nationality)
        stack.push(country_stack, artworks_info)
        stack.push(country_stack, 0)
        stack.push(country_stack, 0)
        
        lt.addLast(final_list, country_stack)

    pos_artworks = 1
    size_artworks = lt.size(artworks)

    while pos_artworks<=size_artworks: #Realiza size(artworks) ciclos
        artwork = lt.getElement(artworks, pos_artworks)

        artwork_info = stack.newStack()
        stack.push(artwork_info, artwork["Dimensions"])
        stack.push(artwork_info, artwork["Medium"])
        stack.push(artwork_info, artwork["Date"])
        stack.push(artwork_info, artwork["ArtistName"])
        stack.push(artwork_info, artwork["Title"])
        stack.push(artwork_info, artwork["ArtworkID"])
        artworkNotInList = True

        authorsIDS = artwork["ArtistID"]
        authors_queue = splitAuthorsIDs(authorsIDS)
        
        while queue.size(authors_queue)>0: #No más de max(autores por obra) ciclos
            authorID = queue.dequeue(authors_queue)

            pos_nationality = 1
            found = False
            size_nationalities = lt.size(nationality_list)

            while (pos_nationality<=size_nationalities) and (not found): #No más de #países ciclos
                nationality = lt.getElement(nationality_list, pos_nationality)
                pos_ID = lt.isPresent(nationality, authorID) #No más de #maxArtistasNacionalidad ciclos

                if pos_ID != 0:
                    found = True
                    country_stack = lt.getElement(final_list, pos_nationality)
                    country_count = stack.pop(country_stack)
                    artwork_count = stack.pop(country_stack)
                    artworks_info = stack.pop(country_stack)
                    
                    if artworkNotInList:
                        lt.addLast(artworks_info, artwork_info)
                        artworkNotInList = False
                        artwork_count += 1

                    country_count += 1
                    
                    stack.push(country_stack, artworks_info)
                    stack.push(country_stack, artwork_count)
                    stack.push(country_stack, country_count)

                pos_nationality += 1

        pos_artworks+=1
    
    return final_list


"Requerimiento 5"
def calculateDimensionsReq5(depth, diameter, height, length, width):
    """
    #Calcula las dimensiones físicas (área o volumen) de cada obra dependiendo de la información que
    #se brinde. Se utilizan unidades de metro
"""
    data = lt.newList("ARRAY_LIST")
    lt.addLast(data, depth)
    lt.addLast(data, height)
    lt.addLast(data, length)
    lt.addLast(data, width)
    lt.addLast(data, diameter)
    
    dimensions_count = 0
    no_dimensions = True
    ans = -1

    pos = 1
    size = lt.size(data)

    #Se evalúa cada dimensión para saber cuántas tienen información útil
    while pos<=size: #O(1) porque size = 5
        dimension = lt.getElement(data, pos)
        if (dimension != "") and (dimension != "0"):
            lt.changeInfo(data, pos, float(dimension)) #O(1) porque se trata de ARRAY_LIST
            dimensions_count += 1
            no_dimensions = False
        else:
            lt.changeInfo(data, pos, 1)
        pos += 1

    #Se calcula el factor de conversión a unidades de metro
    factor = 10**(-2*dimensions_count)

    if no_dimensions==False:
        if diameter != "":
            diameter = lt.getElement(data, 5)
            height = lt.getElement(data, 2)
            ans = 3.1416 * ((diameter/2)**2) * height * factor/100
        
        else:
            depth = lt.getElement(data, 1)
            height = lt.getElement(data, 2)
            length = lt.getElement(data, 3)
            width = lt.getElement(data, 4)
            ans =  depth * height * length * width * factor

    return ans


def calculateSingularCostReq5(depth, diameter, height, length, weight, width):
    """
    #Calcula el costo de transportar cierta obra dadas sus dimensiones físicas y su peso.
    #Las obras con volumen tienen un costo de transporte muy inferior, puesto que 1cm^2 = 10^-4 m^2,
    #mientras que 1cm^3 = 10^-6 m^3
"""
    dimensions = calculateDimensionsReq5(depth, diameter, height, length, width)

    if dimensions == -1:
        dcost = 48
    else:
        dcost = dimensions*72
    
    max = dcost

    if (weight!="") and (weight!="0"):
        wcost = float(weight)*72

        if wcost > max:
            max = wcost

    return round(max,5)


def getInitPosReq5(artworks, department):
    """
    #Realiza a lo sumo max(obras por departamento) ciclos. Consigue la primera posición de la lista
    #en la que aparece una obra del departamento dado
"""
    pos1 = binary_search(artworks, department, DeptLowerThanGivenDepartment, DeptGreaterThanGivenDepartment) 
    index1 = pos1-1

    while index1>0:
        prev_element = lt.getElement(artworks, index1)

        if prev_element["Department"] == department:
            pos1 -= 1
            index1 -= 1
        else:
            break

    return pos1


def addInfoReq5(artwork_info, artwork, cost):
    lt.addLast(artwork_info, artwork["ArtworkID"])       #pos 1: ID de la obra
    lt.addLast(artwork_info, artwork["Title"])           #pos 2: Título de la orba
    lt.addLast(artwork_info, artwork["ArtistName"])      #pos 3: Nombres de los autores
    lt.addLast(artwork_info, artwork["Medium"])          #pos 4: Técnica de la obra
    lt.addLast(artwork_info, artwork["Date"])            #pos 5: Fecha de la obra
    lt.addLast(artwork_info, artwork["Dimensions"])      #pos 6: Dimensiones de la obra
    lt.addLast(artwork_info, artwork["Classification"])  #pos 7: Clasificación de la obra
    lt.addLast(artwork_info, str(cost))                  #pos 8: Costo de transporte


def addTOP5Req5(info_stack, general_list):
    for i in range(5, 0, -1): 
        element = lt.getElement(general_list, i)
        stack.push(info_stack, element)


def moveArtworksReq5(catalog, department):
    sortArtworks(catalog, 3, cmpArtworkByDepartment)
    artworks = catalog["artworks"]
    general_list = lt.newList("ARRAY_LIST")
    total_cost = 0
    total_weight = 0

    pos = getInitPosReq5(artworks, department)
    size_artworks = lt.size(artworks)

    while pos<=size_artworks: #Peor caso: size(artworks) recorridos
        artwork = lt.getElement(artworks, pos)
        artwork_info = lt.newList("ARRAY_LIST")

        if artwork["Department"] == department:
            cost = round(calculateSingularCostReq5(artwork["Depth"], artwork["Diameter"],
                                             artwork["Height"],artwork["Length"],
                                             artwork["Weight"], artwork["Width"]),3)
            addInfoReq5(artwork_info, artwork, cost)
            lt.addLast(general_list, artwork_info)    

            if artwork["Weight"] != "":
                total_weight += float(artwork["Weight"])

            total_cost += cost


        else:
            break

        pos += 1

    num_artworks = lt.size(general_list)

    most_expensive = stack.newStack()
    oldest = stack.newStack()

    mso.sort(general_list, cmpArtworksByCost)
    addTOP5Req5(most_expensive, general_list)

    mso.sort(general_list, cmpArtworksByDate)
    addTOP5Req5(oldest, general_list)

    return num_artworks, round(total_cost,3), round(total_weight,3), most_expensive, oldest
    

"""

# Funciones utilizadas para comparar elementos dentro de una lista
"Para Artistas"
def cmpArtistByBeginDate(artist1,artist2):
    return (float (artist1["BeginDate"]) < float(artist2["BeginDate"]))


def BeginDateLowerThanGivenDate(artist, date):            #Requerimiento 1
    return float(artist["BeginDate"]) < date


def BeginDateGreaterThanGivenDate(artist, date):          #Requerimiento 1
    return float(artist["BeginDate"]) > date


def cmpArtistByAuthorID(artist1, artist2):                #Requerimiento 2
    return artist1["ArtistID"] < artist2["ArtistID"]


"Para Obras"
def cmpArtworkByDateAcquired(artwork1,artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return artwork1["DateAcquired"] < artwork2["DateAcquired"]


def DateAcquiredLowerThanGivenDate(artwork,date):         #Requerimiento 2
    return artwork["DateAcquired"] < date


def DateAcquiredGreaterThanGivenDate(artwork,date):       #Requerimiento 2
    return artwork["DateAcquired"] > date


def AuthorIDLowerThanGivenID(artist, id):                 #Requerimiento 2
    return artist["ArtistID"] < id


def AuthorIDGreaterThanGivenID(artist, id):               #Requerimiento 2
    return artist["ArtistID"] > id


def compare_cantidad(cantidad1,cantidad2):                #Requerimiento 3
    return float(lt.getElement(cantidad1,1)) > float(lt.getElement(cantidad2,1))


def cmpByNumAuthors(nationality1, nationality2):          #Requerimiento 4
    return stack.top(nationality1) > stack.top(nationality2)


def cmpArtworkByDepartment(artwork1,artwork2):            #Requerimiento 5
    return artwork1["Department"] < artwork2["Department"]


def cmpArtworksByCost(artwork1,artwork2):                 #Requerimiento 5
    cost1 = lt.getElement(artwork1, 8)
    cost2 = lt.getElement(artwork2, 8)
    return float(cost1) > float(cost2)


def cmpArtworksByDate(artwork1,artwork2):                 #Requerimiento 5
    date1 = lt.getElement(artwork1, 5)
    date2 = lt.getElement(artwork2, 5)

    if date1 == "":
        date1 = 9999
    if date2 == "":
        date2 = 9999

    return int(date1) < int(date2)


def DeptLowerThanGivenDepartment(artwork,department):     #Requerimiento 5
    return artwork["Department"] < department


def DeptGreaterThanGivenDepartment(artwork,department):   #Requerimiento 5
    return artwork["Department"] > department


# Funciones de ordenamiento
def sortArtists(catalog, cmpfunction):
    mso.sort(catalog['artists'],cmpfunction)


def sortArtworks(catalog, cmpfunction):
    mso.sort(catalog['artworks'],cmpfunction)


def sortReq4(final_list):
    mso.sort(final_list, cmpByNumAuthors)