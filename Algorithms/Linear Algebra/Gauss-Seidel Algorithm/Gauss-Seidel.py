#!bin/python
import numpy as np
from numpy.linalg import inv

print("Enter the coefficients of the equation in matlab matrix notation")
arrInput = input("i.e. [1 1; 2 2], ; is the newline: \n")

rows = arrInput[1:len(arrInput) - 1].split("; ")
matrixT = [list(row.split(" ")) for row in rows]

for i in range(len(matrixT)):
    matrixT[i] = list(map(int, matrixT[i]))

print("Enter the answers to the system of linear equations")
arrInput = input("i.e. [1 2]: \n")

bTemp = [int(x) for x in arrInput[1:len(arrInput) - 1].split(" ")]

matrix = np.array(matrixT)
b = np.transpose(np.array(bTemp)[np.newaxis])

x = np.zeros_like(b)
ITER_LIMIT = 10000
L_STAR = inv(np.tril(matrix))
a = np.triu(matrix, 1)
T = np.dot(np.negative(L_STAR), a)
C = np.dot(L_STAR, b)

for i in range(ITER_LIMIT):
    xTemp = np.add(np.dot(T, x), C)

    if np.allclose(x, xTemp, rtol=1e-6):
        break

    x = xTemp

print("Answer: ")
print(x)
