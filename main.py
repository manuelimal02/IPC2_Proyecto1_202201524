import xml.etree.ElementTree as ET

import tkinter as tk
from tkinter import filedialog

from senal import senal
from lista_senal import lista_senal

from dato import dato
from lista_dato import lista_dato

from lista_patrones import lista_patrones
from lista_grupo import lista_grupo

ruta_archivo = ""

lista_senales_temporal=lista_senal()

def modificar_ruta(nueva_ruta):
    global ruta_archivo
    ruta_archivo = nueva_ruta

def menu_principal():
    print("--------------------------------------------------")
    print("MENÚ PRINCIPAL                                    ")
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
        escribir_archivo_salida()
    elif opcion == "4":
        mostrar_datos_estudiante()
    elif opcion == "5":
        generar_grafica()
    elif opcion == "6":
        inicializar_sistema()
    elif opcion == "7":
        salir()        
    else:
        print("--------------------------------------------------")
        print("Opción No Válida")
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
    print("Archivo cargado correctamente.")
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
        print("Opción No Válida")
        menu_principal()
    print("--------------------------------------------------")

def procesar_archivo():
    print("--------------------------------------------------")
    print("PROCESAR ARCHIVO")
    print("--------------------------------------------------")
    print("")
    if ruta_archivo=="":
        print("ERROR: Seleccione un archivo para procesar.")
    else:
        try:
            with open(ruta_archivo, "r") as archivo:
                tree = ET.parse(ruta_archivo)
                raiz=tree.getroot()
                for senal_temporal in raiz.findall('senal'):
                    nombre_senal=senal_temporal.get('nombre')
                    tiempo_senal=senal_temporal.get('t')
                    amplitud_senal=senal_temporal.get('A')
                    #Listas
                    lista_datos_temporal=lista_dato()
                    lista_binaria_temporal=lista_dato()
                    lista_patrones_temporal=lista_patrones()
                    lista_grupos_temporal=lista_grupo()
                    for dato_senal in senal_temporal.findall('dato'):
                        tiempo=dato_senal.get('t')
                        amplitud=dato_senal.get('A')
                        valor=dato_senal.text
                        nuevo_dato=dato(int(tiempo),int(amplitud),int(valor))
                        lista_datos_temporal.insertar_dato(nuevo_dato)
                        if valor =="0":
                            nuevo_dato=dato(int(tiempo),int(amplitud),0)
                            lista_binaria_temporal.insertar_dato(nuevo_dato)
                        else:
                            nuevo_dato=dato(int(tiempo),int(amplitud),1)
                            lista_binaria_temporal.insertar_dato(nuevo_dato)
                    lista_senales_temporal.insertar_senal(senal(nombre_senal,tiempo_senal,amplitud_senal,
                                                                 lista_datos_temporal,
                                                                 lista_binaria_temporal,
                                                                 lista_patrones_temporal,
                                                                 lista_grupos_temporal)) 
                lista_senales_temporal.procesar_archivo()
        except Exception as e:
            print("ERROR:", e)
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
        print("Opción No Válida")
        menu_principal()
    print("--------------------------------------------------")

def escribir_archivo_salida():
    print("--------------------------------------------------")
    print("ESCRIBIR ARCHIVO SALIDA")
    print("--------------------------------------------------")
    nombre_xml=input("Ingrese un nombre para guardar el archivo XML: ")
    print("")
    lista_senales_temporal.escribir_archivo_salida(nombre_xml)
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
        print("Opción No Válida")
        menu_principal()
    print("--------------------------------------------------")

def mostrar_datos_estudiante():
    print("--------------------------------------------------")
    print("Carlos Manuel Lima y Lima                         ")
    print("202201524                                         ")
    print("Introducción a la Programación y Computación 2    ")
    print("Ingeniería en Ciencias y Sistemas                 ")
    print("Cuarto Semestre, 2023                            ")
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
        print("Opción No Válida")
        menu_principal()
    print("--------------------------------------------------")

def generar_grafica():
    print("--------------------------------------------------")
    print("GENERAR GRÁFICA")
    print("--------------------------------------------------")
    nombre_senal=input("Ingrese nombre de la señal: ")
    print("")
    lista_senales_temporal.grafica_matrices(nombre_senal)
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
        print("Opción No Válida")
        menu_principal()
    print("--------------------------------------------------")

def inicializar_sistema():
    print("--------------------------------------------------")
    print("INICIALIZAR SISTEMA")
    print("--------------------------------------------------")
    lista_senales_temporal.inicializar_sistema()
    print("")
    lista_senales_temporal.imprimir_senales()
    modificar_ruta("")
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
        print("Opción No Válida")
        menu_principal()
    print("--------------------------------------------------")

def salir():
    print("Gracias por utilizar el programa.                 ")
    print("--------------------------------------------------")

if __name__=="__main__":
    print("--------------------------------------------------")
    print("Proyecto 1 – Compresión De Señales                ")
    menu_principal()  