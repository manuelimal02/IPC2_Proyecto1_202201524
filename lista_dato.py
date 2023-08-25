import sys
import os
from nodo_dato import nodo_dato
from patron import patron

class lista_dato:
    def __init__(self):
        self.primero=None
        self.contador_dato=0
    
    def insertar_dato(self,dato):
        nuevo_dato=nodo_dato(dato=dato)
        self.contador_dato+=1
        #Si Lista Vacía
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

    # método para devolver los patrones por nivel
    def devolver_patrones_por_tiempo(self,lista_patron):
        actual = self.primero
        sentinela_de_filas=actual.dato.tiempo #iniciaria en 1
        fila_iniciada=False
        recolector_patron=""
        while actual != None:
            # si hay cambio de fila entramos al if
            if  sentinela_de_filas!=actual.dato.tiempo:
                # fila iniciada se vuelve false, por que se acaba la fila
                fila_iniciada=False
                # ya que terminamos la fila, podemos guardar los patrones
                lista_patron.insertar_patron(patron(sentinela_de_filas,recolector_patron))
                recolector_patron=""
                # actualizamos el valor de la fila (nivel)
                sentinela_de_filas=actual.dato.tiempo 
            # si fila iniciada es false, quiere decir que acaba de terminar fila y debemos empezar una nueva
            if fila_iniciada==False:
                fila_iniciada=True
                #Recolectamos el valor, ya que estamos en la fila
                recolector_patron+=str(actual.dato.valor)+" "
            else:
                #Recolectamos el valor, ya que estamos en la fila
                recolector_patron+=str(actual.dato.valor)+" "
            actual = actual.siguiente
        # Agregamos un nuevo patrón, sería el de toda la fila, ej: 0-1-1-1
        lista_patron.insertar_patron(patron(sentinela_de_filas,recolector_patron))
        # devolvermos la lista llena con los patrones
        return lista_patron

    def devolver_cadena_del_grupo(self,grupo):
        string_resultado=""
        string_temporal=""
        buffer=""
        # viene un parametro llamado grupo, es un string con este formato "1,2"
        # recorremos caracter por caracter
        for digito in grupo:
            #si es digito
            if digito.isdigit():
                #añadimos al buffer
                buffer+=digito
            else:
                # si no es buffer, lo vaciamos
                string_temporal=""
                #recorremos la lista y recuperamos los valores para este grupo
                actual = self.primero
                while actual != None:
                    # si encontramos coincidencia del digito y el nivel , obtenemos su valor
                    if actual.dato.tiempo==int(buffer):
                        string_temporal+=str(actual.dato.valor)+"-"
                    actual = actual.siguiente
                string_resultado=string_resultado+string_temporal+"%"
                buffer=""
        #devolvemos el string resultado
        return string_resultado

    def sum_substrings(input_string):
        sub_strings = input_string.split('%')
        if len(input_string) == 9:
            return input_string.rstrip('-%')
        else: 
            first_values = sub_strings[0].split('-')
            second_values = sub_strings[1].split('-')
            result = []
            for first, second in zip(first_values, second_values):
                if first.isdigit() and second.isdigit():
                    result.append(str(int(first) + int(second)))
            return "-".join(result)


    def generar_grafica_matriz_original(self,nombre,tiempo,amplitud):
        f = open('bb.dot','w')
        text ="""
            digraph G {
                subgraph cluster17
                    {
                    n019 ;
                    n019 [label="Nombre Senal: """+nombre+""""] ;
                    n019 -> n020 ;
                    n020 [label="Tiempo: """+tiempo+""""] ;
                    n019 -> n021 ;
                    n021 [label="Amplitud: """+amplitud+""""] ;
                    }
            label="Matriz de Onda Original"
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
                text+="""<TD bgcolor="brown:purple"  gradientangle="315">"""+str(actual.dato.valor)+"""</TD>\n"""
            else:
                text+="""<TD bgcolor="brown:violet"  gradientangle="315">"""+str(actual.dato.valor)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o grafica_matriz_original.png')

