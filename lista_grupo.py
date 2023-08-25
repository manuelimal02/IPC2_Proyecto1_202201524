from nodo_grupo import nodo_grupo

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


    def imprimir_lista_grupo(self):
        print("===========================================================================================")
        actual = self.primero
        while actual != None:
            print(" Grupo: ",actual.grupo.nombre_grupo)
            print("Cadena-grupo:"+"\n",actual.grupo.cadena_grupo)
            actual = actual.siguiente
        print("===========================================================================================")