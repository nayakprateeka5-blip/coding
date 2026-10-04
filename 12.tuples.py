numbers = (20, 24, 32, 44, 45)

try:
    numbers[1] = 50
except TypeError:
    print("Error: Tuples are immutable and cannot be changed.")
