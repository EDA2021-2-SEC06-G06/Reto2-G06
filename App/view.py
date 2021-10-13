"""
Reto 2 - view.py

Carlos Arturo Holguín Cárdenas
Daniel Hernández Pineda

 """

import config as cf
import sys
import controller
from datetime import datetime, date
from DISClib.ADT import list as lt
from DISClib.ADT import queue
from DISClib.ADT import stack
from time import process_time
from tabulate import tabulate
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


def printMenu():
    print("\n\n-----------------------------------------")
    print("Bienvenido al menú de opciones")
    print("-----------------------------------------")
    print("Opciones preliminares")
    print("1- Cargar datos")
    print("-----------------------------------------")
    print("Requerimientos")
    print("100- Mostrar las n obras más antiguas para un medio específico")
    print("200- Numero total de obras de una nacionalidad")
    print("10- Consultar Requerimiento 1")
    print("20- Consultar Requerimiento 2")
    print("30- Consultar Requerimiento 3")
    print("40- Consultar Requerimiento 4")
    print("50- Consultar Requerimiento 5")
    print("-----------------------------------------")
    print("0- Salir\n")


def initCatalog():
    """
    Inicializa el catálogo
    """
    return controller.initCatalog()


def loadData(catalog, file_size):
    """
    Carga las obras en la estructura de datos
    """
    controller.loadData(catalog, file_size)



#FUNCIONES DEL RETO 1

def printFirst(lst, num):
    """
    Imprime los primeros num elementos de la lista
    """
    for pos in range(1,num+1):
        print(lt.getElement(lst, pos))
        print("")


def printLast(lst, num):
    """
    Imprime los últimos num elementos de la lista.
    """
    for x in range(num-1, -1,-1):
        pos = lt.size(lst) - x
        print(lt.getElement(lst, pos))
        print("")


def adjustlenght(text, step):
    """
    Inserta renglones en una cadena de caracteres para que se ajuste al formato de una tabla
    """
    lenght = len(text)

    for n in range(step, 20*step + 1, step):
        if lenght > n:
            text = text[:n] + "\n" + text[n:]
    
    return text


def printReq1Table(lst):
    """
    #Imprime la tabla del Requerimiento 1
    """
    headers = ["Name", "BeginDate", "EndDate", "Nationality", "Gender"]
    table = []

    for pos in range(1,4):
        artist = lt.getElement(lst, pos)
        c1 = artist["Name"]
        c2 = artist["BeginDate"]
        c3 = artist["EndDate"]
        c4 = artist["Nationality"]
        if c4 == "0":
            c4 = "--"
        c5 = artist["Gender"]
        if c5 == "":
            c5 = "--"

        table.append([c1,c2,c3,c4,c5])
     

    for x in range(2, -1,-1):
        pos = lt.size(lst) - x
        artist = lt.getElement(lst, pos)      
        c1 = artist["Name"]
        c2 = artist["BeginDate"]
        c3 = artist["EndDate"]
        if c3 == "0":
            c3 = "--"
        c4 = artist["Nationality"]
        if c4 == "":
            c4 = "--"
        c5 = artist["Gender"]
        if c5 == "":
            c5 = "--"

        table.append([c1,c2,c3,c4,c5])

    print(tabulate(table, headers, tablefmt="grid"))


