"""
Reto 2 - model.py

Carlos Arturo Holguín Cárdenas
Daniel Hernández Pineda

 """

import config as cf
from datetime import datetime
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import stack
from DISClib.Algorithms.Sorting import mergesort as mso
assert cf

# ==============================================
# Construccion de modelos
# ==============================================
def newCatalog():
    """
    Inicializa el catálogo de obras y artistas
    """
    catalog = {"artistsREQ1":None,
               "artworksREQ2":None,
               "artistREQ2":None,
               "IdWArtworkREQ3":None,
               "Name-IdREQ3":None,
               "ArtworkAndDataREQ3":None,
               "ConstituentID_Directory": None,
               "NationalityArtistReq4": None,
               "MapReq4": None,
               "MapReq5": None}

    
    catalog['artistsREQ1'] = mp.newMap(1000,
                                   maptype='CHAINING',
                                   loadfactor=4.0)
    
    catalog['artworksREQ2'] = mp.newMap(1000,
                                   maptype='PROBING',
                                   loadfactor=0.5)
    
    catalog['artistREQ2'] = mp.newMap(1000,
                                   maptype='PROBING',
                                   loadfactor=0.5)
    
    catalog['Name-IdREQ3'] = mp.newMap(1000,
                                   maptype='PROBING',
                                   loadfactor=0.5)
    
    catalog['IdWArtworkREQ3'] = mp.newMap(1000,
                                   maptype='PROBING',
                                   loadfactor=0.5)
    
    catalog['ArtworkAndDataREQ3'] = mp.newMap(1000,
                                   maptype='PROBING',
                                   loadfactor=0.5)

    catalog['ConstituentID_Directory'] = mp.newMap(15500,
                                                   maptype='PROBING',
                                                   loadfactor=0.5) 
    
    catalog['NationalityArtistReq4'] = mp.newMap(1000,
                                                 maptype='CHAINING',
                                                 loadfactor=4.0)
    
    catalog['MapReq4'] = mp.newMap(1000,
                                   maptype='PROBING',
                                   loadfactor=0.5)


    catalog['MapReq5'] = mp.newMap(30,
                                   maptype='PROBING',
                                   loadfactor=0.5)
    
    return catalog



# ==============================================
# Funciones para agregar informacion al catalogo
# ============================================
def AddIDName(catalog, artist):
    "Los datos tienen la siguiente forma: 'key'= ConstituentID, 'value' = Name"
    artists_ids_map = catalog["ConstituentID_Directory"]
    mp.put(artists_ids_map, artist["ConstituentID"], artist["DisplayName"])

    return artists_ids_map


def addArtistREQ1(catalog, artist):
    "Los datos quedan con la siguiente forma 'key'= Date , 'value'= [Name, EndDate, Nationality, Gender],[....]"

    DatesAndAuthors=catalog["artistsREQ1"]
    ExistDate= mp.contains(DatesAndAuthors,artist["BeginDate"])
    if ExistDate:
        DataAtREQ1=newArtistREQ1(artist['DisplayName'],artist['EndDate'],artist['Nationality'],artist['Gender'],artist["BeginDate"])
        entry= mp. get(DatesAndAuthors,artist["BeginDate"])
        DataOfBeginDate= me.getValue(entry)
        lt.addLast(DataOfBeginDate,DataAtREQ1)
        mp.put(DatesAndAuthors,artist["BeginDate"],DataOfBeginDate)
    else:
        DataAtREQ1=listREQ1(artist['DisplayName'],artist['EndDate'],artist['Nationality'],artist['Gender'], artist["BeginDate"])
        mp.put(DatesAndAuthors,artist["BeginDate"],DataAtREQ1)
    return DatesAndAuthors


