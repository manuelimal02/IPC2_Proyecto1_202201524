from lista import lista_simple
from nodo_senal import nodo_senal
from grupo import grupo
import xml.etree.ElementTree as ET

def dividir_cadena(cadena, separar):
    lista_numero = lista_simple()
    numero_actual = ""
    for char in cadena:
        if char == separar:
            if numero_actual:
                lista_numero.agregar(numero_actual)
                numero_actual = ""
        else:
            numero_actual += char
    if numero_actual:
        lista_numero.agregar(numero_actual)
    return lista_numero

def procesar_cadena(cadena):
    subcadenas = dividir_cadena(cadena, "!")
    nodo_actual_subcadena = subcadenas.inicio
    suma_total = None
    while nodo_actual_subcadena:
        valores = dividir_cadena(nodo_actual_subcadena.dato, "-")
        nodo_actual_valor = valores.inicio
        if suma_total is None:
            suma_total = lista_simple()
            while nodo_actual_valor:
                suma_total.agregar(nodo_actual_valor.dato)
                nodo_actual_valor = nodo_actual_valor.siguiente
        else:
            nodo_suma = suma_total.inicio
            while nodo_actual_valor:
                if nodo_suma:
                    nodo_suma.dato = str(int(nodo_suma.dato) + int(nodo_actual_valor.dato))
                    nodo_suma = nodo_suma.siguiente
                    nodo_actual_valor = nodo_actual_valor.siguiente
        nodo_actual_subcadena = nodo_actual_subcadena.siguiente
    resultado = ""
    nodo_resultado = suma_total.inicio
    while nodo_resultado:
        resultado += nodo_resultado.dato
        if nodo_resultado.siguiente:
            resultado += "-"
        nodo_resultado = nodo_resultado.siguiente
    return resultado


class lista_senal:
    def __init__(self):
        self.primero=None
        self.contador_senal=0
        
    def insertar_senal(self, senal):
        if self.primero is None:
            self.primero=nodo_senal(senal=senal)
            self.contador_senal+=1
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodo_senal(senal=senal)
        self.contador_senal+=1

    def imprimir_senales(self):
        print("Total de Señales:",self.contador_senal)
        actual=self.primero
        while actual !=None:
            print("Nombre:",actual.senal.nombre)
            actual=actual.siguiente

    def grafica_matrices(self,nombre):
        actual=self.primero
        if actual is not None:
            nombre_encontrado=False
            while actual != None:
                if actual.senal.nombre==nombre:
                    nombre_encontrado=True
                    break
                else:
                    actual=actual.siguiente
            if nombre_encontrado:
                print("Gráfica matriz original de la señal "+nombre+" generada correctamente.")
                actual.senal.lista_dato.grafica_matriz_original(actual.senal.nombre,str(actual.senal.tiempo),str(actual.senal.amplitud))
                print("Gráfica matriz reducida de la señal "+nombre+" generada correctamente.")
                actual.senal.lista_grupo.grafica_matriz_reducida(nombre)
            else:
                print("No existe una señal con el nombre: "+nombre)
        else:
            print("ERROR: No existen señales procesadas.")

    def procesar_archivo(self):
        actual=self.primero
        while actual !=None:
            nombre_senal=actual.senal.nombre
            amplitud_senal=actual.senal.amplitud
            print("Procesando la Señal: "+actual.senal.nombre)
            print("Calculando la matriz binaria...")
            actual.senal.lista_patron=actual.senal.lista_binaria.patrones_por_tiempo(actual.senal.lista_patron)
            lista_patrones_temporal=actual.senal.lista_patron
            grupos_sin_analizar=lista_patrones_temporal.encontrar_coincidencias()
            buffer=""
            for digito in grupos_sin_analizar:
                if digito.isdigit() or digito=="/":
                    buffer+=digito
                elif digito =="-" and buffer!="":
                    cadena_grupo=actual.senal.lista_dato.cadena_del_grupo(buffer)
                    cadena_grupo_sumado=procesar_cadena(cadena_grupo)
                    actual.senal.lista_grupo.insertar_grupo(grupo=grupo(nombre_senal,amplitud_senal,buffer,cadena_grupo,cadena_grupo_sumado))
                    buffer=""
                else:
                    buffer=""
            print("Realizando suma de duplas...")
            print("")
            actual=actual.siguiente
        print("Archivo procesado correctamente.")

    def escribir_archivo_salida(self,nombre_xml):
        actual=self.primero
        if actual is not None:
            senales=ET.Element("senalesReducidas")
            while actual!=None:
                senal=ET.SubElement(senales,"senal")
                senal.set("nombre",actual.senal.nombre)
                senal.set("A",actual.senal.amplitud)
                lista_grupo_temporal=actual.senal.lista_grupo.primero
                contador_grupo=1
                while  lista_grupo_temporal!=None:
                    grupo=ET.SubElement(senal,"grupo")
                    grupo.set("g",str(contador_grupo))
                    contador_grupo+=1
                    tiempos=ET.SubElement(grupo,"tiempos")
                    tiempos.text= lista_grupo_temporal.grupo.nombre_grupo
                    datos_grupo=ET.SubElement(grupo,"datosGrupo")
                    lista_numero=dividir_cadena(lista_grupo_temporal.grupo.cadena_grupo_sumado,"-")
                    actual_nodo=lista_numero.inicio
                    contador_amplitud=1
                    while actual_nodo:
                        dato=ET.SubElement(datos_grupo,"dato")
                        dato.set("A",str(contador_amplitud))
                        dato.text=actual_nodo.dato
                        contador_amplitud+=1
                        actual_nodo=actual_nodo.siguiente   
                    lista_grupo_temporal=lista_grupo_temporal.siguiente
                    contador_amplitud=1
                actual=actual.siguiente
                contador_grupo=1
            datos=ET.tostring(senales)
            datos=str(datos)
            self.xml_identado(senales)
            arbol_xml=ET.ElementTree(senales)
            arbol_xml.write(nombre_xml+".xml",encoding="UTF-8",xml_declaration=True)
            print("Archivo XML generado correctamente.")
        else:
            print("ERROR: No existen señales procesadas.")

    def xml_identado(self, element, indent='  '):
        queue = [(0, element)]
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level + 1)
            if queue:
                element.tail = '\n' + indent * queue[0][0]
            else:
                element.tail = '\n' + indent * (level - 1)
            queue[0:0] = children

    def inicializar_sistema(self):
        self.primero = None
        self.contador_senal = 0
        print("Sistema inicializado correctamente.")