def printReq2Table(lst):
    """
    #Imprime la tabla del Requerimiento 2
"""
    headers = ['Title','ArtistsNames',"DateAcquired","Medium","Dimensions"]
    table = []

    if lt.size(lst)>=3:
        for pos in range(1,4):
            lista = lt.getElement(lst, pos)
            c1 = adjustlenght(lista["Title"], 12)
            c2 = adjustlenght(lt.getElement(lista["Artist(s)"],1), 18)
            c3 = adjustlenght(lista["DateAcquired"], 15)
            c4 = adjustlenght(lista["Medium"], 15)
            c5 = adjustlenght(lista["Dimensions"], 15)
            

            table.append([c1,c2,c3,c4,c5])
     

        for x in range(2, -1,-1):
            pos = lt.size(lst) - x
            lista = lt.getElement(lst, pos)
            c1 = adjustlenght(lista["Title"], 12)
            c2 = adjustlenght(lt.getElement(lista["Artist(s)"],1), 18)
            c3 = adjustlenght(lista["DateAcquired"], 15)
            c4 = adjustlenght(lista["Medium"], 15)
            c5 = adjustlenght(lista["Dimensions"], 15)
        

            table.append([c1,c2,c3,c4,c5])

    print(tabulate(table, headers, tablefmt="grid"))

""""
def printReq3Table(lst):
    """
    #Imprime la tabla del Requerimiento 3
"""
    headers=['Title',"Date","Medium","Dimensions"]
    table=[]
    SizeOfList=lt.size(lst)
    for pos in range(SizeOfList):
        lista = lt.getElement(lst,pos)
        c1 = adjustlenght(lt.getElement(lista, 1), 18)
        c2 = adjustlenght(lt.getElement(lista, 2), 12)
        c3 = adjustlenght(lt.getElement(lista, 3), 18)
        c4 = adjustlenght(lt.getElement(lista, 4), 18)
            
        table.append([c1,c2,c3,c4])
    print(tabulate(table, headers, tablefmt="grid"))


def printReq4Table(lst):
    """
    #Imprime las tablas del Requerimiento 4
"""
    headers1 = ["Nationality", "ArtWorks"]
    headers2 = ['ObjectID','Title','ArtistsNames',"Date","Medium","Dimensions"]
    table1 = []
    table2 = []

    head = lt.firstElement(lst)
    num_head = stack.pop(head)
    artwork_count_head = stack.pop(head)
    artworks_head = stack.pop(head)
    country_head = stack.pop(head)
    table1.append([country_head, num_head])  

    #Tabla 1
    for pos in range(2,11):
        country_stack = lt.getElement(lst, pos)
        num = stack.pop(country_stack)
        artwork_count = stack.pop(country_stack)
        artworks_info = stack.pop(country_stack)
        country = stack.pop(country_stack)
        table1.append([country, num])

    #Tabla 2 (primeros elementos)
    for pos in range(1,4):
        artwork_info = lt.getElement(artworks_head, pos)
        c1 = adjustlenght(stack.pop(artwork_info), 8)
        c2 = adjustlenght(stack.pop(artwork_info), 20)
        c3 = adjustlenght(stack.pop(artwork_info), 15)
        c4 = stack.pop(artwork_info)
        c5 = adjustlenght(stack.pop(artwork_info), 25)
        c6 = adjustlenght(stack.pop(artwork_info), 15)
        
        table2.append([c1,c2,c3,c4,c5,c6])
     
    #Tabla 2 (últimos elementos)
    for x in range(2, -1,-1):
        pos = lt.size(lst) - x
        artwork_info = lt.getElement(artworks_head, pos)
        c1 = adjustlenght(stack.pop(artwork_info), 8)
        c2 = adjustlenght(stack.pop(artwork_info), 15)
        c3 = adjustlenght(stack.pop(artwork_info), 15)
        c4 = stack.pop(artwork_info)
        c5 = adjustlenght(stack.pop(artwork_info), 15)
        c6 = adjustlenght(stack.pop(artwork_info), 15)
        
        table2.append([c1,c2,c3,c4,c5,c6])

    print(tabulate(table1, headers1, tablefmt="grid"))

    print("\nLa nacionalidad con autores de más obras es: " + country_head + " con " + str(artwork_count_head) + " piezas únicas.")
    print("\nLas primeras y últimas 3 obras en la lista (ordenadas por fecha de adquisición) son:")
    print("(se recomienda ampliar la vista de la Terminal para observar mejor la tabla)")
    print(tabulate(table2, headers2, tablefmt="grid"))


def printReq5Table(most_expensive, oldest):
    """
    #Imprime las tablas del Requerimiento 5
