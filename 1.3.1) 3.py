'''виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
Результати множення елементів занесіть до нової матриці та виведіть її на екран;'''

import numpy as np # імпортуємо бібліотеку NumPy

print('Введіть елементи матриці А:')
a = np.zeros((3, 3), dtype=int) # задаємо масив A розмірністю 3 на 3, заповнений нулями, тиа даних - цілочисельний
for i in range(3):
    for j in range(3):
        a[i, j] = int(input(f'A[{i}, {j}] = ')) # за допомогою циклу користувач надає значення кожному елементу масиву

print()
print('Введіть елементи матриці B:')
b = np.zeros((3, 3), dtype=int) # повторюємо те ж саме з матрицею B
for i in range(3):
    for j in range(3):
        b[i, j] = int(input(f'B[{i}, {j}] = '))

c = np.zeros((3, 3), dtype=int) # задаємо масив С, в який будемо вводити елементи множення матриць A та B
s = 0
for z in range(3):
        for i in range(3):
            for j in range(3):
                s += a[z][j] * b[j][i]  # множимо елементи
            c[z, i] = s  # та додаємо в матрицю C
            s = 0

print() # робимо відступ від попередніх записів
print('Добуток двох квадратних матриць:')
print(c) # виводимо результат множення

