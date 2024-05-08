single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []

#Printing every digit
for digit in single_digits:
    print(digit)
    squares.append(digit ** 2)
print(squares)

cubes = [cube **3 for cube in single_digits]
print(cubes)