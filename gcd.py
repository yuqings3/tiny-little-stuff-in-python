def gcd(a, b):
    if a < b:
        i = a
        a = b
        b = i
    if a % b == 0:
        return b
    else:
        return gcd(a, a % b)
print(gcd(int(input()), int(input())))
