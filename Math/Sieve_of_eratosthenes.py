def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    
    p=2
    
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n+1, p):
                is_prime[multiple] = False
        p+=1
    
    prime=[]

    for i in range(len(is_prime)):
        if is_prime[i] == True:
            prime.append(i)
    
    return prime

print(sieve_of_eratosthenes(30))
        
    
                