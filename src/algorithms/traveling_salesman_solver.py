from locale import currency


def can_go_to_city(city_weights, city, amount):
    return amount + city_weights[city] > 0


def solve(matrix, city_weights):
    solution = [0]
    city = 0
    min_city = 0
    current_amount = city_weights[0]
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
    print("total_distance:", total_distance)
    return [str(x + 1) for x in solution]
