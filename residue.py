def gcd(a, b):
    "Euclid's algorithm"
    if b == 0:
        return a
    return gcd(b, a % b)

def egcd(a, b):
    "find integers  x, y  such that  gcd(a, b) = x*a + y*b"
    if b == 0:
        return (1, 0)
    x, y = egcd(b, a % b)
    x, y = y, x - (a // b) * y
    return (x, y)

class Residue:
    "residue classes"

    def __init__(self, val, mod):
        "constructor for the residue class of val modulo mod"
        self.val = val % mod
        self.mod = mod

    def __repr__(self):
        "string representation"
        return "Residue({}, {})".format(self.val, self.mod)

    def __mul__(self, other):
        "self * other"
        if self.mod != other.mod:
            raise TypeError("operands must have same modulus")
        return Residue(self.val * other.val, self.mod)

    def inverse(self):
        "1/self: extended gcd"
        x, y = egcd(self.mod, self.val)
        d = x * self.mod + y * self.val
        if d != 1:
            raise ValueError("{} has no inverse mod {}".format(self.val, self.mod))
        return Residue(y, self.mod)

    def __pow__(self, exp):
        "self ** exp"
        if exp == 0:
            return Residue(1, self.mod)
        elif exp == 1:
            return self
        else:
            q, r = divmod(exp, 2) # exp == 2 * q + r, r < 2
            result = (self * self) ** q
            if r > 0:
                result *= self
            return result

