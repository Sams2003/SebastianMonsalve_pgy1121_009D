import os
import time
import msvcrt
import numpy

lista_rut=[]
lista_fila=[]
lista_columna=[]
lista_cantidad=[]
lista_platinum=[]
lista_gold=[]
lista_silver=[]

platinum = 120000
gold = 80000
silver = 50000

escenario = numpy.zeros((10,10),int)

def ver_menu():
    print("""Menú
    1) Comprar entrada
    2) Ver escenario
    3) Ver asistente
    4) Mostrar ganancia totales
    5) salir""")

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion in (1,2,3,4,5):
                return opcion
            else:
                print("ERROR! OPCIÓN INVALIDA")
        except:
            print("ERROR! DEBE INGRESAR NÚMEROS ENTEROS")

def ver_escenario():
    print("Escenario")
    for x in range(10):
        print(f"\tFila {x+1}\n", end="  ")
        print()
        for y in range(10):
            print(f"\tColumna {y+1}\n", end="  ")
            print()

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut(sin puntos ni digito verificador): "))
            if rut >= 10000000 and rut <= 99999999:
                return rut
            else:
                print("Rut invalido")
        except:
            print("ERROR! DEBE INGRESAR NÚMEROS ENTEROS")

def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese su fila: "))
            if fila >= 1 and fila <= 10:
                return fila
            else:
                print("Fila invalida")
        except:
            print("ERROR! DEBE INGRESAR NÚMEROS ENTEROS")

def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese su columna: "))
            if columna >= 1 and columna <= 10:
                return columna
            else:
                print("Columna invalida")
        except:
            print("ERROR! DEBE INGRESAR NÚMEROS ENTEROS")

def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de personas: "))
            if cantidad >= 1 and cantidad <= 3:
                return cantidad
            else:
                print("Cantidad no valida o se excede a la cantidad máxima")
        except:
            print("ERROR! DEBE INGRESAR NÚMEROS ENTEROS")

def comprar():
    os.system('cls')
    contador= 1
    print("Compra")
    if 0 not in escenario:
        print("escenario lleno")
    
    cantidad = validar_cantidad()
    for cantidad in range(cantidad):
        ver_escenario()
        fila = validar_fila()
        columna = validar_columna()
        rut = validar_rut()

    if escenario [fila+1][columna+1] != 0:
            print("Asiento ocupado")    
    if fila >=1 and fila <= 20:
        lista_rut.append(rut)
        lista_cantidad.append(cantidad)
        lista_fila.append(fila)
        lista_columna.append(columna)
        lista_platinum.append(contador)
        contador += 1
    elif fila >= 21 and fila <= 50:
        lista_rut.append(rut)
        lista_cantidad.append(cantidad)
        lista_fila.append(fila)
        lista_columna.append(columna)
        lista_gold.append(contador)
        contador += 1
    else:
        lista_rut.append(rut)
        lista_cantidad.append(cantidad)
        lista_fila.append(fila)
        lista_columna.append(columna)
        lista_silver.append(contador)
        contador += 1
    time.sleep(3)

def ver_asistente():
    print("Ver asistentes")
    print("La cantidad de asistentes es: ", lista_rut)
    
    

def ver_ganancia():
    total_platinum = len(lista_platinum) * platinum
    total_gold = len(lista_gold) * gold
    total_silver = len(lista_silver) * silver
    contador = total_gold + total_platinum + total_silver
    total = total_platinum + total_gold + total_silver
    print("tipo de entrada=======cantidad=======total")
    print(f"Platinum={platinum}-------{len(lista_platinum)}--------{total_platinum}")
    print("****************************************")
    print(f"gold={gold}-------------{len(lista_gold)}----------{total_gold}")
    print("****************************************")
    print(f"silver={silver}----------{len(lista_silver)}--------{total_silver}")
    print("****************************************")
    print(f"total--------------------{contador}-------------{total}")
    time.sleep(3)

def salir():
    print("Gracias por preferirnos")
    print("Sebastian Monsalve 06-07-2023")