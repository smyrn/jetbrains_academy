from math import sqrt

edge_length = abs(int(input()))
oct_area = 2 * sqrt(3) * pow(edge_length, 2)
oct_volume = (1 / 3) * sqrt(2) * pow(edge_length, 3)
print(f'{round(oct_area, 2)} {round(oct_volume, 2)}')
