# fibonacci: if n = 6.  0, 1, 1, 2, 3, 5. sum of last two digit

def fibonacci(n):
    if n <=1: return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))