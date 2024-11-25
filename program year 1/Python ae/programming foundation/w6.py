import random
rock = 1
scissor = 2
paper = 3
def enter_balance():
    user_balance = int(input('Please enter your balance: '))
    while user_balance < 10 or user_balance > 100:
        user_balance = int(input('Please enter your balance: '))
    return user_balance
    
def random_rsp():
    rd = random.randint(1, 3)
    if rd == 1:
        return rock
    if rd == scissor:
        return scissor
    if rd == paper:
        return paper

def get_rsp():
    ask_user = input('rock/paper/scissor: ')
    if ask_user == 'rock':
        ask_user = rock
    if ask_user == 'scissor':
        ask_user = scissor
    if ask_user == 'paper':
        ask_user = paper
    return ask_user

def compare_result(comp_choice, user_choice, result):
    comp_choice = get_rsp()
    user_choice = random_rsp()
    if comp_choice == user_choice:
        result = "tie"
    elif user_choice == rock:
        if comp_choice == paper: 
            result = "lose"
        elif comp_choice == scissor: 
            result = "win"
    elif user_choice == paper:
        if comp_choice == rock: 
            result = "win"
        elif comp_choice == scissor:
            result = "lose"
    elif user_choice == scissor:
        if comp_choice == rock:
            result = "lose"
        elif comp_choice == paper: 
            result = "win"
    print('result is: ', result)
    return result

def is_continue(b):
    ask = input('Do you want to play again?: [yes/no]')
    if ask == 'yes':
        return True
    if ask == 'no':
        return False

def update_balance(result, balance):
    if result in ("win"):
        balance += 1
    
    elif result in ("lose"):
        balance += -1
    
    elif result in ("tie"):
        balance += 0
    print('Your new balance:', balance)
    return balance

#### MAIN PROGRAM ####

playing = True
while playing:
    balance = enter_balance()
    comp_choice = random_rsp()
    user_choice = get_rsp()
    result = compare_result(comp_choice, user_choice)
    balance = update_balance(result, balance)
    playing = is_continue()




