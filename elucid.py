# a implementation of the Extended Euclid's GCD algorithm.
def gcd(a,b):
    inversed = False
    if a < b:
        inversed = True
        c = b
        b = a
        a = c
    assert a >= b and b >=0 and a + b > 0
    if b <= 0:

        d, x, y = a, 1, 0
    else:

        (d, p, q) = gcd(b, a % b)

        x = q
        y = p -q*(a//b)

    if inversed:
        return (d, y, x)
    else:
        return (d,x,y)

def lcm(a, b):
    assert a > 0 and b > 0
    (d, x, y) = gcd(a,b)
    return a * b/ d


def diophantine(a, b, c):
    (d, x, y) = gcd(a, b)
    assert c % d == 0

    factor = c / d

    x = x * factor
    y = y * factor

    return (x, y)


def divide(a, b, n):
    assert n > 1 and a > 0
    (d, x, y) = gcd(a, n)

    if d != 1:
        print('No inverse multiplicative inverse exist')
        return
    else:
        inverse = x % n
        inverse = (b * inverse) % n

    return inverse



print(diophantine(2, 9, 1))
print(divide(2, 7, 9))
print(divide(3, 1, 4))