datammb = read.csv("C:/Users/Admin/Downloads/income.data.csv")
fix(datammb)


#plot mqh giua happiness va income
plot(happiness~income, data=datammb)


lmodel <- lm(happiness~income, data=datammb)
print(lmodel)


plot(happiness~income, data=datammb)
abline(lmodel, col="red")


#chia tap du lieu thanh 80/20: 80 de train data, 20 de test
dat = read.csv("C:/Users/Admin/Downloads/income.data.csv")
set.seed(100)
trainingRowIndex <- sample(1:nrow(dat), 0.8*(nrow(dat)))

trainingData <- dat[trainingRowIndex, ] # 80 data de train
testData <- dat[-trainingRowIndex, ]# 20 data con lai de test



#xay dung mo hinh

lmodel <- lm(happiness~income, data=trainingData)
print(lmodel)

#plot model data len bieu do
plot(happiness~income, data=trainingData)
abline(lmodel, col="red")