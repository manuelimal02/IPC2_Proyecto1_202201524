import sys
import os
from nodo_dato import nodo_dato
from patron import patron

class lista_dato:
    def __init__(self):
        self.primero=None
        self.contador_dato=0

    def imprimir_valor(self):
        print("-----------------------------------")
        actual=self.primero
        while actual !=None:
            print("T:",actual.dato.tiempo,"A:",actual.dato.amplitud,"V:",actual.dato.valor)
            actual=actual.siguiente   
        print("-----------------------------------") 

    def insertar_dato(self,dato):
        nuevo_dato=nodo_dato(dato=dato)
        self.contador_dato+=1
        if self.primero is None:
            self.primero =nuevo_dato
            return
        if dato.tiempo < self.primero.dato.tiempo or(dato.tiempo==self.primero.dato.tiempo and dato.amplitud<=self.primero.dato.amplitud):
            nuevo_dato.siguiente=self.primero
            self.primero=nuevo_dato
            return
        actual=self.primero
        while actual.siguiente is not None and(dato.tiempo>actual.siguiente.dato.tiempo or (dato.tiempo == actual.siguiente.dato.tiempo and dato.amplitud > actual.siguiente.dato.amplitud)):
            actual=actual.siguiente
        nuevo_dato.siguiente=actual.siguiente
        actual.siguiente=nuevo_dato

    def patrones_por_tiempo(self,lista_patron):
        actual = self.primero
        sentinela_de_filas=actual.dato.tiempo
        fila_iniciada=False
        recolector_patron=""
        while actual != None:
            if  sentinela_de_filas!=actual.dato.tiempo:
                fila_iniciada=False
                lista_patron.insertar_patron(patron(sentinela_de_filas,recolector_patron))
                recolector_patron=""
                sentinela_de_filas=actual.dato.tiempo 
            if fila_iniciada==False:
                fila_iniciada=True
                recolector_patron+=str(actual.dato.valor)+" "
            else:
                recolector_patron+=str(actual.dato.valor)+" "
            actual = actual.siguiente
        lista_patron.insertar_patron(patron(sentinela_de_filas,recolector_patron))
        return lista_patron

    def cadena_del_grupo(self,grupo):
        string_resultado=""
        string_temporal=""
        buffer=""
        for digito in grupo:
            if digito.isdigit():
                buffer+=digito
            else:
                string_temporal=""
                actual = self.primero
                while actual != None:
                    if actual.dato.tiempo==int(buffer):
                        string_temporal+=str(actual.dato.valor)+"-"
                    actual = actual.siguiente
                string_resultado=string_resultado+string_temporal+"!"
                buffer=""
        return string_resultado

    def grafica_matriz_original(self,nombre,tiempo,amplitud):
        f = open('g_original.dot','w')
        text ="""
            digraph G {
            label="Matriz Original"
                subgraph cluster1 {bgcolor="purple:pink" label="Matriz Reducida" fontcolor="white"
                    fillcolor="blue:cyan" label="Senal: """+nombre+"""" fontcolor="white" style="filled" gradientangle="270"
                    node [shape=box fillcolor="red:yellow" style="filled" gradientangle=90]
                    "Tiempo: """+tiempo+"""";
                    "Amplitud: """+amplitud+"""";
                    }
            fontname="Helvetica,Arial,sans-serif"
            node [fontname="Helvetica,Arial,sans-serif"]
            edge [fontname="Helvetica,Arial,sans-serif"]
            a0 [shape=none  label=<
            <TABLE border="0" cellspacing="10" cellpadding="10" >\n"""
        actual = self.primero
        sentinela_de_filas=actual.dato.tiempo
        fila_iniciada=False
        while actual != None:
            if  sentinela_de_filas!=actual.dato.tiempo:
                sentinela_de_filas=actual.dato.tiempo
                fila_iniciada=False
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                text+="""<TR>"""  
                text+="""<TD style="radial" bgcolor="yellow:green"  gradientangle="60">"""+str(actual.dato.valor)+"""</TD>\n"""
            else:
                text+="""<TD style="radial" bgcolor="yellow:green"  gradientangle="60">"""+str(actual.dato.valor)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng g_original.dot -o grafica_matriz_original.png')