def AddArtworksREQ2(catalog,artwork):
    ArtworksInDate=catalog['artworksREQ2']
    ExistDate= mp.contains(ArtworksInDate, artwork["DateAcquired"])
    if ExistDate:
        DataAtREQ2=newArtworkREQ2(artwork["Title"],artwork["DateAcquired"],artwork["Medium"],artwork["Dimensions"],artwork["CreditLine"],artwork["ConstituentID"])
        entry= mp. get(ArtworksInDate,artwork["DateAcquired"])
        DataOfDateAcquired= me.getValue(entry)
        lt.addLast(DataOfDateAcquired,DataAtREQ2)
        mp.put(ArtworksInDate,artwork["DateAcquired"],DataOfDateAcquired)
    else:
        DataAtREQ2=listREQ2(artwork["Title"],artwork["DateAcquired"],artwork["Medium"],artwork["Dimensions"],artwork["CreditLine"],artwork["ConstituentID"])
        mp.put(ArtworksInDate,artwork["DateAcquired"],DataAtREQ2)
    return ArtworksInDate


def IDwithNameREQ2(catalog, artist):
    "Los datos tienen la siguiente forma: 'key'= ConstituentID, 'value' = DisplayName"
    mp.put(catalog['artistREQ2'],artist["ConstituentID"],artist["DisplayName"])


def AddArtworksWidREQ3(catalog,artwork):
    IdWArtworks=catalog['IdWArtworkREQ3']
    IDsArtwork=artwork["ConstituentID"]
    IDsClean=splitAuthorsIDs(IDsArtwork)
    largeIDsClean=lt.size(IDsClean)
    if largeIDsClean==1:
        ExistId= mp.contains(IdWArtworks, lt.getElement(IDsClean, 1))
        if ExistId:
            EntryIdArt=mp.get(IdWArtworks,lt.getElement(IDsClean, 1))
            TitleArtworks=me.getValue(EntryIdArt)
            lt.addLast(TitleArtworks,artwork["Title"])
            mp.put(IdWArtworks, lt.getElement(IDsClean, 1), TitleArtworks)
        else:
            ListTitle=listREQ3(artwork["Title"])
            mp.put(IdWArtworks, lt.getElement(IDsClean, 1), ListTitle)
    
    elif largeIDsClean>1:
        i=1
        while i<=largeIDsClean:
            id=lt.getElement(IDsClean,i)
            ExistId= mp.contains(IdWArtworks, id)
            if ExistId:
                EntryIdArt=mp.get(IdWArtworks,id)
                TitleArtworks=me.getValue(EntryIdArt)
                lt.addLast(TitleArtworks,artwork["Title"])
                mp.put(IdWArtworks, id, TitleArtworks)
            else:
                ListTitle=listREQ3(artwork["Title"])
                mp.put(IdWArtworks, id, ListTitle)
            i+=1
    return IdWArtworks


def  DataNecessaryREQ3(Title, Date, Medium ,Dimensions):
    DataNecessary=lt.newList("ARRAY_LIST")
    lt.addLast(DataNecessary, Title)
    lt.addLast(DataNecessary, Date)
    lt.addLast(DataNecessary, Medium)
    lt.addLast(DataNecessary, Dimensions)
    return DataNecessary


def AddTitleAndDataREQ3(catalog,artwork):
    ArtworkAndDataREQ3=catalog["ArtworkAndDataREQ3"]
    mp.put(ArtworkAndDataREQ3, artwork['Title'], DataNecessaryREQ3(artwork['Title'],artwork['Date'], artwork['Medium'],artwork['Dimensions']))
    return ArtworkAndDataREQ3


def AddArtistsNationalitiesREQ4(catalog, artist):
    "Los datos tienen la siguiente forma: 'key'= Id, 'value' = Nationality"
    artists_nationalities_map = catalog["NationalityArtistReq4"]
    nationality = artist["Nationality"]

    if (nationality == "") or (nationality == "Nationality unknown"):
        nationality = "Unknown"

    mp.put(artists_nationalities_map, artist["ConstituentID"], nationality)

    return artists_nationalities_map


