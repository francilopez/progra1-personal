import random

def mostrar_matriz(matriz, estudiantes, materias):
    print("notas:")
    
    print(f"{'alumno':<12}", end="")
    for materia in materias:
        print(f"{materia:<12}", end=" ")       #:<12 para alinear las notas con las materias y end="    "
    print()
    
    num_estudiantes = len(estudiantes)
    num_materias = len(materias)
    
    for i in range(num_estudiantes):
        print(f"{estudiantes[i]:<12}", end="       ")
        for j in range(num_materias):
            print(f"{matriz[i][j]:<12}", end="")
        print()

def calcular_promedio_estudiantes(matriz, estudiantes):
    print("\npromedio de notas por alumno:")
    for i in range(len(matriz)):
        promedio = sum(matriz[i]) / len(matriz[i])
        print(f"{estudiantes[i]}: {promedio:.2f}")

def calcular_promedio_materias(matriz, materias):
    print("\npromedio de notas por materia:")
    num_materias = len(materias)
    for j in range(num_materias):
        suma = sum(matriz[i][j] for i in range(len(matriz)))
        promedio = suma / len(matriz)
        print(f"{materias[j]}: {promedio:.2f}")



alumnos = ["francisco", "jose", "catalina", "ciro"]

materias = ["programacion", "marketing", "testing de apps", "sistemas operativos"]

num_alumnos = len(alumnos)

num_materias = len(materias)

matriz_notas = [[random.randint(1,10) for _ in range (num_materias)] for _ in range (num_alumnos)]  #lista por comprension 


mostrar_matriz(matriz_notas, alumnos, materias)
print(calcular_promedio_estudiantes(matriz_notas, alumnos))
print(calcular_promedio_materias(matriz_notas, materias))