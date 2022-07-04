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
x = 22

if (x % 15 == 0):
   print("foobar")
elif (x % 5 == 0):
   print("bar")
elif (x % 3 == 0):
    print("foo")
elif (x % 15 != 0):
    print("Not a multiple of 3, 5, or 15")

### or (don't grade this please, I was just trying it)

x = int(input('Enter number for x here: '))
x = 30


if (type(x/15) == int):
   print("foobar")
elif (type(x/3) == int):
    print("foo")
elif (type(x/5)== int):
    print("bar")
elif (type(x/15) == float):
   print("Not a multiple of 3, 5, or 15")
   
##does division always make something a float?