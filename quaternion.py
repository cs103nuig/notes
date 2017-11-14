from math import sqrt

class Quaternion:
    "Hamilton's quaternions"

    def __init__(self, *coeffs):
        "quaternion constructor"
        self.coeffs = coeffs

    def __repr__(self):
        "string representation"
        return "{} + {}i + {}j + {}k".format(*self.coeffs)

    def __neg__(self):
        "-self"
        return Quaternion(*[-x for x in self.coeffs])

    def __add__(self, other):
        "self + other"
        if not isinstance(other, type(self)):
            raise TypeError("type mismatch: {} + {}"
                        .format(*[type(x).__name__ for x in [self, other]]))
        return Quaternion(*[x + y for x, y in zip(self.coeffs, other.coeffs)])

    def __sub__(self, other):
        "self - other"
        return self + -other

    def __rmul__(self, number):
        "number * self"
        return Quaternion(*[number * x for x in self.coeffs])

    def __mul__(self, other):
        "self * other"
        if not isinstance(other, type(self)):
            raise TypeError("type mismatch: {} * {}"
                        .format(*[type(x).__name__ for x in [self, other]]))

        o = Quaternion(1, 0, 0, 0)
        i = Quaternion(0, 1, 0, 0)
        j = Quaternion(0, 0, 1, 0)
        k = Quaternion(0, 0, 0, 1)
        table = [[o,  i,  j,  k],
                 [i, -o,  k, -j],
                 [j, -k, -o,  i],
                 [k,  j, -i, -o]]

        total = Quaternion(0, 0, 0, 0)
        for r in range(4):
            for s in range(4):
                number = self.coeffs[r] * other.coeffs[s]
                total += number * table[r][s]
        return total

    def conjugate(self):
        "self^*"
        coeffs = [self.coeffs[0]] + [-x for x in self.coeffs[1:]]
        return Quaternion(*coeffs)

    def norm_squared(self):
        "||self||^2"
        return sum(x ** 2 for x in self.coeffs)

    def norm(self):
        "||self||"
        return sqrt(self.norm())

    def inverse(self):
        "1/self"
        return 1 / self.norm_squared() * self.conjugate()

    def __truediv__(self, other):
        "self / other"
        return self * other.inverse()

    def __eq__(self, other):
        "self == other"
        if not isinstance(other, type(self)):
            return False
        for x, y in zip(self.coeff, other.coeff):
            if x != y:
                return False
        return True

o = Quaternion(1, 0, 0, 0)
i = Quaternion(0, 1, 0, 0)
j = Quaternion(0, 0, 1, 0)
k = Quaternion(0, 0, 0, 1)
q = o + 2*i + 3*j + 4*k
w = Quaternion(1, 1, 1, 1)
