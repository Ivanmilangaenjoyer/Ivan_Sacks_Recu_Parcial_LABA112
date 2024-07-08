# Iván Sacks Labo A112
# Se deberá realizar un programa que permita el análisis de dicho archivo.
# El programa contará con el siguiente menú:
# 1) Cargar archivo CSV: Se pedirá el nombre del archivo y se cargará en una lista de diccionarios
# los elementos del mismo.
# 2) Imprimir lista: Se imprimirá por pantalla la tabla con los datos de las bicicletas.
# 3) Asignar tiempos: Se deberá mapear la lista con una función que asignará a cada bicicleta un
# valor de tiempo entre 50 y 120 minutos calculado de manera aleatoria y se mostrará por pantalla la
# lista.
# 4) Informar ganador: Informar el nombre del dueño de la bicicleta que llego primero y el tiempo
# que tardo. Si hubiera empate. informar todos los nombres de las bicicletas que empataron.
# 5) Filtrar por tipo: Se deberá pedir un tipo de bicicleta al usuario y escribir un archivo igual al
# original, pero donde solo aparezcan bicicletas del tipo seleccionado. El nombre del archivo será por
# ejemplo playeras.csv
# 6) Informar promedio por tipo: Listar el promedio de tiempo por cada tipo de bicicleta.
# 7) Mostrar posiciones: Se deberá mostrar por pantalla un listado de las bicicletas ordenadas
# por tipo y dentro de las del mismo tipo que aparezcan ordenadas por tiempo ascendente.
# 8) Guardar posiciones:Se deberá guardar el listado del punto anterior en un archivo JSON.
#9 SALIR
import os
from modulo_funciones import *

path_0 = os.getcwd()
path = os.path.join(path_0, "bicicletas.csv")



programa = True
menu_opciones = ("Que desea hacer?\n"
                "1: Cargar CSV\n"
                "2: Imprimir lista\n"
                "3: Asignar tiempo\n"
                "4: Informar ganador\n"
                "5: Filtrar por tipo de bici\n"
                "6: Informar promedio por tipo\n"
                "7: Ordenar posiciones\n"
                "8: Guardar bicis\n"
                "9: Salir\n")
while programa:
    
    opcion = input(menu_opciones)
    try:
        opcion = int(opcion)
    except:
        raise ValueError("Por favor, ingrese numeros solamente")
    
    while opcion < 1 or opcion > 9:
        opcion = input(f"Por favor ingrese numeros validos {menu_opciones}")

    match opcion:
        case 1:
            #1
            bicicletas = cargar_csv(path)
        case 2:
            #2
            mostrar_bicicletas(bicicletas)
        case 3:
            mapear_bicicleta(bicicletas, asignar_tiempo)
        case 4: 
            #4
            nombre_ganador, tiempo_ganador = tiempo_min(bicicletas)
            mostrar_bicicletas(bicicletas)
            print(f"La persona que llego en el menor es: {nombre_ganador} en: {tiempo_ganador} min")
        case 5:
            #5
            tipo = input("Ingrese el tipo de bici que quieres filtrar: BMX, PLAYERA, MTB, PASEO ")

            while tipo != "BMX" and tipo != "PLAYERA" and tipo != "MTB" and tipo != "PASEO":
                tipo = input("Reingrese el tipo de bici que quieres filtrar: BMX, PLAYERA, MTB, PASEO ")

            filtrar_bicis(bicicletas, tipo, path_0)
        case 6:
            tiempos_tipo, bicis = promedio_tipo_bicis(bicicletas)
            for tipo in bicis:
                print(f"El promedio de tiempo de {tipo} es de: {tiempos_tipo[tipo]}\n")

        case 7:
            ordenar_tipo_tiempo_asc(bicicletas)

        case 8:
            guardar_bicis_json(bicicletas, path_0)

        case 9:
            programa = False