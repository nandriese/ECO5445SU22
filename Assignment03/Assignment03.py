# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 22:11:54 2022

@author: ni664326
"""
import os

# Module numpy for numerical methods in Python, 
# e.g. to use linear algebra.
import numpy as np
os.getcwd()

#2

A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(A)

#3
# number 7
A[1,2]
#row 1
A[0]
# column 2
A[:,1]
# rows 2 and 3
A[0:2]
#values 7,8,11,and 12
# not sure if there is another way, tried with different syntax but didn't work
A[1,2],A[1,3],A[2,2],A[2,3]

#4
B = 2*A-8
print(B)
#sum row
FirstRowSum = np.sum(B[0])
SecondRowSum = np.sum(B[1])
ThirdRowSum = np.sum(B[2])

FirstRowSum
SecondRowSum
ThirdRowSum
#sum column
FirstColumnSum = np.sum(B[:,0])
SecondColumnSum = np.sum(B[:,1])
ThirdColumnSum = np.sum(B[:,2])
FourthColumnSum = np.sum(B[:,3])

FirstColumnSum
SecondColumnSum
ThirdColumnSum
FourthColumnSum 
#cumulative sum of row values
CumulativeRowSum = (FirstRowSum + SecondRowSum + ThirdRowSum)

CumulativeRowSum
  ##or
np.sum(B)
#cumulative sum of column values
CumulativeColSum = (FirstColumnSum + SecondColumnSum + ThirdColumnSum + FourthColumnSum)

CumulativeColSum
   #or
np.sum(B)

#5
#natural log array
np.log(B)
#square root array
np.sqrt(B)
#square array
np.square(B)
#absolute value array
np.abs(B)

#6

a = np.array([[1,20],[1,-40]])
b = np.array([[286],[88]])
x = np.linalg.solve(a,b)
print(x)
