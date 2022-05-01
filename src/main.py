from helpers.parser import parse_file
import algorithms.brut_force as bf

data = 'datasets/data.txt'

model = parse_file(data)
adjacency_matrix = model.adjacency_matrix()

solution = bf.solve(adjacency_matrix, model.requests)

with open('soluciones/solucion_1.txt', 'w') as f:
    f.write(' '.join(solution))
