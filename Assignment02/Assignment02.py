# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 23:04:00 2022
"""
#2

Yo = 2
I = 2.0
Love = 10j
Python = "2 Cool for School"
Mucho = "True"

type(Yo)
type(I)
type(Love)
type(Python)
type(Mucho)

#3
    
A = [Yo, I, Love, Python, Mucho]

#4

B = "I like pie more than cake."

B[:6]
B[7:15]
B[16:25]
B[:6] + B[10:15] + B[20:25]

#5
x = int(input('Enter number for x here: '))
x = "cat"

# Didn't define the function and didn't provide headers, description, or examples (-15)
# Example: 

# def foobar(value: int) -> str:
    # """ 
    # This function takes an integer and applies the following rules: 
    # * If it is a multiple of 3 return the string "foo"
    # * If it is a multiple of 5 return the string "bar"
    # * If it is a multiple of 15 return the string "foobar"
    # * If it does not satisfy any of those, return the string "Not a multiple of 3, 5, or 15"
    # >>> foobar(9)
    # "foo"
    # >>> foobar(10)
    # "bar"
    # >>> foobar(45)
    # "foobar"
    # >>> foobar(19)
    # "Not a multiple of 3, 5, or 15"   
    # """

    
if (x % 15 == 0):
   print("foobar")
elif (x % 5 == 0):
   print("bar")
elif (x % 3 == 0):
    print("foo")
elif (x % 15 != 0):
    print("Not a multiple of 3, 5, or 15")
    
##does division always make something a float? (I believe so)


# No test cases and No catch for non numeric values
# changed line 34 to a string and it breaks (-5)

