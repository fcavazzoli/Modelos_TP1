from helpers.parser import parse_file
import algorithms.traveling_salesman_solver as solver


data = 'datasets/data.txt'

model = parse_file(data)
adjacency_matrix = model.adjacency_matrix()

solution = solver.solve(adjacency_matrix, model.requests)

with open('soluciones/solucion_1.txt', 'w') as f:
    f.write(str(solution))
