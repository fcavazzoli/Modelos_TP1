from helpers.parser import parse_file
import algorithms.brut_force as bf
import algorithms.traveling_salesman_solver as tsm

data = 'datasets/data_3.txt'

model = parse_file(data)
print('cargando datos')
adjacency_matrix = model.adjacency_matrix()

solution = tsm.solve(adjacency_matrix, model.requests, 0)

with open('soluciones/solucion_4.txt', 'w') as f:
    f.write(','.join(solution[1]))
