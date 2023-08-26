from nodo_senal import nodo_senal
from grupo import grupo

def procesar_cadena(cadena):
    subcadenas = cadena.split("%")
    suma_total = None

    for subcadena in subcadenas:
        valores = subcadena.split("-")
        
        if suma_total is None:
            suma_total = valores
        else:
            for i in range(len(valores)):
                if valores[i]:
                    suma_total[i] = str(int(suma_total[i]) + int(valores[i]))
    return "-".join(suma_total)

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
        print("Total de Señales:",self.contador_senal)
        actual=self.primero
        while actual !=None:
            print("Nombre:",actual.senal.nombre)
            actual=actual.siguiente
        print("-----------------------------------")

    def grafica_matrices(self,nombre):
        actual=self.primero
        nombre_encontrado=False
        while actual != None:
            if actual.senal.nombre==nombre:
                nombre_encontrado=True
                break
            else:
                actual=actual.siguiente
        if nombre_encontrado:
            #print("Gráfica matriz original de la señal "+nombre+" generada correctamente.")
            #actual.senal.lista_dato.grafica_matriz_original(actual.senal.nombre,str(actual.senal.tiempo),str(actual.senal.amplitud))
            print("Gráfica matriz reducida de la señal "+nombre+" generada correctamente.")
            actual.senal.lista_grupo.grafica_matriz_reducida(nombre)
        else:
            print("No existe una señal con el nombre: "+nombre)


    def calcular_los_patrones(self):
        actual=self.primero
        while actual !=None:

            nombre_senal=actual.senal.nombre
            amplitud_senal=actual.senal.amplitud

            #print("Procesando la Señal: "+actual.senal.nombre)
            # Si entra al if, es por que encontramos la carcel que queremos
            #if actual.senal.nombre==nombre_senal:
            # Obtenemos sus patrones

            actual.senal.lista_patron=actual.senal.lista_binaria.devolver_patrones_por_tiempo(actual.senal.lista_patron)

            # Imprimimos todos sus patrones
            #print("Calculando la matriz binaria...")

            #actual.senal.lista_patron.imprimir_lista_patron()
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

                    cadena_grupo_sumado=procesar_cadena(cadena_grupo)

                    actual.senal.lista_grupo.insertar_grupo(grupo=grupo(nombre_senal,amplitud_senal,buffer,cadena_grupo,cadena_grupo_sumado))
                    buffer=""
                else:
                    buffer=""
            actual.senal.lista_grupo.imprimir_lista_grupo()
            #print("Realizando suma de duplas...")
            #print("")
            actual=actual.siguiente


    