def AddArtworksREQ4(catalog, artwork):
    "Los datos tienen la siguiente forma: 'key'= Nationality, 'value' = Lista de obras"
    Map = catalog["MapReq4"]
    NationalityArtist = catalog["NationalityArtistReq4"]

    artwork_info,IDs_list = getArtworkInfo(catalog, artwork)    #Obtener información de la obra

    for id in lt.iterator(IDs_list):
        entry = mp.get(NationalityArtist, id)
        nationality = me.getValue(entry)
        nationality_exists= mp.contains(Map, nationality)
        
        if not nationality_exists:
            artworks_list = lt.newList("ARRAY_LIST")      #Crear lista de obras para la nacionalidad
            lt.addLast(artworks_list, artwork_info)    
            mp.put(Map, nationality, artworks_list)       #Añadir lista de obras al mapa en la nacionalidad

        else:
            entry1 = mp.get(Map, nationality)             #Obtener entrada del mapa donde se ubica la nacionalidad
            artworks_list = me.getValue(entry1)           #Extraer la lista de obras de la nacionalidad
            lt.addLast(artworks_list, artwork_info)
            mp.put(Map, nationality, artworks_list)       #Actualizar lista de obras


def AddArtworksREQ5(catalog, artwork):
    "Los datos tienen la siguiente forma: 'key'= Department, 'value' = Lista de obras"
    Map = catalog["MapReq5"]
    department = artwork["Department"]
    artwork_info,trash = getArtworkInfo(catalog, artwork)      #Obtener información de la obra

    department_exists= mp.contains(Map, department)

    if not department_exists:
        artworks_list = lt.newList("ARRAY_LIST")      #Crear lista de obras para el departamento
        lt.addLast(artworks_list, artwork_info)    
        mp.put(Map, department, artworks_list)        #Añadir lista de obras al mapa en el departamento

    else:
        entry1 = mp.get(Map, department)              #Obtener entrada del mapa donde se ubica el departamento
        artworks_list = me.getValue(entry1)           #Extraer la lista de obras del departamento
        lt.addLast(artworks_list, artwork_info)
        mp.put(Map, department, artworks_list)        #Actualizar lista de obras



# ==============================================
# Funciones para creacion de datos
# ==============================================
def splitAuthorsIDs(authorsIDs):
    """
    Separa los IDs de los autores de una obra en una lista
    """
    authors=authorsIDs.replace(",","")
    authors = authors.replace("[","")
    authors=authors.replace("]","")

    authorsIDs_list = lt.newList("ARRAY_LIST")
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


def getAuthorsNames(catalog, artwork):
    """
    Se obtienen los nombres de los artistas de una obra a partir de sus IDs
    """
    directory = catalog["ConstituentID_Directory"]
    IDs_list = splitAuthorsIDs(artwork["ConstituentID"])          #Obtener IDs de artistas en una lista
    IDs_lenght = lt.size(IDs_list)
    authors = ""                                                  #str que contendrá los nombres de los artistas

    i= 1
    while i <= IDs_lenght:
        artist_ID = lt.getElement(IDs_list, i)
        artist_name = me.getValue(mp.get(directory, artist_ID))

        if authors == "":
            authors = artist_name
        else:
            authors += ", " + artist_name
        i += 1

    return authors, IDs_list


def getArtworkInfo(catalog, artwork):
    """
    Se filtra la información útil para las obras
    """
    artwork_final = {}
    authors, IDs_list = getAuthorsNames(catalog, artwork)

    artwork_final["ObjectID"] = artwork["ObjectID"]
    artwork_final["Title"] = artwork["Title"]
    artwork_final["ArtistsNames"] = authors
    artwork_final["Date"] = artwork["Date"]
    artwork_final["Medium"] = artwork["Medium"]
    artwork_final["Dimensions"] = artwork["Dimensions"]
    artwork_final["Classification"] = artwork["Classification"]

    artwork_final["Depth"] = artwork["Depth (cm)"]
    artwork_final["Diameter"] = artwork["Diameter (cm)"]
    artwork_final["Height"] = artwork["Height (cm)"]
    artwork_final["Length"] = artwork["Length (cm)"]
    artwork_final["Weight"] = artwork["Weight (kg)"]
    artwork_final["Width"] = artwork["Width (cm)"]

    return artwork_final, IDs_list


#Requerimiento 1
def newArtistREQ1( Name, EndDate, Nationality, Gender, BeginDate):    
    DataNecessary = {
            'Name':'', 
            'EndDate':'',
            'Nationality':'',
            'Gender':'',
            'BeginDate':'' 
                  }

    DataNecessary['Name']=Name
    DataNecessary['EndDate']=EndDate
    DataNecessary['Nationality']=Nationality
    DataNecessary['Gender']=Gender
    DataNecessary['BeginDate']=BeginDate
    return DataNecessary


