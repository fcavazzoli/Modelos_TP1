from typing import List
from helpers.distances import coor_to_km


class Model:
    capacity = 0
    dimension = 0
    requests = []
    nodes = []
    distance_type = ''

    def __init__(self):
        pass

    def adjacency_matrix(self):
        matrix = [[0 for i in range(self.dimension)]
                  for j in range(self.dimension)]
        for i in range(self.dimension):
            for j in range(self.dimension):
                if i != j:
                    matrix[i][j] = self.euclidean_distance(
                        self.nodes[i], self.nodes[j])
        return matrix

    def euclidean_distance(self, node1, node2):
        return coor_to_km(node1, node2)
