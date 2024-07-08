import random
import sys, os
import json
def cargar_csv(path: str) -> list:
    """Recibe una dirección de memoria, carga el csv en una lista 
    de diccionarios y devuelve esa lista


    Args:
        path (str): Dirección de memoria

    Returns:
        Lista(list): Una lista de diccionarios
    """
    with open(path, "r", encoding = "utf-8") as archivo:
        lista = []
        encabezado = archivo.readline().strip("\n").split(",")
        for linea in archivo.readlines():
            bicicletas = {}
            linea = linea.strip("\n").split(",")
            id_bike_bike, nombre, tipo, tiempo = linea 
            
            bicicletas["id_bike"] = int(id_bike_bike)
            bicicletas["nombre"] = nombre
            bicicletas["tipo"] = tipo
            bicicletas["tiempo"] = int(tiempo)
            lista.append(bicicletas)

        return lista
    

def mostrar_bicicletas(bicicletas: list):
    """Recibe una lista de diccionarios y la muestra en pantalla. No devuelve nada

    Args:
        bicicletas (list): Las bicicletas a mostrar
    """
    print("ID_BIKE     NOMBRE      TIPO         TIEMPO")
    for i in range(len(bicicletas)):
        print(f" {bicicletas[i]["id_bike"]:3}      {bicicletas[i]["nombre"]:<10}     {bicicletas[i]["tipo"]:<8}      {bicicletas[i]["tiempo"]:2}")

def mapear_bicicleta(lista: list, funcion):
    """Recibe una lista de diccionarios y una funcion.
    Mapea la lista y no devuelve nada

    Args:
        lista (list): La lista a mapear
        funcion (funct): La funcion que mapea la lista
    """
    for i in range(len(lista)):
        funcion(lista, i)

def asignar_tiempo(lista: list, bicicleta: int):
    """Recibe una bicicleta y le asigna un numero del 1 al 10 y un decimal

    Args:
        lista (list): La lista a asignar
        bicicleta (int): La bicicleta del valor que se va a cambiar
    """
    lista[bicicleta]["tiempo"] = random.randint(50, 120)


def tiempo_min(lista: list):
    """Recibe una lista, calcula cual es la persona  con el 
    tiempo más corto, devuelve el nombre y tiempo de esta

    Args:
        lista (list): La lista a comparar

    Returns:
        str: El nombre del ganador
        int: El tiempo de este
    """
    nombre_ganador = "Ninguno"
    tiempo_ganador = 150
    bandera = True
    for i in range(len(lista)):
        if lista[i]["tiempo"] < tiempo_ganador or bandera:
            bandera = False
            nombre_ganador = lista[i]["nombre"]
            tiempo_ganador = lista[i]["tiempo"]

    return nombre_ganador, tiempo_ganador

def filtrar_bicis(lista:list, tipo_bici: str, path: str):
    """Recibe una lista, un tipo de bicicleta y una dirrecion de memoria, 
    crea un archivo csv(si no existe lo crea) y guarda las bicis del tipo correspondiente

    Args:
        lista (list): La lista a escribir
        bicicleta (str): EL bicicleta a filtrar
        path (str): La dirrecion de memoria donde crear el archivo
    """
    with open(os.path.join(path, "playeras.csv"), "a", encoding = "utf-8") as archivo:
        if os.stat(os.path.join(path, "playeras.csv")).st_size == 0:
            archivo.write("id_bike,nombre,tipo,tiempo\n")
        for i in range(len(lista)):
            print(f"{lista[i]["tipo"]}, {tipo_bici}")
            if lista[i]["tipo"] == tipo_bici:
                id_bike = f"{lista[i]["id_bike"]},"
                nombre = f"{lista[i]["nombre"]},"
                tipo = f"{lista[i]["tipo"]}," 
                tiempo = f"{lista[i]["tiempo"]}\n"

                archivo.write(id_bike)
                archivo.write(tipo)
                archivo.write(nombre)
                archivo.write(tiempo)


def promedio_tipo_bicis(lista: list):
    """Recibe una lista, crea un diccionario
    con cada tipo de tipo y suma,
    devuelve el diccionario

    Args:
        lista (list): La lista de diccionarios

    Returns:
        dict: El diccionario con los resultados
    """
    tipos_bicis = {}
    tiempos_bicis = {}
    bicis = []
    lista_promedios_bicis = {}

    for vuelta in range(len(lista)):
        bicis.append(lista[vuelta]["tipo"])

    bicis = set(bicis)

    for tipo in bicis:
        tipos_bicis[tipo] = 0
        tiempos_bicis[tipo] = 0
        lista_promedios_bicis[tipo] = 0

    for vuelta in range(len(lista)):
        for tipo in bicis:
            if lista[vuelta]["tipo"] == tipo:
                tipos_bicis[tipo] += 1
                tiempos_bicis[tipo] += lista[vuelta]["tiempo"]


    for tipo in bicis:
        lista_promedios_bicis[tipo] = tiempos_bicis[tipo] / tipos_bicis[tipo]
    

    return lista_promedios_bicis, bicis

def cambiar_bicis(lista, i, j):
    """Recibe una lista y dos bicis,
    las cambia de lugar, 
    no devuelve nada

    Args:
        lista (_type_): La lista con las bicis
        i (int): Primer bici
        j (int): Segunda bici
    """
    for clave, valor in lista[i].items():
        aux = lista[i][clave]
        lista[i][clave] = lista[j][clave]
        lista[j][clave] = aux


def ordenar_tipo_tiempo_asc(lista: list):
    """Recibe una lista,
    ordena la lista por genero dentro de este por rating descendiente
    no devuelve nada

    Args:
        lista (list): La lista a ordenar
    """
    for i in range(len(lista) -1):
        for j in range(i + 1, len(lista)):
            if lista[i]["tipo"] == lista[j]["tipo"]:
                if lista[i]["tiempo"] > lista[j]["tiempo"]:
                    cambiar_bicis(lista, i, j)
            elif lista[i]["tipo"] > lista[j]["tipo"]:
                cambiar_bicis(lista, i, j)


def guardar_bicis_json(lista: list, path: str):
    with open(f"{path}/bicis.ordenadas.json", "w", encoding = "utf-8") as archivo:
        json.dump(lista, archivo, ensure_ascii = False, indent = 4)