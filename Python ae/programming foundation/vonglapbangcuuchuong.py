ques = 'y'
while ques == 'y' or ques =='yes':
    n = int(input('enter n: '))
    for i in range(1, n+1):
        print(n,'*',i, '=', n*i)
    ques = input('again[y/n]? ')


        








