from math import log


value1 = abs(int(input()))
value2 = int(input())

if value2 <= 1:
    print(f'{round(log(value1), 2)}')
else:
    print(f'{round(log(value1, value2), 2)}')
