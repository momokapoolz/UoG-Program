acronyms = {'IP': 'Internet protocol', 'DNS': 'Domain name system', 'RAM': 'Random access memory'}

status = True

def print_acronym():
    for key in acronyms:
        print(key, ':', acronyms[key])

def handle_new(a):
    if a == 'yes':
        acronyms[w] = input('What is the meaning:')
        print_acronym()
    if a == 'no':
        print('ok')


while status:
    w = input("Enter a acronyms: ")
    if w in acronyms:
        print('This acronyms mean: ', acronyms[w])
    elif w == '.':
        print_acronym()
    elif w == 'quit':
        print('ok bye')
        status = False
    else:
        ask = input("This acronyms is not exist. Do you want to add[yes/no]: ")
        handle_new(ask)





