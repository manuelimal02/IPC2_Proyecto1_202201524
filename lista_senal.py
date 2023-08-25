from nodo_senal import nodo_senal
from grupo import grupo

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

  

    def calcular_los_patrones(self,nombre_senal):
        # recorremos la lista de carceles hasta encontrar una coincidencia
        actual = self.primero
        while actual != None:
            # Si entra al if, es por que encontramos la carcel que queremos
            if actual.senal.nombre==nombre_senal:
                # Obtenemos sus patrones
                actual.senal.lista_patron=actual.senal.lista_binaria.devolver_patrones_por_tiempo(actual.senal.lista_patron)
                # Imprimimos todos sus patrones
                actual.senal.lista_patron.imprimir_lista_patron()
                # obtenemos los grupos
                lista_patrones_temporal=actual.senal.lista_patron
                grupos_sin_analizar=lista_patrones_temporal.encontrar_coincidencias()
                # Este es un string, por ejemplo "1,2--3,5--4"
                #print(grupos_sin_analizar)
                # por cada grupo recorrer la matriz original e ir devolviendo las coordenadas especificadas
                #recordando que por cada coincidencia encontrada, se va borrando para dejar solo las que no tienen grupo.
                buffer=""
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito==",":
                        buffer+=digito
                    elif digito =="-" and buffer!="":
                        cadena_grupo=actual.senal.lista_dato.devolver_cadena_del_grupo(buffer)
                        print("Prueba")
                        suma=sum_substrings(cadena_grupo)
                        print(suma)
                        print("Prueba")
                        actual.senal.lista_grupo.insertar_grupo(grupo=grupo(buffer,cadena_grupo))
                        buffer=""
                    else:
                        buffer=""
                actual.senal.lista_grupo.imprimir_lista_grupo()
                return
            actual=actual.siguiente
        print ("No se encontró la carcel")






