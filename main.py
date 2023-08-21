import xml.etree.ElementTree as ET

import tkinter as tk
from tkinter import filedialog

from senal import senal
from lista_senal import lista_senal

from dato import dato
from lista_dato import lista_dato

ruta_archivo = "D:/USAC/4 Cuarto Semestre/Introducción A La Programación Y Computación 2 Laboratorio/PROYECTO 1/prueba1.xml"
def modificar_ruta(nueva_ruta):
    global ruta_archivo
    ruta_archivo = nueva_ruta

def menu_principal():
    print("--------------------------------------------------")
    print("Menú Principal                                    ")
    print("--------------------------------------------------")
    print("1. Cargar Archivo                                 ")
    print("2. Procesar Archivo                               ")
    print("3. Escribir Archivo de Salida                     ")
    print("4. Mostrar Datos del Estudiante                   ")
    print("5. Generar Gráfica                                ")
    print("6. Inicializar Sistema                            ")
    print("7. Salida                                         ")
    print("--------------------------------------------------")
    opcion = input("Ingrese Una Opción: ")
    if opcion == "1":
        cargar_archivo()
    elif  opcion == "2":
        procesar_archivo()
    elif opcion == "3":
        print(ruta_archivo)
    elif opcion == "4":
        mostrar_datos_estudiante()
    else:
        print("--------------------------------------------------")
        print("OPCIÓN NO VÁLIDA")
        menu_principal()

def cargar_archivo():
    print("--------------------------------------------------")
    print("CARGAR ARCHIVO")
    print("--------------------------------------------------")
    print("Selecciona el archivo xml a cargar:")
    print("")
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    ruta_seleccionada = filedialog.askopenfilename()
    if ruta_seleccionada:
        ruta_archivo = ruta_seleccionada
        modificar_ruta(ruta_archivo)
    print("Archivo cargado correctamente: ",ruta_archivo )
    print("--------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("2. No")
    print("--------------------------------------")
    opcion = input("Ingrese Una Opción: ")
    if opcion=="1":
        menu_principal()
    elif opcion=="2":
        salir()  
    else:
        print("--------------------------------------------------")
        print("OPCIÓN NO VALIDA")
        menu_principal()
    print("--------------------------------------------------")

def procesar_archivo():
    print("--------------------------------------------------")
    print("PROCESAR ARCHIVO")
    print("--------------------------------------------------")
    print(ruta_archivo)
    archivo= open(ruta_archivo,"r")
    archivo.close()

    tree = ET.parse(ruta_archivo)
    raiz=tree.getroot()
    

    lista_senales_temporal=lista_senal()
    lista_dato_temporal=lista_dato()
    lista_dato_patrones_temporal=lista_dato()

    for senal_temporal in raiz.findall('senal'):
        nombre_senal=senal_temporal.get('nombre')
        tiempo_senal=senal_temporal.get('t')
        amplitud_senal=senal_temporal.get('A')

        for dato_senal in senal_temporal.findall('dato'):
            tiempo=dato_senal.get('t')
            amplitud=dato_senal.get('A')
            valor=dato_senal.text
            nuevo_dato=dato(int(tiempo),int(amplitud),int(valor))
            lista_dato_temporal.insertar_dato(nuevo_dato)

            if valor =="0":
                nuevo_dato=dato(int(tiempo),int(amplitud),0)
                lista_dato_patrones_temporal.insertar_dato(nuevo_dato)
            else:
                nuevo_dato=dato(int(tiempo),int(amplitud),1)
                lista_dato_patrones_temporal.insertar_dato(nuevo_dato)
        lista_senales_temporal.insertar_senal(senal(nombre_senal,tiempo_senal,amplitud_senal, lista_dato_temporal,lista_dato_patrones_temporal))

    #lista_senales_temporal.imprimir_matriz(lista_dato_temporal)
    lista_senales_temporal.imprimir_matriz(lista_dato_temporal)

    print("--------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("2. No")
    print("--------------------------------------")
    opcion = input("Ingrese Una Opción: ")
    if opcion=="1":
        menu_principal()
    elif opcion=="2":
        salir()  
    else:
        print("--------------------------------------------------")
        print("OPCIÓN NO VALIDA")
        menu_principal()
    print("--------------------------------------------------")

def mostrar_datos_estudiante():
    print("--------------------------------------------------")
    print("Carlos Manuel Lima y Lima                         ")
    print("202201524                                         ")
    print("Introducción a la Programación y Computación 2    ")
    print("Ingeniería en Ciencias y Sistemas                 ")
    print("ICuarto Semestre, 2023                            ")
    print("--------------------------------------------------")
    print("--------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("2. No")
    print("--------------------------------------")
    opcion = input("Ingrese Una Opción: ")
    if opcion=="1":
        
        menu_principal()
    elif opcion=="2":
        salir()  
    else:
        print("--------------------------------------------------")
        print("OPCIÓN NO VALIDA")
        menu_principal()

def salir():
    print("--------------------------------------------------")
    print("Gracias por utilizar el programa.                 ")
    print("--------------------------------------------------")

if __name__=="__main__":
    print("--------------------------------------------------")
    print("Proyecto 1 – Compresión De Señales                ")
    menu_principal()  