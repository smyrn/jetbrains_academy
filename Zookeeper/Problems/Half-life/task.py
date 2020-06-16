n_atoms = int(input())
final_quantity = int(input())

counter = 0
while n_atoms > final_quantity:
    counter += 1
    n_atoms /= 2

print(counter * 12)
