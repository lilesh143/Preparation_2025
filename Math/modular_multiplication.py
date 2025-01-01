def modular_multiplication(a, b, c):
    a = a % b
    b = b % c
    return ((a*b)%c)

a = 1000000007
b = 2000000003
c = 1000000009

ans = modular_multiplication(a, b, c)
print(f"(a * b) % c = {ans}")