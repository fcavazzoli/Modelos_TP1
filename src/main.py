from helpers.parser import parse_file
import algorithms.traveling_salesman_solver as solver


data = 'datasets/data.txt'

model = parse_file(data)
adjacency_matrix = model.adjacency_matrix()

solution = solver.solve(adjacency_matrix)

with open('soluciones/solucion_1.txt', 'w') as f:
    for row in adjacency_matrix:
        f.write(' '.join(map(str, row)) + '\n')
