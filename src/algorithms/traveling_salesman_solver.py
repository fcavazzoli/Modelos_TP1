from locale import currency
from os import PRIO_USER


def can_go_to_city(city_weights, city, amount):
    return (amount + city_weights[city] > 0) and (amount + city_weights[city] < 100)


def solve(matrix, city_weights, initial_city):
    print("empizando")
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
        print("Current " + len(solution).__str__() + " cities")
    # Primer item es 0 y deberia ser 1, ultimo item es 149 y deberia ser 150.
    return (total_distance, [str(x + 1) for x in solution])
