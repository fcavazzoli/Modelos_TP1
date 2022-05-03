from helpers.parser import parse_file
import algorithms.brut_force as bf
import algorithms.traveling_salesman_solver as tsm

data = 'datasets/data.txt'

model = parse_file(data)
adjacency_matrix = model.adjacency_matrix()

solution = tsm.solve(adjacency_matrix, model.requests, 0)

with open('soluciones/solucion_2.txt', 'w') as f:
    f.write(' '.join(solution[1]))
