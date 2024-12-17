# fibonacci: if n = 6.  0, 1, 1, 2, 3, 5. sum of last two digit

def fibonacci(n):
    a = 0
    b = 1
    
    count = 2
    
    while(count <= n):
        sum=a+b
        a=b
        b=sum
        count=count+1
    return sum

print(fibonacci(6))