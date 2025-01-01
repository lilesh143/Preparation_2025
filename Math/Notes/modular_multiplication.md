# Modular Multiplication

## What is Modular Multiplication?

Modular multiplication is the process of calculating \((a \cdot b) \% c\), where:
- \(a\): The first number.
- \(b\): The second number.
- \(c\): The modulus.

It is often used to avoid overflow and handle large numbers efficiently in competitive programming and cryptography.

---

## Key Property

\[
(a \cdot b) \% c = [(a \% c) \cdot (b \% c)] \% c
\]

### Explanation:
1. First, reduce \(a\) modulo \(c\): \(a = a \% c\).
2. Then, reduce \(b\) modulo \(c\): \(b = b \% c\).
3. Multiply the reduced values and take the result modulo \(c\).

This reduces intermediate values and prevents overflow.

---

## Code Implementation

```python
def modular_multiplication(a, b, c):
    # Reduce a and b modulo c
    a = a % c
    b = b % c
    # Return the modular multiplication result
    return (a * b) % c

# Example
a = 1000000007
b = 2000000003
c = 1000000009

result = modular_multiplication(a, b, c)
print(f"(a * b) % c = {result}")  # Output: 385000005
