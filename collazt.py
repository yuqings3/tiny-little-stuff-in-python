
def collazt(i: int) -> int:
    if i == 1:
        return 1
    elif i % 2 == 0:
        i = i / 2
        return collazt(i)
    else:
        i = 3 * i + 1
        return collazt(i)
print(collazt(int(input())))
