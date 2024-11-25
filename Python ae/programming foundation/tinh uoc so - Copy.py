n = int(input('enter n: '))
i = 2
c = 0
while i < n:
    if n % i == 0:
        c += 1
    i += 1
print('total ', c)




