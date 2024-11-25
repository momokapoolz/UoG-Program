pmf = dbinom(4, size = 6, prob = 1/10) 

## 1/10 la sucess, hoi 4 cai bat ky tren 6 cai la success ##

pmf00 = dbinom(0, size = 6, prob = 1/10)
pmf01 = dbinom(1, size = 6, prob = 1/10)
pmf02 = dbinom(2, size = 6, prob = 1/10)
pmf03 = dbinom(3, size = 6, prob = 1/10)

r1 = pmf00 + pmf01 + pmf02 + pmf03

print(r1)

## sac xuat cuoc goi ban la 1/10, neu goi 4 cuoc tren 6 cuoc thi xac xuat cuoc goi ban la bnh?



m <- c(9, 10, 7, 8, 9, 6, 5, 9, 4, 7, 1, 7, 2, 7, 8, 5, 4, 3, 10, 7, 3, 7, 8, 6, 9, 7, 4, 2, 3, 9, 4, 3, 7, 5, 5, 2, 7, 9, 7, 1)
print(m)


f <- c(0,0,0,0,0,0,0,0,0,0)



for (i in m){
  if (i == 1){
    f[1] = f[1] + 1
  }
  if (i == 2){
    f[2] = f[2] + 1
  }
  if (i == 3){
    f[3] = f[3] + 1
  }
  if (i == 4){
    f[4] = f[4] + 1
  }
  if (i == 5){
    f[5] = f[5] + 1
  }
  if (i == 6){
    f[6] = f[6] + 1
  }
  if (i == 7){
    f[7] = f[7] + 1
  }
  if (i == 8){
    f[8] = f[8] + 1
  }
  if (i == 9){
    f[9] = f[9] + 1
  }
  if (i == 10){
    f[10] = f[10] + 1
  }
}

print(f)






input <- c(9, 10, 7, 8, 9, 6, 5, 9, 4, 7, 1, 7, 2, 7, 8, 5, 4, 3, 10, 7, 3, 7, 8, 6, 9, 7, 4, 2, 3, 9, 4, 3, 7, 5, 5, 2, 7, 9, 7, 1)

freq = table(input)

print(freq)

barplot(freq)



a <- sum(9, 10, 7, 8, 9, 6, 5, 9, 4, 7, 1, 7, 2, 7, 8, 5, 4, 3, 10, 7, 3, 7, 8, 6, 9, 7, 4, 2, 3, 9, 4, 3, 7, 5, 5, 2, 7, 9, 7, 1)
print(a)

b <- a / 40
print(b)



cau2 <- c(266, 231,  223, 262, 260, 230, 191, 182, 165, 153)
max(cau2) - min(cau2)

cau2sort <- sort(cau2)

q2 = (cau2sort[5] + cau2sort[6]) / 2
q1 = cau2sort[3]
q3 = cau2sort[8]
interquartile_range = q3 - q1
print(interquartile_range)




pa = pnom(o.75, mean = 0)





  