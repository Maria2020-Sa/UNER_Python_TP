#Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
#de una lista vacía:
#a. Agregar un elemento al final.
#b. Agregar un elemento al principio.
#c. Quitar un elemento al final.
#d. Quitar un elemento al principio.


lista = []

def agregar_elemento_al_final(elemento):
    lista.append(elemento)

def agregar_elemento_al_principio(elemento):
    lista.insert(0, elemento)

def quitar_elemento_del_final():
    lista.remove(lista[-1])

def quitar_elemento_del_principio():
    lista.remove(lista[0])

def menu_opciones():
    valor = 1
    print("Bievenido!!")
    while valor != 0:
        valor = int(input("""\nElija una opción del menú:
1-Agregar elementos al final
2-Agregar elementos al principio
3-Quitar elementos del final
4-Quitar elementos del principio
5-Ver lista                          
0-Salir \n Opción: """))   
        match valor :
            case 1:
                elemento = input("Ingrese el elemento: ")
                agregar_elemento_al_final(elemento)
            case 2:
                elemento = input("Ingrese el elemento: ")
                agregar_elemento_al_principio(elemento)
            case 3:
                quitar_elemento_del_final()
                print("Se ha quitado un elemento del final de la lista")                
            case 4:
                quitar_elemento_del_principio()
                print("Se ha quitar un elemento del principio de la lista")
            case 5:
                print("Lista: ", lista)
            case _:
                if(valor != 0): print("Opción invalida")


menu_opciones();                