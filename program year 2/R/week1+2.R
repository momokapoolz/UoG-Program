x <- 12
y <- 7
print(x%%y)
print(x%/%y)
print(x/y)


name = "MikiNyan"
myFunction <- function(){
  name <- "Momokapool"
  print(name)
}

myFunction()
print(name)


mark <- 7.5
group <- function(mark){
  if (mark >= 8){
    print("Excellent")
  } else if (mark < 8 && mark > 6.5){
    print("Good")
  } else if (mark < 6.5 && mark >= 4){
    print("Acceptable")
  } else{
    print("Fail")
  }
}
group(mark)

vector <- c(123, 456, 246) #in a vector cannot store different data types
for (x in vector){
  print(x)
}

newNumber = sort(x = vector, decreasing = FALSE)
print(newNumber)