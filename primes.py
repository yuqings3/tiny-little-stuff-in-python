def primes(input_integer: int):
    if input_integer <= 1:
        print(None)
        
    prime_or_not = [True for i in range(0, input_integer + 1)]
    p = 2

    while (p <= input_integer):
        if prime_or_not[p] == True:
            for i in range(p * p, input_integer + 1, p):
                prime_or_not[i] = False
        p += 1

    output = []
    for num in range(2, input_integer + 1):
        if prime_or_not[num] == True:
            output.append(num)
    print(output)

primes(int(input()))