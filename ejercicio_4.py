# Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”],
#realizar lo siguiente:
#a. Imprimir la cantidad de elementos que tiene la lista.
#b. Imprimir el primer y último elemento.
#c. Imprimir el resto.
#d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
#la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
#e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de
#la lista. Quitar el elemento correspondiente de esa posición.
#f. Imprimir la lista en orden inverso.
#g. Vaciar la lista.

paises = [ "Argentina" ,"Brasil", "Bolivia","Paraguay","Venezuela"]
paises_minusculas = [s.lower() for s in paises]

def imprimir_longitud_lista():
    print("Cantidad de paises: ", len(paises))

def imprimir_primer_ultimo_elemento():
    print("Primer elemento: ", paises[0])
    print("Último elemento: ", paises[-1])

def imprimir_elementos_restantes():
    print("Paises restantes: ", paises[1:-1])

def buscar_paises():
    valor = input("Por favor ingrese un pais: ").lower()
    if(valor in  paises_minusculas):
        print("Indice: ", paises_minusculas.index(valor))
    else:
        print("El pais no se encuentra en la lista")

def ingresar_paises():
    index_elemento = int(input(f"Ingrese un valor entre o y  { len(paises)-1 }: "))
    paises.remove(paises[index_elemento])
    print("Nueva lista de paises: ", paises)

def imprimir_orden_inverso():
    print("Lista inversa: ", paises[::-1])

def vaciar_lista():
    print("Lista vacia: ", paises.clear())

imprimir_longitud_lista()
imprimir_primer_ultimo_elemento()
imprimir_elementos_restantes()
buscar_paises()
ingresar_paises()
imprimir_orden_inverso()
vaciar_lista()