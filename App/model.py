"""
Reto 2 - model.py

Carlos Arturo Holguín Cárdenas
Daniel Hernández Pineda

 """


from tabulate import DataRow
import config as cf
from datetime import datetime, date
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import queue
from DISClib.ADT import stack
from DISClib.Algorithms.Sorting import shellsort as sso
from DISClib.Algorithms.Sorting import mergesort as mso
assert cf

# ==============================================
# Construccion de modelos
# ==============================================

def newCatalog():
    """
    Inicializa el catálogo de obras y artistas
    """
    catalog = {"artworksLab5": None,
               "NationalityArtistLab6'": None,
               "MapLab6": None}
    catalog = {"artistsREQ1":None}
    catalog = {"artworksREQ2":None}
    catalog = {"artistREQ2":None}
    catalog = {"IdWArtworkREQ3":None,
               "Name-IdREQ3":None,
               "ArtworkAndDataREQ3":None}

    """
    Este indice crea un map cuya llave es el autor del libro
    """
    
    catalog['artworksLab5'] = mp.newMap(140000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   )
     
    catalog['NationalityArtistLab6'] = mp.newMap(16000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   )
    
    catalog['MapLab6'] = mp.newMap(1000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   )
    
    catalog['artistsREQ1'] = mp.newMap(1000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   )
    
    catalog['artworksREQ2'] = mp.newMap(1000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   )
    
    catalog['artistREQ2'] = mp.newMap(1000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   )
    
    catalog['Name-IdREQ3'] = mp.newMap(1000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   )
    
    catalog['IdWArtworkREQ3'] = mp.newMap(1000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   )
    
    catalog['ArtworkAndDataREQ3'] = mp.newMap(1000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   )
    
    return catalog



# ==============================================
# Funciones para agregar informacion al catalogo
# ============================================

def AddMediumLab5(catalog, artwork):
    DataForMedium=newArtworksLab5(artwork['Title'],artwork['Date'],artwork['Medium'])
    mp.put(catalog['artworksLab5'],artwork['ObjectID'],DataForMedium)


def AddIdsLab6(catalog, artwork):
    "Los datos tienen la siguiente forma: 'key'= Nationality, 'value' = Lista de obras"
    MapLab6=catalog["MapLab6"]
    NationalityArtist=catalog["NationalityArtistLab6"]
    IDsArtwork=artwork["ConstituentID"]
    IDsClean=splitAuthorsIDs(IDsArtwork)
    largeIDsClean=lt.size(IDsClean)
    if largeIDsClean==1:
        id=lt.getElement(IDsClean,1)
        entry= mp.get(NationalityArtist, id)
        NationalityAtM=me.getValue(entry)
        ExistNationality= mp.contains(MapLab6, NationalityAtM)
        if ExistNationality:
            entry1=mp.get(MapLab6, NationalityAtM)
            ValueListNames=me.getValue(entry1)
            lt.addLast(ValueListNames,artwork["Title"])
            mp.put(MapLab6,NationalityAtM,ValueListNames)
        else:
            ListNamesArtwork=listLab6(artwork["Title"])
            mp.put(MapLab6,NationalityAtM,ListNamesArtwork)
    
    elif largeIDsClean>1:
        i=1
        while i<=largeIDsClean:
            id=lt.getElement(IDsClean,i)
            entry= mp.get(NationalityArtist, id)
            NationalityAtM=me.getValue(entry)
            i+=1
            ExistNationality= mp.contains(MapLab6, NationalityAtM)
            if ExistNationality:
                entry1=mp.get(MapLab6, NationalityAtM)
                ValueListNames=me.getValue(entry1)
                lt.addLast(ValueListNames,artwork["Title"])
                mp.put(MapLab6,NationalityAtM,ValueListNames)
            else:
                ListNamesArtwork=listLab6(artwork["Title"])
                mp.put(MapLab6,NationalityAtM,ListNamesArtwork)

    return MapLab6



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


