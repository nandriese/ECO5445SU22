# Future submissions, please submit Rmd files

#2, repeat question 2 and 5 from assignment 02

a <- (2) # if it is one value, you do not need quotes
b <- (2.0)
c <- ("10j") # Did you try without the quotes?
d <- ("2 Cool for School")
e <- ("True") # Did you try without the quotes?

class(a)
class(b)
class(c)
class(d)
class(e)


x <- as.numeric(x)
FoobarFunction <- function(x) {
  # """ 
  # This function takes an integer and applies the following rules: 
  # * If it is a multiple of 3 return the string "foo"
  # * If it is a multiple of 5 return the string "bar"
  # * If it is a multiple of 15 return the string "foobar"
  # * If it does not satisfy any of those, return the string "Not a multiple of 3, 5, or 15"
  # * If a character is entered, it will return the string "Non-numeric, not a multiple of 3, 5, or 15"
  #>>> FoobarFunction(9)
  # "foo"
  # >>> FoobarFunction(10)
  # "bar"
  # >>> FoobarFunction(45)
  # "foobar"
  # >>> FoobarFunction(19)
  # "Not a multiple of 3, 5, or 15" 
  # >>> FoobarFunction("hi")
  # Not a multiple of 3, 5, or 15"
  
  if(class(x)!= 'numeric') {
    print("Not a multiple of 3, 5, or 15")
  }else if(x %% 15 == 0){
    print("foobar")
  }else if(x %% 5 == 0) {
    print("foo")
  }else if(x %% 3 == 0) {
    print("bar")
  }else if(x %% 15 != 0) {
    print("Not a multiple of 3, 5, or 15")
    
  }
}
  
FoobarFunction(45)
# Only ran one test (-1)

# 3
attach(swiss)

#4
summary(swiss)
# missing spread of data (sd or variance) (-5)

#5
agrSwiss <- swiss$Agriculture
maxAg <- max(agrSwiss)
maxAgProvince <- which(agrSwiss == (maxAg))
print(row.names(swiss[maxAgProvince,])) ## you needed to reference the dataframe again. rowname(33) provides nothing. (-5)

#6
cor(swiss)

#7
plot(swiss$Education, swiss$Fertility, main = "Relationship between Education and Fertility", xlab = "Education", ylab = "Fertility")

#7
hist(swiss$Catholic, main = "Swiss Catholic Prevalence", xlab = "Percent Catholic", ylab = "Number of Provinces")
