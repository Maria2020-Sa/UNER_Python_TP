#Escriba un programa Python que solicite al usuario el ingreso de números enteros. 
# Cuando el usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos.  
# Cada uno de los números ingresados por el usuario deberá ser almacenado en una lista. 
# A continuación, realice las siguientes tareas:
#a. Determinar el máximo.
#b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
#c. Determinar el mínimo.
#d. Calcular la multiplicación de todos los números de la lista.
#e. Contar los valores pares e impares.
#f. Remover los elementos repetidos.

lista_numeros = []
def almacenar_dato(numero, lista):
    lista.append(int(numero))

def solicitar_datos():
    print("Para salir ingrese <fin>")
    numero = input("Ingrese cualquier número entero o <fin>: ")
    while numero != "fin":   
        almacenar_dato(numero, lista_numeros)     
        numero = input("Ingrese cualquier número entero o <fin>: ")
    print(f"**Lista: {lista_numeros}")

def determinar_maximo(lista):
    max_lista = max(lista)
    print(f"**Número máximo de la Lista: {max_lista}")

def obtener_segundo_maximo(lista):
    lista_modificada = lista.copy()
    maximo = max(lista_modificada)

    lista_modificada.remove(maximo)
    if lista_modificada:
        max_lista = max(lista_modificada)
        print(f"**Segundo número máximo de la Lista: {max_lista}")
    else:
        print(f"**No hay un segundo número máximo")

def determinar_minimo(lista):
    min_lista = min(lista)
    print(f"**Número mínimos de la Lista: {min_lista} ")

def calcular_multipicacion(lista):
    i = 1
    for numero in lista:
        i*=numero
    print(f"**Multiplicación de todos los números de la lista es: {i}")

def determinar_par(lista):
    lista_pares = []
    lista_impares = []
    for numero in lista:
        if numero % 2 == 0:
            almacenar_dato(numero, lista_pares)
        else: 
            almacenar_dato(numero, lista_impares)
    print(f"**Número pares: {lista_pares}")
    print(f"**Números impares: {lista_impares}")

def remover_repetidos(lista):
    lista_sin_duplicados = []
    for valor in lista:
        if valor not in lista_sin_duplicados:
            almacenar_dato(valor, lista_sin_duplicados)
    print(f"Lista sin duplicados: {lista_sin_duplicados}")

def iniciar_programa_python(lista):
    solicitar_datos()
    determinar_maximo(lista)
    obtener_segundo_maximo(lista)
    determinar_minimo(lista)
    calcular_multipicacion(lista)
    determinar_par(lista)
    remover_repetidos(lista)

iniciar_programa_python(lista_numeros)