#Lab 5
def newArtworksLab5(title, date, Medium):
    DataNecessary = {'Title': '',
           'Date': '',
           'Medium': '',
                    }
    DataNecessary['Title']=title
    DataNecessary['Date']=date
    DataNecessary['Medium']=Medium
    return DataNecessary


#Lab 6
def listLab6(NameArtwork):
    DataNecessary=lt.newList("ARRAY_LIST")
    lt.addLast(DataNecessary,NameArtwork)
    return DataNecessary


def FindNationalityArtist(catalog, artist):
    "Los datos tienen la siguiente forma: 'key'= Id, 'value' = Nationality"
    NationalityArtist=catalog["NationalityArtistLab6"]
    mp.put(NationalityArtist, artist["ConstituentID"], artist["Nationality"])
    return NationalityArtist



# Creacion de diccionario para requerimiento 1

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


# Creacion de diccionario para requerimiento 2

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

#Creacion de diccionario para rquerimiento 3
def listREQ3(Title):
    DataNecessary =lt.newList("ARRAY_LIST")
    lt.addLast(DataNecessary,Title)
    return DataNecessary    

def NameIdREQ3(catalog, artist):
    "Los datos tienen la siguiente forma: 'key'=  DisplayName, 'value' = ConstituentID"

    MapNameId=catalog["Name-IdREQ3"]
    mp.put(MapNameId, artist["DisplayName"], artist["ConstituentID"])
    return MapNameId

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

# ==============================================
# Funciones de consulta
# ==============================================

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


#Funcion de consulta Lab 5
def REQLab5(catalog,Medium):
    ArtworksMoreOld=lt.newList()
    MediumOfCatalog=catalog["artworksLab5"]
    for n in lt.iterator(mp.keySet(MediumOfCatalog)):
        DataAtMoment=mp.get(MediumOfCatalog,n)
        ValueAtMoment=me.getValue(DataAtMoment)
        MediumAtMoment=ValueAtMoment['Medium']
        if MediumAtMoment==Medium:
            lt.addLast(ArtworksMoreOld,ValueAtMoment)
    sortMediumDate(ArtworksMoreOld)
    ArtworksOfMedium=lt.size(ArtworksMoreOld)
    return ArtworksMoreOld, ArtworksOfMedium


#Funcion de consulta Lab 6
def REQLab6(catalog, Nationality):
    MapNationality=catalog["MapLab6"]
    Entry=mp.get(MapNationality,Nationality)
    ValueAtMoment=me.getValue(Entry)
    LargeValue=lt.size(ValueAtMoment)
    return LargeValue


# ==============================================
#Funcion de consulta requerimiento 1
# ============================================

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

# ==============================================
#Funcion de consulta requerimiento 2
# ============================================

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
    sortDateAcquired(ArtworksListFinal)
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

# ============================================
#Funcion de consulta requerimiento 3
# ============================================
def GetTechniquesReq3(catalog,Name):
    max=0
    MediumMoreUsed=''
    MapMediumData=mp.newMap(100,
                            maptype='PROBING',
                            loadfactor=0.5,)
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



# ================================================================
# Funciones de comparación
# ================================================================

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


# Funcion de comparacion Lab 5
def cmpDate(Date1,Date2):
    return int(Date1['Date'])<int(Date2['Date'])


# Funcion de comparacion REQ 2
def cmpDateAcquired(Date1,Date2):
    return (Date1['DateAcquired'])<(Date2['DateAcquired'])



# ==============================
# Funciones de ordenamiento
# ==============================

# Funcion de ordenamiento Lab 5
def sortMediumDate(ListaMDLab5):
    mso.sort(ListaMDLab5,cmpDate)


def sortReq4(final_list):
    mso.sort(final_list, cmpByNumAuthors)


# Funcion de ordenamiento REQ2
def sortDateAcquired(ListREQ2):
    mso.sort(ListREQ2,cmpDateAcquired)

