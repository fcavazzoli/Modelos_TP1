# Primera entrega del trabajo practico

 - Materia: Modelos y Optimizacion I 
 - Fecha de entrega: 02/05/2022
 - Alumno: Federico Cavazzoli
 - Padron: 98533



# Objetivo
Deterninar el orden en el que el camion debe recorrer los puntos de la ruta cumpliendo con las restricciones de capacidad minimizando la distancia total.

# Hipotesis y Supuestos
 - El camion debe recorrer todos los puntos de la ruta.
 - La carga de todos los puntos es menor o igual a la capacidad del camion.
 - La distancia entre puntos es constante (no se mudan los bancos en ningun momento).
 - No se considera el costo de transporte entre puntos.
 - La distancia de a casa central al cualquier punto es constante.
 - Cualquier punto de la ruta es valido para iniciar el recorrido siempre y cuando cumpla las condiciones de capacidad.
 - El camion solo carga y descarga en los puntos de la ruta (no hay robos y perdidas).
 - El camion no puede cargar y descargar en el mismo punto.


# Algoritmos
## Greedy

La idea de este algoritmo es tomar el punto de inicio y a partir de ahi comenzar a recorrer. 
Siempre se elige como proximo punto aquel mas cercano que cumpla con las condiciones de capacidad y que ademas no haya sido visitado.
Es por definicion, un algoritmo greedy, dado que sin importar el caso en el que se encuentre se aplica el mismo algoritmo para resolver el siguente punto a visitar.

```python
def can_go_to_city(city_weights, city, amount):
    return (amount + city_weights[city] > 0) and (amount + city_weights[city] < 30)


def solve(matrix, city_weights, initial_city):
    solution = [initial_city]
    city = initial_city
    min_city = 0
    current_amount = city_weights[initial_city]
    total_distance = 0
    while len(solution) < len(matrix):
        min_distance = float("inf")
        for i in range(len(matrix)):
            if (i not in solution) and can_go_to_city(city_weights, i, current_amount):
                if matrix[city][i] < min_distance:
                    min_distance = matrix[city][i]
                    min_city = i
        solution.append(min_city)
        city = min_city
        current_amount += city_weights[min_city]
        total_distance += min_distance
    # Primer item es 0 y deberia ser 1, ultimo item es 149 y deberia ser 150.
    return (total_distance, [str(x + 1) for x in solution])
```
## Fuerza Bruta - Greedy

Este algoritmo es una mejora del algoritmo anterior, donde se elige una solucion inicial, se guarda el resultado y luego se elige otro punto de inicio y se vuelve a correr el algoritmo, si la solucion es mejor que la guardada se guarda y se repite el proceso hasta que no queden puntos iniciales por probar.
Cabe aclarar que dadas las condiciones de capacidad el camion parte vacio y es por eso que la primera parada debe ser si o si un punto con carga positiva, entonces todos los negativos son filtrados en un primer paso para evitar ejecuciones inecesarias.

```python
import algorithms.traveling_salesman_solver as tsm

def solve(matrix, city_weights):
    positive_city_weights_index = [
        i for i, x in enumerate(city_weights) if x > 0]
    best_sol = (float("inf"), [])
    for i in positive_city_weights_index:
        sol = tsm.solve(matrix, city_weights, i)
        if sol[0] < best_sol[0]:
            best_sol = sol
    return best_sol[1]
```