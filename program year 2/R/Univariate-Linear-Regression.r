data_path = 'E:/table_data.csv'
dat = read.csv(data_path)

fix(dat)

# Data understanding:
# data types, distribution, outlier, linear or non-linear
# Is there any potential outlier

# Detect any potential outlier: IQR (Lec 3. Descriptive Analysis) / Z-score
x = dat$Hydrocarbon.Level
y = dat$Purity

# IQR for x
sorted_x = sort(x)
print(sorted_x)
Q1_x = (sorted_x[5] + sorted_x[6])/2
Q3_x = (sorted_x[15] + sorted_x[16])/2
IQR_x = Q3_x - Q1_x
min_x = Q1_x - 1.5 * IQR_x
max_x = Q3_x + 1.5 * IQR_x

# IQR for y
sorted_y = sort(y)
print(sorted_y)
Q1_y = (sorted_y[5] + sorted_y[6])/2
Q3_y = (sorted_y[15] + sorted_y[16])/2
IQR_y = Q3_y - Q1_y
min_y = Q1_y - 1.5 * IQR_y
max_y = Q3_y + 1.5 * IQR_y

# c2: Data visuliazation
library(ggplot2)
# Plotting a box plot for Purity
ggplot(dat, aes(y = Purity, fill = "Purity")) + 
  geom_boxplot() +
  theme_minimal() +
  ggtitle("Box Plot of Purity") +
  ylab("Purity") +
  scale_fill_manual(values = "beige") +
  theme(legend.position = "none") # hide the legend if not needed

# Remove / Normalize
outlier = subset(dat, dat$Hydrocarbon.Level < min_x | dat$Hydrocarbon.Level > max_x 
                 | dat$Purity < min_y | dat$Purity > max_y)
print(outlier)

clean_data = subset(dat, !dat$Hydrocarbon.Level < min_x | dat$Hydrocarbon.Level > max_x 
                    | dat$Purity < min_y | dat$Purity > max_y)
print(clean_data)

# 2. Data modeling
# Linear Regression Analysis

# Hydrocarbon.Level (x) is an independent varible
x = clean_data$Hydrocarbon.Level
# Purity (y) is a dependent varible
y = clean_data$Purity

plot(y~x)
# Relationship between "Hydrocarbon.Level" & "Purity" is somewhat linear

model = lm(data = clean_data, Purity ~ Hydrocarbon.Level)
print(model)

predicted_value = predict(model, clean_data)
residuals = clean_data$Purity - predicted_value

result = data.frame(clean_data$Hydrocarbon.Level, clean_data$Purity, predicted_value, residuals)

fix(result)

# Plot the linear regresstion model
plot(Purity ~ Hydrocarbon.Level, data = clean_data)
abline(model, col = "orange")

# Evaluation
# Verify the assumption of linerarity
hist(residuals)
lines(density(residuals))

hist(residuals, prob=TRUE, col = "beige", border = "black")
lines(density(residuals))

mean_rs = mean(residuals)
print(mean_rs)
k = 1 # number of independent variables
un_var_epsion = sum((residuals-mean_rs)**2/ length(residuals) - (k + 1))
print(un_var_epsion)

# Plot residuals & predicted values
ggplot(clean_data, aes(x = predicted_value, y = residuals)) + 
  geom_point() +
  geom_hline(yintercept = 0, linetype = "dashed", color = "gold") +
  theme_minimal() +
  xlab("Predicted Values") +
  ylab("Residuals") +
  ggtitle("Residuals & Predicted Values") 

# Evaluate the model: Is the model good enough?
  # R-Square, MAE, MSE, RMSE
MAE = sum(abs(residuals))/length(residuals)
MSE = sum(abs(residuals**2))/length(residuals)
RMSE = sqrt(sum(abs(residuals))/length(residuals))
print(MAE)
print(MSE)
print(RMSE)

mean_y = mean(clean_data$Purity)
R2 = 1 - ( (sum(residuals**2)) / (sum((clean_data$Purity - mean_y)**2)) )
print(R2)