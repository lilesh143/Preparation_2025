def gcd1(a, b):
    if b == 0:
        return a
    return gcd1(b, a % b)

def gcd2(a, b):
    if a ==  0:
        return b
    return gcd2(b % a, a)

def lcm(a, b):
    return a * b // gcd1(a, b)

if __name__ == "__main__":
    a =  12
    b = 15
    print("gcd using method1 ", gcd1(a, b))
    print("gcd using method2 ", gcd2(a, b))
    print("lcm using euclid formula", lcm(a, b))
