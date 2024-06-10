#Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
#Imprimir por pantalla el resultado.

lista =  []
def almacenar_datos(valor):
    lista.append(valor)

def odernar_datos():
    lista.sort()

def solicitar_datos():
    i = 0
    print("Por favor ingrese cinco valores")
    while i < 5:
        valor = input(f"ingrese el { i+1 } valor: ")
        almacenar_datos(valor)
        i+=1    
    odernar_datos()

solicitar_datos()
print("valores de la lista", lista)