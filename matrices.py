#Bernal Flores Axel Sadami
#Téllez López Angel
#algebra libeal
import numpy as np

def pedirMatriz(): #Función para la dimension y los valores de cada posicion
    n = int(input("¿Cuantos lados tendra la matriz? "))
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            valor = float(input(f"Ingresa el valor para la posicion [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return np.array(matriz)

def mostrarMenu():#Función para mostrar al usuario las opciones disponible
    print("Opciones:")
    print("1. Suma de matrices")
    print("2. Resta de matrices")
    print("3. Multiplicacion de matrices")
    print("4. Determinante de una matriz")
    print("5. Matriz inversa")
    print("6. Salir")

def encontrarInversa(A):#Funcion para encontrar la matriz inversa utilizando el metodo de GaussJordan
    n = A.shape[0]
    matriz_aumentada = np.concatenate((A, np.identity(n)), axis=1)
    for i in range(n):
        if matriz_aumentada[i][i] == 0:
            for j in range(i+1, n):
                if matriz_aumentada[j][i] != 0:
                    matriz_aumentada[[i, j]] = matriz_aumentada[[j, i]]
                    break
            else:
                raise ValueError("La matriz no tiene inversa")
        matriz_aumentada[i] = matriz_aumentada[i] / matriz_aumentada[i][i]
        for j in range(n):
            if j != i:
                matriz_aumentada[j] = matriz_aumentada[j] - matriz_aumentada[i] * matriz_aumentada[j][i]
    inversa = matriz_aumentada[:, n:]
    return inversa

while True: #opciones para cada caso
    mostrarMenu()
    opcion = int(input("Ingresa una opcion: "))

    if opcion == 1:
        print("Ingrese la primera matriz:")
        A = pedirMatriz()
        print("Ingrese la segunda matriz:")
        B = pedirMatriz()
        C = A + B
        print("La suma de las matrices es:")
        print(C)

    elif opcion == 2:
        print("Ingrese la primera matriz:")
        A = pedirMatriz()
        print("Ingrese la segunda matriz:")
        B = pedirMatriz()
        C = A - B
        print("La resta de las matrices es:")
        print(C)

    elif opcion == 3:
        print("Ingrese la primera matriz:")
        A = pedirMatriz()
        print("Ingrese la segunda matriz:")
        B = pedirMatriz()
        if A.shape[1] != B.shape[0]:
            print("No se pueden multiplicar estas matrices")
        else:
            C = np.matmul(A, B)
            print("La multiplicación de las matrices es:")
            print(C)

    elif opcion == 4:
        print("Ingrese la matriz:")
        A = pedirMatriz()
        if A.shape[0] != A.shape[1]:
            print("Error: la matriz debe ser cuadrada")
        else:
            det = np.linalg.det(A)
            print("El determinante de la matriz es:")
            print(det)

    elif opcion == 5:
        print("Ingrese la matriz:")
        A = pedirMatriz()
        if A.shape[0] != A.shape[1]:
            print("Error: la matriz debe ser cuadrada")
        else:
            try:
                inversa = encontrarInversa(A)
                print("La matriz inversa es:")
                print(inversa)
            except ValueError as e:
                print(str(e))

    elif opcion == 6:
        break

    else:
        print("Opcion invalida")