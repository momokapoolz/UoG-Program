def isPrime(n):
    if n <= 1 :
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_prime(n, m):
    count = 0
    for i in range(2, n + 1):
        if isPrime(i):
            print(i, end = " ")
            count += 1
            if count == m:
                print()




n = int(input('enter n: '))
m = int(input('how many rows? '))
print_prime(n, m)