def listREQ1( Name, EndDate, Nationality, Gender, BeginDate):
    MapnREQ1=newArtistREQ1(Name, EndDate, Nationality, Gender, BeginDate)
    DataNecessary =lt.newList("ARRAY_LIST")   
    lt.addLast(DataNecessary,MapnREQ1)
    return DataNecessary


#Requerimiento 2
def newArtworkREQ2(Title, DateAcquired, Medium, Dimensions,CreditLine,ConstituentID):
    
    #Los datos quedan con la siguiente forma 'key'= DateAcquired , 
    #'value'= [Title, DateAcquired, Medium , CreditLine, ConstituentID],[....]"
    
    DataNecessary = {
            'Title':'', 
            'Artist(s)':'',
            'DateAcquired':'',
            'Medium':'',
            'Dimensions':'',
            'CreditLine':'', 
            'ConstituentID':''      
                     }
    
    DataNecessary['Title']=Title
    DataNecessary['DateAcquired']=DateAcquired
    DataNecessary['Medium']=Medium
    DataNecessary['Dimensions']=Dimensions
    DataNecessary['CreditLine']=CreditLine
    DataNecessary['ConstituentID']=ConstituentID
    return DataNecessary


def listREQ2(Title, DateAcquired, Medium, Dimensions,CreditLine,ConstituentID):
    MapnREQ2=newArtworkREQ2(Title, DateAcquired, Medium, Dimensions,CreditLine,ConstituentID)
    DataNecessary =lt.newList("ARRAY_LIST")   
    lt.addLast(DataNecessary,MapnREQ2)
    return DataNecessary    


#Requerimiento 3
def listREQ3(Title):
    DataNecessary =lt.newList("ARRAY_LIST")
    lt.addLast(DataNecessary,Title)
    return DataNecessary    


def NameIdREQ3(catalog, artist):
    "Los datos tienen la siguiente forma: 'key'=  DisplayName, 'value' = ConstituentID"

    MapNameId=catalog["Name-IdREQ3"]
    mp.put(MapNameId, artist["DisplayName"], artist["ConstituentID"])
    return MapNameId



# ==============================================
# Funciones de consulta
# ==============================================

#Requerimiento 1
def getArtistsRangeReq1(catalog, date_initial, date_final):
    MapForREQ1=catalog["artistsREQ1"]
    listFinal=lt.newList("ARRAY_LIST")
    i=0
    for i in range(date_initial,(date_final+1)):
        entry= mp.get(MapForREQ1,str(i))
        DataOfBeginDate= me.getValue(entry)
        LargeAtMoment=lt.size(DataOfBeginDate)
        j=1
        while j<=LargeAtMoment:
            Element=lt.getElement(DataOfBeginDate,j)
            lt.addLast(listFinal,Element)
            j+=1
    TotalOfArtists=lt.size(listFinal)
    
    return listFinal, TotalOfArtists


#Requerimiento 2
def getArtworksInfoReq2(catalog, date_initial, date_final):
    ArtworksListFinal=lt.newList("ARRAY_LIST")
    ArtworksWithDate=catalog["artworksREQ2"]
    NumberOfArtworksPurchase=0                                 #Corregir cuando no existe una fecha y aparece asi ''
    for n in lt.iterator(mp.keySet(ArtworksWithDate)):
        if n == "":
            DateInThisCase="1111-01-01"
            dateForCompare=datetime.strptime(DateInThisCase, "%Y-%m-%d")
        if n != "":
            dateForCompare=datetime.strptime(n, "%Y-%m-%d")
        
        if date_initial<=dateForCompare and dateForCompare<=date_final:
            entry= mp.get(ArtworksWithDate,str(n))
            DataOfDateAcquired= me.getValue(entry)
            LargeAtMoment=lt.size(DataOfDateAcquired)
            j=1
            while j<=LargeAtMoment:
                Element=lt.getElement(DataOfDateAcquired,j)
                Ids=splitAuthorsIDs(Element["ConstituentID"])    #LLista con los IDs
                Artist=FindDisplayNameREQ2(Ids,catalog)
                Element["Artist(s)"]=Artist
                if Element["CreditLine"]=="Purchase":
                    NumberOfArtworksPurchase+=1
                lt.addLast(ArtworksListFinal,Element)
                j+=1
    NumberOfArtworks=lt.size(ArtworksListFinal)
    sortDateAcquiredREQ2(ArtworksListFinal)
    return ArtworksListFinal,NumberOfArtworks,NumberOfArtworksPurchase


