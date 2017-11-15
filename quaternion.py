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

        a, b = self.coeffs, other.coeffs
        return Quaternion(
            a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3],
            a[0]*b[1] + a[1]*b[0] + a[2]*b[3] - a[3]*b[2],
            a[0]*b[2] - a[1]*b[3] + a[2]*b[0] + a[3]*b[1],
            a[0]*b[3] + a[1]*b[2] - a[2]*b[1] + a[3]*b[0]
        )

    def conjugate(self):
        "self^*"
        return Quaternion(self.coeffs[0], *[-x for x in self.coeffs[1:]])

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
