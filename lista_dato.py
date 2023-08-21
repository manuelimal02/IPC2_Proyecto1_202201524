from nodo_dato import nodo_dato

class lista_dato:
    def __init__(self):
        self.primero=None
        self.contador_dato=0
    
    def insertar_dato(self,dato):
        if self.primero is None:
            self.primero=nodo_dato(dato=dato)
            self.contador_dato+=1
            return
        
        actual=self.primero

        while actual.siguiente:
            actual=actual.siguiente

        actual.siguiente=nodo_dato(dato=dato)
        self.contador_dato+=1
    
    def recorrer_imprimir_dato(self):
        print("-----------------------------------")
        actual=self.primero

        while actual !=None:
            print("T:",actual.dato.tiempo,"A:",actual.dato.amplitud,"V:",actual.dato.valor)
            actual=actual.siguiente   
        print("-----------------------------------")

