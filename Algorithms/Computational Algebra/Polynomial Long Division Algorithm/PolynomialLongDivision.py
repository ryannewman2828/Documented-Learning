#!/usr/bin/python
import copy


class Polynomial:
    # coeffs is a list of the coefficients where index represents the degree
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __deepcopy__(self, memo={}):
        return Polynomial(copy.deepcopy(self.coeffs))

    def __getitem__(self, degree):
        return self.coeffs[degree - 1]

    def __sub__(self, polynomial):
        for i in range(0, len(polynomial.coeffs)):
            self.coeffs[i] -= polynomial.coeffs[i]
        # Removes the powers with a coefficient of 0 from the end
        while self.coeffs[len(self.coeffs) - 1] == 0:
            self.coeffs = self.coeffs[:len(self.coeffs) - 1]
        return self

    def __mul__(self, other):
        for i in range(0, len(self.coeffs)):
            self.coeffs[i] *= other
        return self

    def __str__(self):
        ans = ""
        if self.coeffs[len(self.coeffs) - 1] != 0 and len(self.coeffs) > 1:
            if self.coeffs[len(self.coeffs) - 1] < 0:
                ans += "-" + str(abs(self.coeffs[len(self.coeffs) - 1])) + "x^" + str(len(self.coeffs) - 1)
            else:
                ans += str(self.coeffs[len(self.coeffs) - 1]) + "x^" + str(len(self.coeffs) - 1)
        for i in range(len(self.coeffs) - 2, 0, -1):
            if self.coeffs[i] != 0:
                if self.coeffs[i] > 0:
                    ans += " + "
                else:
                    ans += " - "
                ans += str(abs(self.coeffs[i])) + "x^" + str(i)
        if self.coeffs[0] != 0:
            if self.coeffs[0] > 0:
                ans += " + "
            else:
                ans += " - "
            ans += str(abs(self.coeffs[0]))
        return ans

    # Returns the degree of the polynomial
    def degree(self):
        return len(self.coeffs)


def longDivision(dividend, divisor):
    if divisor.degree() == 0:
        return  # Error
    q = [0] * (dividend.degree() - divisor.degree() + 1)
    while dividend.degree() >= divisor.degree():
        coeffs = [0] * (dividend.degree() - divisor.degree())
        coeffs.extend(divisor.coeffs)
        d = Polynomial(coeffs)
        q[dividend.degree() - divisor.degree()] = int(dividend[dividend.degree()] / d[d.degree()])
        d *= q[dividend.degree() - divisor.degree()]
        dividend -= d
    return Polynomial(q), dividend


# Set the dividend here
# x^3 - 12x^2 - 42
dividend = Polynomial([-42, 0, -12, 1])

# Set the divisor here
# x - 3
divisor = Polynomial([-3, 1])

t = longDivision(copy.deepcopy(dividend), divisor)
print("(" + str(dividend) + ") / (" + str(divisor) + ") = " + str(t[0]) + " Remainder = " + str(t[1]))

# List of tuples to iteratively test on
examples = [(Polynomial([-4, 0, -2, 1]), Polynomial([-3, 1])),
            (Polynomial([-3, 2, -4, 1]), Polynomial([2, 1])),
            (Polynomial([-7, 2, -13, 4]), Polynomial([-2, 3, 1])),
            (Polynomial([5, 0, -2, 3]), Polynomial([-1, 0, 1]))]

for ex in examples:
    t = longDivision(copy.deepcopy(ex[0]), ex[1])
    print("(" + str(dividend) + ") / (" + str(divisor) + ") = " + str(t[0]) + " Remainder = " + str(t[1]))
