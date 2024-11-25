#Fibbonscci using recursion
fib <- function(n){
  if (n <= 2){
    return (1)
  }
  else{
    return (fib(n-1) + fib(n-2))
  }
}

print(fib(20)) #this solution is complex

#Solution 2
fib2 <- function(n){
  x <- 1
  y <- 1
  for(i in (1:n)){
    z <- x + y
    #print(z)
    x <- y
    y <- z
  }
  return (z)
}

print(fib2(20))

#solution 3:interactive function using vector
fib03 <- function(n){
  result <- c(1,1)
  for (i in (3:n)){
    num <- result[length(result)] + result[length(result) - 1]
    result <- append(result, num)
    print(length(result))
  }
  return (result)
  
}

print(fib03(11))
