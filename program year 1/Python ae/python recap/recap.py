# x = int(input("Enter first number: \n"))
# y = int(input("Enter second number: \n"))
#
# result1 = "x "
#
# if (x % 2 == 0):
#     result1 = "x is even"
# else:
#     result1 = "x is odd"
#
# result2 = "y"
#
# if (y % 2 == 0):
#     result2 = "y is even"
# else:
#     result2 = "y is odd"
#
# result = result1 + " and " + result2
# print(result)



# x = int(input("Enter first number: \n"))
# for i in range(x):
#     result = x * i
#     print(x, "*", i, "=", result)



#Palindrond: 1 so hay 1 chuoi khi dao nguoc lai thi van giong nhu ban dau
num = int(input("Enter second number: \n"))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10  #1   #2  #1
    reverse = (reverse * 10) + remainder  #1  #12
    temp = temp // 10  #12   #1
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")








