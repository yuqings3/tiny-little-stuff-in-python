def lcm(a, b: int) -> int:
    i = a
    while a % b != 0:
        a += i
    return a
print(lcm(int(input()), int(input())))