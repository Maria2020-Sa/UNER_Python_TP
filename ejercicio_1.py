#Crear un programa que almacene en una lista las materias de esta u otra carrera y que las
#muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario).


lista_materias=["programaciónI", "Introducción a la Informatica","Diseño Gráfico", "Arquitectura de Computadoras", "Programación II"]

def almacenar_materias(materias):
    lista_nueva = []
    lista_nueva.extend(lista_materias)
    print(f"{lista_nueva}\n")

print("""
              ************************
Materias de Programación Universitaria en Desarrollo Web 1er año
              ************************\n""")       
almacenar_materias(lista_materias)