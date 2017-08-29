#!/usr/bin/python
import ast
import numpy as np

# Assumption is that the Linear Program is in SEF


# Prints the linear program defined by the
def printLP(obj, constraints, conV):
    print("MAX " + str(obj) + "x")
    print("Subject To")
    print(str(constraints) + "x = " + str(conV))


def newCanonical(matrix, entering, exiting):
    return 0


def runSimplex(obj, constraints, conV):
    return 0

print("Enter Objective Function Vector")
obj = input()        # the user is expected to enter a 2D array like [[1,2],[3,4]] for example
obj = np.array(ast.literal_eval(obj))

print("Enter Constraint Matrix")
constraints = input()
constraints = np.array(ast.literal_eval(constraints))
constraints = np.asmatrix(constraints)

print("Enter Constraint Vector")
conV = input()
conV = np.array(ast.literal_eval(conV))

print("Constructing the auxiliary LP:")
objA = np.zeros((len(obj),), dtype=np.int)
objA = np.append(objA, -1 * np.ones((constraints.shape[0],), dtype=np.int))

constraintsA = constraints.copy()
for i in range(len(conV)):
    if conV[i] < 0:
        constraintsA[i:, ] *= -1
        conV[i] *= -1

constraintsA = np.concatenate((constraintsA, np.identity(constraints.shape[0], dtype=np.int)), axis=1)
conVA = conV.copy()

printLP(objA, constraintsA, conVA)

# Runs simplex on auxiliary LP
optVal = runSimplex(objA, constraintsA, conVA)
