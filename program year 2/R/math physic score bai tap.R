math_score = c(20, 25,8,29,14,11,11,20,17,17)
physic_score = c(30, 35, 21,33,33,26,22,31,33,36)

plot(math_score, physic_score)

r = cor(math_score, physic_score, method = 'pearson')
print(r)





x = c(1, 3, 5, 5, 8)
y = c(5, -2, 2, -1, -3)

plot(y~x)

#correlation coefficient
r = cor(x, y, method = 'pearson')
print(r)

