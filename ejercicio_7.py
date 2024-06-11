#Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings con tareas pendientes
#y la segunda almacenará strings con tareas terminadas.
# Permita al usuario:
#a. Agregar nuevas tareas pendientes.
#b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar de la lista de pendientes a la de terminadas.
#Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas listas.

lista_tareas_pendientes = []
lista_tareas_terminadas = []

def menu_tareas():
    return int(input("""
----------------MENÚ---------------------------
Seleccionar el número correspondiente para: 
** 1 -Ingresar tareas pendientes
** 2 -Ingresar tareas terminadas
** Ingrese cualquier otro número para salir
-----------------------------------------------                    
"""))

def almacenar_dato(valor, lista):
    lista.append(valor)

def borrar_dato(valor, lista):
    lista.remove(valor)

def agregar_tareas():
    while True:
        valor = menu_tareas()
        match valor:
            case 1:
                pendiente = input("Ingrese las tareas pendientes separadas por comas(,): ")
                tarea = pendiente.split(",")
                for i in tarea:
                    almacenar_dato(i.strip(), lista_tareas_pendientes)
                mostrar_listas()
            case 2:
                terminado = input("Ingrese las tareas terminadas separadas por comas(,): ")
                tareas = terminado.split(",")
                for tarea in tareas:
                    tarea_limpia = tarea.strip()
                    if tarea_limpia in lista_tareas_pendientes:
                        almacenar_dato(tarea_limpia, lista_tareas_terminadas)
                        borrar_dato(tarea_limpia, lista_tareas_pendientes)
                    else:
                        print(f"¡¡Oye!! La tarea {tarea_limpia} no se encuentra en tu lista de tareas pendientes.")
                mostrar_listas()    
            case _:
                print("...Gracias por utilizar nuestro servicio...")
                mostrar_listas()
                break
                
def mostrar_listas():
    print(f"""
Lista de tareas Pendientes: {lista_tareas_pendientes}
Lista de tareas Terminadas: {lista_tareas_terminadas}
---------------------------------------------------------""")
    
agregar_tareas()