def FindDisplayNameREQ2(ListIDs,catalog):
    i=1
    LargeOfConstituent=lt.size(ListIDs)
    MapIDs=catalog["artistREQ2"]
    ListArtists=lt.newList("ARRAY_LIST")
    StringArtist=''
    
    while i<=LargeOfConstituent:
        ElementAtMoment=lt.getElement(ListIDs,i)
        entry= mp.get(MapIDs,ElementAtMoment)
        DisplayName= me.getValue(entry)
        i+=1
        StringArtist=StringArtist+" "+str(DisplayName)
    lt.addLast(ListArtists,StringArtist)
        
    return ListArtists


#Requerimiento 3
def GetTechniquesReq3(catalog,Name):
    max=0
    MediumMoreUsed=''
    MapMediumData=mp.newMap(100,
                            maptype='PROBING',
                            loadfactor=0.5)
    i=1
    MapNameId=catalog["Name-IdREQ3"]
    MapIdTitle=catalog['IdWArtworkREQ3']
    MapTitleAndData= catalog["ArtworkAndDataREQ3"]
    EntryId=mp.get(MapNameId,Name)
    IdOfArtist=me.getValue(EntryId)
    EntryIdForTitle=mp.get(MapIdTitle,IdOfArtist)
    ListOfTitles=me.getValue(EntryIdForTitle)
    NumberOfArtworks=lt.size(ListOfTitles)
    while i<=NumberOfArtworks:
        TitleAtMoment=lt.getElement(ListOfTitles, i)
        EntryTitleData=mp.get(MapTitleAndData, TitleAtMoment)
        listTitleData=me.getValue(EntryTitleData)
        CreateTableHashREQ3(listTitleData,MapMediumData)
        i+=1
    
    NumberOfTechniques=mp.size(MapMediumData)
    for n in lt.iterator(mp.keySet(MapMediumData)):
        EntryMediumArt=mp.get(MapMediumData,n)
        TitleOfArtworks=me.getValue(EntryMediumArt)
        NumberOfTitleM=lt.size(TitleOfArtworks)
        if NumberOfTitleM>max:
            max=NumberOfTitleM
            MediumMoreUsed=n
    
    EntryMediumMoreArt=mp.get(MapMediumData, MediumMoreUsed)
    listMediumMoreUsed=me.getValue(EntryMediumMoreArt)
    return NumberOfArtworks, NumberOfTechniques, MediumMoreUsed, listMediumMoreUsed 


def CreateTableHashREQ3(listTitleData, MapMediumData):
    Medium=lt.getElement(listTitleData,3)
    ExistMedium=mp.contains(MapMediumData, Medium)
    if ExistMedium:
        EntryMediumData=mp.get(MapMediumData,Medium)
        ListData=me.getValue(EntryMediumData)
        lt.addLast(ListData, listTitleData)
    else:
        ListForData=lt.newList("ARRAY_LIST")
        lt.addLast(ListForData,listTitleData)
        mp.put(MapMediumData,Medium,ListForData)
    return MapMediumData


#Requerimiento 4
def counterREQ4(catalog, nationality):
    """
    Indica la cantidad de obras encontradas para una nacionalidad dada
    """
    MapNationalities = catalog["MapReq4"]
    entry = mp.get(MapNationalities, nationality)
    artworks_list = me.getValue(entry)
    count_value = lt.size(artworks_list)

    return count_value


