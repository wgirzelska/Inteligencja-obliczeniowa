# a)

def checkPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

def prime(n):
    if checkPrime(n):
        print("Wynik: " + str(True))
    else:
        print("Wynik: " + str(False))

prime(3)
prime(4)
prime(49)

# b)

def select_primes(x):
    primesList = []
    for i in range(0, len(x)):
        if checkPrime(x[i]):
            primesList.append(x[i])
    print("Liczby pierwsze: " + str(primesList))

select_primes([1,3,5,8])