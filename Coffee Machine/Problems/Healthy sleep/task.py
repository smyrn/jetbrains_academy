a_hours = int(input())
b_hours = int(input())
h_hours = int(input())

if a_hours <= h_hours <= b_hours:
    print("Normal")
else:
    if h_hours < a_hours:
        print('Deficiency')
    if h_hours > b_hours:
        print("Excess")