def getCountListREQ4(catalog):
    """
    Crea una lista de tuplas tipo (nacionalidad, conteo_de_obras), y retorna el TOP 10
    """
    MapNationalities = catalog["MapReq4"]
    NationalityCountList = lt.newList("ARRAY_LIST")    

    nationalities = mp.keySet(MapNationalities)

    for nationality in lt.iterator(nationalities):    #Realiza numero_de_nacionalidades ciclos
        nationality_count = counterREQ4(catalog, nationality)
        info_tuple = nationality, nationality_count
        lt.addLast(NationalityCountList, info_tuple)

    sortREQ4(NationalityCountList)                    #O(nlog(n)) por usar merge_sort
    final_list = lt.subList(NationalityCountList, 1, 10)   #TOP 10 de nacionalidades con más obras

    return final_list


def REQ4(catalog):
    "Se reúne el TOP 10 ya obtenido con la información de la nacionalidad con más obras"
    MapNationalities = catalog["MapReq4"]
    NationalityCountList = getCountListREQ4(catalog)
    most_authors = lt.firstElement(NationalityCountList)[0]

    entry = mp.get(MapNationalities, most_authors)
    artworks_list = me.getValue(entry)

    return NationalityCountList, artworks_list


#Requerimiento 5
def calculateDimensionsReq5(depth, diameter, height, length, width):
    """
    Calcula las dimensiones físicas (área o volumen) de cada obra dependiendo de la información que
    se brinde. Se utilizan unidades de metro
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
    Calcula el costo de transportar cierta obra dadas sus dimensiones físicas y su peso.
    Las obras con volumen tienen un costo de transporte muy inferior, puesto que 1cm^2 = 10^-4 m^2,
    mientras que 1cm^3 = 10^-6 m^3
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

    return round(max,3)


def addTOP5Req5(info_stack, artworks_list):
    for i in range(5, 0, -1): 
        element = lt.getElement(artworks_list, i)
        stack.push(info_stack, element)


def REQ5(catalog, department):
    """
    Se manipula la lista de obras del departamento dado, añadiéndole a cada obra su respectivo costo. Al mismo
    tiempo, se realizan los cálculos pertinentes para el requerimiento
    """
    MapDepartments = catalog["MapReq5"]
    department_entry = mp.get(MapDepartments, department)
    artworks_list = me.getValue(department_entry)

    total_cost = 0
    total_weight = 0

    for artwork in lt.iterator(artworks_list):   #Calcula el costo para cada una de las obras del departamento
        cost = calculateSingularCostReq5(artwork["Depth"], artwork["Diameter"], artwork["Height"],
                                         artwork["Length"], artwork["Weight"], artwork["Width"])
        artwork["TransCost"] = cost  

        if artwork["Weight"] != "":
            total_weight += float(artwork["Weight"])

        total_cost += cost

    num_artworks = lt.size(artworks_list)

    most_expensive = stack.newStack()
    oldest = stack.newStack()

    #Los ordenamientos contribuyen a tiempos de ejecución altos!
    mso.sort(artworks_list, cmpArtworksByCost)      #5 más costosos
    addTOP5Req5(most_expensive, artworks_list)
                                                    
    mso.sort(artworks_list, cmpArtworksByDate)      #5 más antiguos
    addTOP5Req5(oldest, artworks_list)

    return num_artworks, round(total_cost,3), round(total_weight,3), most_expensive, oldest



# ================================================================
# Funciones de comparación
# ================================================================

def cmpDateAcquired(Date1,Date2):                         #Requerimiento 2
    return (Date1['DateAcquired'])<(Date2['DateAcquired'])


def cmpByNumAuthors(nationality1, nationality2):          #Requerimiento 4
    return nationality1[1] > nationality2[1]


def cmpArtworksByCost(artwork1,artwork2):                 #Requerimiento 5
    cost1 = artwork1["TransCost"]
    cost2 = artwork2["TransCost"]
    return float(cost1) > float(cost2)


def cmpArtworksByDate(artwork1,artwork2):                 #Requerimiento 5
    date1 = artwork1["Date"]
    date2 = artwork2["Date"]

    if date1 == "":
        date1 = 9999
    if date2 == "":
        date2 = 9999

    return int(date1) < int(date2)



# ==============================
# Funciones de ordenamiento
# ==============================
def sortDateAcquiredREQ2(ListREQ2):
    mso.sort(ListREQ2,cmpDateAcquired)


def sortREQ4(lst):
    mso.sort(lst, cmpByNumAuthors)