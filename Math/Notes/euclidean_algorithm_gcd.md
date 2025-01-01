
# Euclidean Algorithm for GCD

The **Euclidean Algorithm** is an efficient method to find the **Greatest Common Divisor (GCD)** of two numbers.

## Steps
1. If the second number (`b`) is `0`, then the GCD is the first number (`a`).
2. Otherwise, recursively find the GCD of `b` and the remainder of `a % b`.

---

## Algorithm in Python
```python
def gcd(a, b):
    if b == 0:  # Base case
        return a
    return gcd(b, a % b)  # Recursive case

# Example
print(gcd(48, 18))  # Output: 6
```

---

## Example Walkthrough
Find GCD of `48` and `18`:
1. `gcd(48, 18)` → `48 % 18 = 12`, so call `gcd(18, 12)`.
2. `gcd(18, 12)` → `18 % 12 = 6`, so call `gcd(12, 6)`.
3. `gcd(12, 6)` → `12 % 6 = 0`, so GCD is `6`.

---

## Key Points
- Efficient and uses recursion.
- Works for both positive integers.
- Stops when the remainder becomes `0`.
