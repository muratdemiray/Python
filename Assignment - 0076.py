# C7212-Murat

def prime(n):
    for i in range(2,n-1):
        if i != n and n%i == 0:
            return False      
    return n


number = int(input("Write a number: "))

primes = []

for p in range(2,number):
    if prime(p) != False:
        primes.append(p)

print(primes)

