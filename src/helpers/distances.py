import math


def coor_to_km(x, y):
    lat1, lon1 = x
    lat2, lon2 = y
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)
