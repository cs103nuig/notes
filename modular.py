def egcd(a, b):
    "find integers  x, y  such that  gcd(a,b) = x*a + y*b"
    if b == 0:
        return (1, 0)
    x, y = egcd(b, a % b)
    x, y = y, x - (a // b) * y
    return (x, y)

def modular_inverse(a, m):
    "compute the modular inverse of a modulo m"
    x, y = egcd(m, a)
    d = x * m + y * a
    if d == 1:
        return y % m
    print("error: ", a, "has no inverse mod", m, ": d = ", d)

def product_numbers(numbers):
    "compute the product of a list of numbers"
    total = 1
    for number in numbers:
        total *= number
    return total

def chinese_remainder(moduli, residues):
    "compute the chinese remainders of residues mod moduli"
    M = product_numbers(moduli)
    total = 0
    for i in range(len(moduli)):
        a = residues[i]
        m = moduli[i]
        m1 = M // m
        n = modular_inverse(m1, m)
        total += a * m1 * n
    return total % M
