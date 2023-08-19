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
        salir()
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

def salir():
    print("--------------------------------------------------")
    print("Gracias por utilizar el programa.                 ")
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


if __name__=="__main__":
    print("--------------------------------------------------")
    print("Proyecto 1 – Compresión De Señales                ")
    menu_principal()  