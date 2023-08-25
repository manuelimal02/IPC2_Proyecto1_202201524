import xml.etree.ElementTree as ET

import tkinter as tk
from tkinter import filedialog

from senal import senal
from lista_senal import lista_senal

from dato import dato
from lista_dato import lista_dato

from lista_patrones import lista_patrones
from lista_grupo import lista_grupo

ruta_archivo = "D:/USAC/4 Cuarto Semestre/Introducción A La Programación Y Computación 2 Laboratorio/PROYECTO 1/prueba1.xml"

manejador_lista_senales=lista_senal()
manejador_lista_datos=lista_dato()
manejador_lista_binaria=lista_dato()

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
        print("OPCION ESCRIBIR XML")
    elif opcion == "4":
        mostrar_datos_estudiante()
    elif opcion == "5":
        generar_grafica()
    elif opcion == "6":
        print("OPCION INICIALIZAR SISTEMA")
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
        print("Opción No Válida")
        menu_principal()
    print("--------------------------------------------------")

def procesar_archivo():
    print("--------------------------------------------------")
    print("PROCESAR ARCHIVO")
    print("--------------------------------------------------")
    print("")
    #try:
    with open(ruta_archivo, "r") as archivo:
            # Parsear el XML
            tree = ET.parse(ruta_archivo)
            raiz=tree.getroot()
            # Recorrer el XML
            for senal_temporal in raiz.findall('senal'):
                nombre_senal=senal_temporal.get('nombre')
                tiempo_senal=senal_temporal.get('t')
                amplitud_senal=senal_temporal.get('A')
                #Lista Patron y Grupos
                manejador_lista_patrones=lista_patrones()
                manejador_lista_grupos=lista_grupo()
                for dato_senal in senal_temporal.findall('dato'):
                    tiempo=dato_senal.get('t')
                    amplitud=dato_senal.get('A')
                    valor=dato_senal.text
                    nuevo_dato=dato(int(tiempo),int(amplitud),int(valor))
                    manejador_lista_datos.insertar_dato(nuevo_dato)
                    if valor =="0":
                        nuevo_dato=dato(int(tiempo),int(amplitud),0)
                        manejador_lista_binaria.insertar_dato(nuevo_dato)
                    else:
                        nuevo_dato=dato(int(tiempo),int(amplitud),1)
                        manejador_lista_binaria.insertar_dato(nuevo_dato)
                    manejador_lista_senales.insertar_senal(senal(nombre_senal,tiempo_senal,amplitud_senal,manejador_lista_datos,manejador_lista_binaria,manejador_lista_patrones,manejador_lista_grupos))
               
    manejador_lista_senales.calcular_los_patrones("Prueba 1")         
    #except Exception as e:
        #print("ERROR:", e)
    
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
    #manejador_lista_senales.grafica_matriz_original(nombre_senal)
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

def sumar_subcadenas(input_str):
        subcadenas = []
        subcadena = ""
        for char in input_str:
            if char == "%":
                subcadenas.append(subcadena)
                subcadena = ""
            else:
                subcadena += char
        
        # Encontrar la longitud mínima entre las subcadenas
        min_len = min(len(subcadenas[0]), len(subcadenas[1]))
        
        # Inicializar una lista para almacenar las sumas
        sumas = []
        current_sum = 0
        
        # Iterar a través de los caracteres y calcular las sumas
        for i in range(min_len):
            char1 = subcadenas[0][i]
            char2 = subcadenas[1][i]
            
            if char1.isdigit() and char2.isdigit():
                current_sum = current_sum + int(char1) + int(char2)
                sumas.append(str(current_sum))
        
        # Crear un nuevo string separado por guiones con las sumas calculadas
        resultado = "-".join(sumas)
        return resultado

if __name__=="__main__":
    print("--------------------------------------------------")
    print("Proyecto 1 – Compresión De Señales                ")
    menu_principal()  