import random
def schulte():
    schulte = list(random.sample(range(1, 26), 25))
    return [schulte[i: i + 5] for i in range(0, 25, 5)]
print(schulte())