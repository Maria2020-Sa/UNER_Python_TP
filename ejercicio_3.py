#Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], 
# permitir al usuario ingresar 3 frutas más para agregarlas al final de lista. 
# Luego, mostrar por pantalla la lista completa y 
# debajo la misma lista pero sólo con las frutas que añadió el usuario.

lista_frutas = ["banana", "manzana", "pera"]
lista_nueva = []

def almacenar_frutas(otra_fruta):
    lista_frutas.extend(otra_fruta)

def ingresar_frutas():
    i = 0
    print("Ingrese tres frutas más por favor: ")
    while i < 3:
        lista_nueva.append(input(f"Ingrese {i+1} fruta por favor: "))
        i+=1
    almacenar_frutas(lista_nueva)

ingresar_frutas()
print(f"Lista completa de frutas: {lista_frutas}")
print(f"Lista solo con frutas ingresadas por el usuario: {lista_nueva}")
        

