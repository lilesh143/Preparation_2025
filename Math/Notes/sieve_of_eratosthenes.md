# Sieve of Eratosthenes

The **Sieve of Eratosthenes** is an efficient algorithm to find all prime numbers up to a given number `n`. It systematically eliminates non-prime numbers by marking the multiples of each prime.

---

## Algorithm Steps
1. Create a list `is_prime` of size `n + 1` and initialize all elements to `True`.
2. Set `is_prime[0]` and `is_prime[1]` to `False` since `0` and `1` are not prime.
3. Start from `p = 2` (the smallest prime number):
   - If `is_prime[p]` is `True`, mark all multiples of `p` (starting from `p^2`) as `False`.
   - Increment `p` and repeat until `p * p > n`.
4. Collect all indices in `is_prime` that are still `True`—these are the prime numbers.

---

## Code Implementation

```python
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    # Collect all prime numbers without enumerate
    primes = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            primes.append(i)

    return primes

# Example
print(sieve_of_eratosthenes(30))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
