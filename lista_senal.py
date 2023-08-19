from nodo_senal import nodo_senal

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
    
    def recorrer_imprimir_senal(self):
        print("-----------------------------------")
        print("Total de Señales:",self.contador_senal)
        print("")
        print("")
        actual=self.primero

        while actual !=None:
            print("Nombre:",actual.senal.nombre,"Tiempo:",actual.senal.tiempo,"Amplitud:",actual.senal.amplitud)
            actual.senal.lista_dato.recorrer_imprimir_dato()
            actual.senal.lista_patrones.recorrer_imprimir_dato()
            actual=actual.siguiente
            print("")
            print("")
        print("-----------------------------------")