"""
    headers = ['ObjectID','Title','ArtistsNames',"Medium","Date","Dimensions","Classification","TransCost (USD)"]
    table1 = []
    table2 = []

    for i in range(5):
        artwork1 = stack.pop(most_expensive)
        c11 = adjustlenght(lt.getElement(artwork1, 1),8)
        c12 = adjustlenght(lt.getElement(artwork1, 2),15)
        c13 = adjustlenght(lt.getElement(artwork1, 3),15)
        c14 = adjustlenght(lt.getElement(artwork1, 4),15)
        c15 = lt.getElement(artwork1, 5)
        c16 = adjustlenght(lt.getElement(artwork1, 6),15)
        c17 = adjustlenght(lt.getElement(artwork1, 7),10)
        c18 = lt.getElement(artwork1, 8)
        table1.append([c11,c12,c13,c14,c15,c16,c17,c18])

        artwork2 = stack.pop(oldest)
        c21 = adjustlenght(lt.getElement(artwork2, 1),8)
        c22 = adjustlenght(lt.getElement(artwork2, 2),15)
        c23 = adjustlenght(lt.getElement(artwork2, 3),15)
        c24 = adjustlenght(lt.getElement(artwork2, 4),15)
        c25 = lt.getElement(artwork2, 5)
        c26 = adjustlenght(lt.getElement(artwork2, 6),15)
        c27 = adjustlenght(lt.getElement(artwork2, 7),10)
        c28 = lt.getElement(artwork2, 8)
        table2.append([c21,c22,c23,c24,c25,c26,c27,c28])

    print("\n Las 5 obras más costosas de transportar son: ")
    print(tabulate(table1, headers, tablefmt="grid"))
    print("\n\n Las 5 obras más antiguas a transportar son: ")
    print(tabulate(table2, headers, tablefmt="grid"))


"""

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    

    if int(inputs) == 1:
        #file_size = input("Ingrese el sufijo del archivo que desea utilizar (small, large, 10pct...): ")
        file_size = "large"

        #Cargar archivos
        print("\nCargando información de los archivos ....")
        catalog = initCatalog()

        start_time = process_time()
        loadData(catalog, file_size)
        stop_time = process_time()
        running_time = (stop_time - start_time)*1000

        print("\nTiempo de carga: " + str(running_time) + " milisegundos")

        #print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        #print("\nÚltimos 3 artistas:")
        #printLast(catalog["artists"], 3)
        #print("\nÚltimas 3 obras:")
        #printLast(catalog["artworks"], 3)

    # Laboratorio 5

    elif int(inputs) == 100:
        Medium=input("Por favor ingrese el medio o tecnica de interes: ")
        MediumImportantREQLab5,SizeOfList=controller.REQLab5(catalog,Medium)
        print(Medium+" tiene "+str(SizeOfList)+" obras en total")
        print("Las 3 obras mas antiguas son las siguientes:")
        print(printFirst(MediumImportantREQLab5,3))

    # Laoratorio 6
    elif int(inputs) == 200:
        Nationality=input("Por favor ingrese la nacionalidad de interes: ")
        SizeOfArtworksOfNationality=controller.REQLab6(catalog,Nationality)
        print("Los "+Nationality+" tienen "+str(SizeOfArtworksOfNationality)+" obras")

    # Requerimiento 1

    elif int(inputs) == 10:
        a_initial = int(input("Ingrese el año inicial: "))
        a_final = int(input("Ingrese el año final: "))

        #Para pruebas de rendimiento
        #a_inicial = 0
        #a_final = 2022

        start_time = process_time()
        req1, count = controller.REQ1getArtistsRange(catalog, a_initial, a_final)
        stop_time = process_time()
        running_time = (stop_time - start_time)*1000

        print("\n\n=============== Requerimiento Número 1 ===============")
        print("Tiempo de ejecución: " + str(running_time) + " milisegundos")
        
        print("\nSe encontraron " + str(count) + " artistas nacidos en el rango dado")
        print("Los primeros y últimos 3 artistas nacidos en el rango fueron:  (se recomienda ampliar la vista de la Terminal para observar mejor la tabla)")
        print(printReq1Table(req1))
    
    

    
    elif int(inputs) == 20:
        a_initial = input("Ingrese la fecha de adquisición inicial en formato AAAA-MM-DD: ")
        a_final = input("Ingrese la fecha de adquisición final en formato AAAA-MM-DD: ")

        date_initial=datetime.strptime(a_initial, "%Y-%m-%d")
        date_final=datetime.strptime(a_final, "%Y-%m-%d")
        #Para pruebas de rendimiento
        #date_initial = "1900-01-01"
        #date_final = "2022-12-31"

        start_time = process_time()
        req2,artworks_count,purchase_count = controller.REQ2getArtworksRange(catalog, date_initial, date_final)
        stop_time = process_time()
        running_time = (stop_time - start_time)*1000
        
        print("\n\n=============== Requerimiento Número 2 ===============")
        print("Tiempo de ejecución: " + str(running_time) + " milisegundos")
    
        print("\nSe encontraron " + str(artworks_count) + " obras adquiridas entre " + a_initial + " y " + a_final + ".")
        print(str(purchase_count) + " fueron adquiridas por compra" + "\n")
        print("Las primeras y últimas 3 compras en el rango fueron:       (se recomienda ampliar la vista de la Terminal para observar mejor la tabla)")
        printReq2Table(req2)
    
    else:
        sys.exit(0)    
    """
    elif int(inputs) == 30:
        Name=input("Por favor ingrese el nombre del artista: ")
        
        start_time = process_time()
        NumberOfArtworks,TechniqueMoreUsed,NumberOfTechniques,ListOfArtists = controller.REQ3get_techniquees(catalog,Name)
        stop_time = process_time()
        running_time = (stop_time - start_time)*1000
        print("\n\n=============== Requerimiento Número 3 ===============")
        print("Tiempo de ejecución: " + str(running_time) + " milisegundos")
        
        print("\n"+Name+" tiene "+ str(NumberOfArtworks) +" obras en MoMA")
        print("Ademas, tiene "+str(NumberOfTechniques)+" medios o tecnicas en sus trabajos")
        print("La tecnica mas usada es: " +str(TechniqueMoreUsed))
        printReq3Table(ListOfArtists)


    elif int(inputs) == 40:
        start_time = process_time()
        req4_list = controller.REQ4getNationalityCount(catalog)
        stop_time = process_time()
        running_time = (stop_time - start_time)

        print("\n\n=============== Requerimiento Número 4 ===============")
        print("Tiempo de ejecución: " + str(running_time) + " segundos\n")
        print("El TOP 10 de nacionalidades con más obras es:")
        printReq4Table(req4_list)


    elif int(inputs) == 50:
        department = input("Digite el departamento a transportar: ")
        
        #Para pruebas
        #department = "Drawings & Prints"

        start_time = process_time()
        num_artworks,total_cost,total_weight,most_expensive,oldest = controller.REQ5moveArtworks(catalog, department)
        stop_time = process_time()
        running_time = (stop_time - start_time)*1000

        print("\n\n=============== Requerimiento Número 5 ===============")
        print("Tiempo de ejecución: " + str(running_time) + " milisegundos\n")

        print("\nNúmero de obras a transportar: " + str(num_artworks))
        print("Costo total calculado: " + str(total_cost))
        print("Peso total calculado: " + str(total_weight))
        printReq5Table(most_expensive, oldest)"""

sys.exit(0)
