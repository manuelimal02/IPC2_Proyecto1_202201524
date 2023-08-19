import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename

from senal import senal
from lista_senal import lista_senal

from dato import dato
from lista_dato import lista_dato



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
        print("prueba")
        cargar_archivo()
    elif  opcion == "2":
        salir()
    elif opcion == "3":
        mostrar_datos_estudiante()
    elif opcion == "4":
        mostrar_datos_estudiante()
    else:
        print("--------------------------------------------------")
        print("OPCIÓN NO VÁLIDA")
        menu_principal()

def cargar_archivo():
    print("--------------------------------------------------")
    ruta_archivo=askopenfilename()
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

