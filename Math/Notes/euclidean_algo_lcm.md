# Euclidean Algorithm for LCM

The **Least Common Multiple (LCM)** of two numbers is the smallest positive integer that is divisible by both numbers.

## Formula
The relationship between **GCD** and **LCM** is:
\[ LCM(a, b) = \frac{a \times b}{GCD(a, b)} \]

This means we can calculate the LCM of two numbers if we know their GCD.

---

## Steps to Calculate LCM
1. Find the GCD of the two numbers using the **Euclidean Algorithm**.
2. Use the formula:
   \[ LCM(a, b) = \frac{a \times b}{GCD(a, b)} \]
   to compute the LCM.

---

## Algorithm in Python
```python
def gcd(a, b):
    if b == 0:  # Base case
        return a
    return gcd(b, a % b)  # Recursive case

def lcm(a, b):
    return (a * b) // gcd(a, b)  # Formula for LCM

# Example
print(lcm(12, 15))  # Output: 60
