### **Recursion Notes**

#### **What is Recursion?**
- **Recursion** is a process where a function calls itself to solve a smaller version of the problem.
- It continues until it reaches a **base case**, which stops further recursive calls.

---

#### **Key Components of Recursion**
1. **Base Case**:  
   The condition where recursion stops. Without it, the function leads to infinite calls.  
   Example: `if n == 0: return 1` (in factorial calculation).

2. **Recursive Case**:  
   The part where the function calls itself to break the problem into smaller pieces.  
   Example: `return n * factorial(n - 1)`.

---

#### **Advantages of Recursion**
- Simplifies solving problems like traversing trees, generating combinations, etc.
- Often leads to clean and intuitive code.

#### **Disadvantages of Recursion**
- Can cause stack overflow if too many calls are made.
- Often less efficient than iterative solutions due to function call overhead.

---

### **Recursion Examples (With Code Snippets)**

#### 1. **Factorial Calculation**  
Recursively multiply `n` with the factorial of `(n-1)` until `n` reaches 0.  
**Code:**  
```python
def factorial(n):
    if n == 0:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

# Example:
print(factorial(5))  # Output: 120
```

---

#### 2. **Fibonacci Sequence**  
Recursively sum the two previous numbers in the sequence.  
**Code:**  
```python
def fibonacci(n):
    if n <= 1:  # Base cases
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Example:
print(fibonacci(6))  # Output: 8
```

---

#### 3. **Sum of Digits**  
Recursively add the last digit (`n % 10`) and call for the rest of the number (`n // 10`).  
**Code:**  
```python
def sum_of_digits(n):
    if n == 0:  # Base case
        return 0
    return n % 10 + sum_of_digits(n // 10)  # Recursive case

# Example:
print(sum_of_digits(1234))  # Output: 10
```

---

#### 4. **Check Palindrome**  
Recursively check if the first and last characters of a string match and continue for the inner substring.  
**Code:**  
```python
def is_palindrome(s):
    if len(s) <= 1:  # Base case
        return True
    if s[0] != s[-1]:  # Check first and last characters
        return False
    return is_palindrome(s[1:-1])  # Recursive case

# Example:
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
```

---

#### 5. **Tower of Hanoi**  
Recursively move `n-1` disks to the auxiliary rod, move the last disk, and then move the remaining `n-1` disks.  
**Code:**  
```python
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:  # Base case
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)  # Step 1
    print(f"Move disk {n} from {source} to {target}")  # Step 2
    tower_of_hanoi(n - 1, auxiliary, target, source)  # Step 3

# Example:
tower_of_hanoi(3, 'A', 'C', 'B')
# Output:
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C
```

---

### **General Tip**
Always start solving recursion problems by identifying:
1. **What is the base case?**
2. **How is the problem reduced in each recursive step?**

