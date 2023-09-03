from nodo import Nodo
class lista_simple:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.fin is None:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo