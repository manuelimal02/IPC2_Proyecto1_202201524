import sys
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from nodo_grupo import nodo_grupo

def dividir_cadena_sumada(cadena, delimitador):
    numeros = [] 
    numero_actual = ""
    for char in cadena:
        if char == delimitador:
            if numero_actual:
                numeros.append(int(numero_actual))
                numero_actual = ""
        else:
            numero_actual += char
    if numero_actual:
        numeros.append(int(numero_actual))
    return numeros

class lista_grupo:
    def __init__(self):
        self.primero = None
        self.contador_grupos=0

    def insertar_grupo(self,grupo):
        if self.primero is None:
            self.primero = nodo_grupo(grupo=grupo)
            self.contador_grupos+=1
            return
        actual= self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_grupo(grupo=grupo)
        self.contador_grupos+=1

    def grafica_matriz_reducida(self, nombre_senal):
        actual = self.primero
        f = open('aa.dot','w')
        text ="""
            digraph G {
            subgraph cluster17
                    {
                    n019 ;
                    n019 [label="Nombre Senal Reducida: """+actual.grupo.nombre_senal+""""] ;
                    n019 -> n020 ;
                    n020 [label="Amplitud: """+actual.grupo.amplitud+""""] ;
                    }
            label="Matriz de Onda Reducida"
            fontname="Helvetica,Arial,sans-serif"
            node [fontname="Helvetica,Arial,sans-serif"]
            edge [fontname="Helvetica,Arial,sans-serif"]
            a0 [shape=none  label=<
            <TABLE border="0" cellspacing="10" cellpadding="10" >\n"""
        while actual:
            if actual.grupo.nombre_senal == nombre_senal:
                text+="""<TR>""" 
                cadena_digitos=dividir_cadena_sumada(actual.grupo.cadena_grupo_sumado,"-")
                text+="""<TD bgcolor="brown:purple"  gradientangle="315">"""+str(actual.grupo.nombre_grupo)+"""</TD>\n"""
                for i in cadena_digitos:
                    text+="""<TD bgcolor="red:blue"  gradientangle="315">"""+str(i)+"""</TD>\n"""
                text+="""</TR>\n"""
            actual = actual.siguiente
        text+="""</TABLE>>];
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng aa.dot -o grafica_matriz_reducida.png')

    def imprimir_lista_grupo(self):
        print("-----------------------------------")
        actual = self.primero
        while actual != None:
            print("Nombre Senal: ",actual.grupo.nombre_senal,"Amplitud: ",actual.grupo.amplitud,"Grupo: ",actual.grupo.nombre_grupo,"Suma: ",actual.grupo.cadena_grupo_sumado)
            actual = actual.siguiente
        print("-----------------------------------")
