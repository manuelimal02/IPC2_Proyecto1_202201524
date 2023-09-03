import sys
import os
import xml.etree.ElementTree as ET
from nodo_grupo import nodo_grupo
from lista import lista_simple

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
        f = open('g_reducida.dot','w')
        text ="""
            digraph G {
            label="Matriz Reducida"
            subgraph cluster1 {bgcolor="purple:pink" label="Matriz Reducida" fontcolor="white"
                fillcolor="blue:cyan" label="Senal: """+actual.grupo.nombre_senal+"""" fontcolor="white" style="filled" gradientangle="270"
                node [shape=box fillcolor="red:yellow" style="filled" gradientangle=90]
                "Amplitud: """+actual.grupo.amplitud+"""";
                }
            fontname="Helvetica,Arial,sans-serif"
            node [fontname="Helvetica,Arial,sans-serif"]
            edge [fontname="Helvetica,Arial,sans-serif"]
            a0 [shape=none  label=<
            <TABLE border="0" cellspacing="10" cellpadding="10" >\n"""
        while actual:
            if actual.grupo.nombre_senal == nombre_senal:
                text+="""<TR>"""
                lista_numero=dividir_cadena(actual.grupo.cadena_grupo_sumado,"-")
                actual_nodo=lista_numero.inicio
                text+="""<TD style="radial" bgcolor="yellow:gold"  gradientangle="60">"""+str(actual.grupo.nombre_grupo)+"""</TD>\n"""
                while actual_nodo:
                    text+="""<TD style="radial" bgcolor="gold"  gradientangle="60">"""+actual_nodo.dato+"""</TD>\n"""
                    actual_nodo=actual_nodo.siguiente
                text+="""</TR>\n"""
                
            actual = actual.siguiente
        text+="""</TABLE>>];
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng g_reducida.dot -o grafica_matriz_reducida.png')

    def imprimir_lista_grupo(self):
        print("-----------------------------------")
        actual = self.primero
        while actual != None:
            print("Nombre Senal: ",actual.grupo.nombre_senal,"Amplitud: ",actual.grupo.amplitud,"Grupo: ",actual.grupo.nombre_grupo,"Suma: ",actual.grupo.cadena_grupo_sumado)
            actual = actual.siguiente
        print("-----------------------------------")
