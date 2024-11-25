import random as rd
numbers = [rd.randint(1, 100) for i in range(10)]
print(numbers)

first_digits = [n // 10 for n in numbers]
print(first_digits)

negative = [0 - n for n in numbers]
print(negative)


names = ["hakos baezl", "ouro kronii", "mori calliope"]
first_name = [n.split()[0] for n in names]
print(first_name)

