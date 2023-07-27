#A program for finding derivatives numerically.
import numpy as np
from math import exp
import sys

n = 10 #We will neglect terms of the order h^(n). n must be 1 or an even positive integer.
a1 = 1 

if n>2:
    A = []
    for i in range(3,2*n+1,2):
        temp = []
        for j in range(2,n+1):
            temp.append(j**i)
        A.append(temp)
    B = [-a1 for i in range(0,n-1)]

    A_n = np.array(A) #coefficient matrix
    B_n = np.array(B) #constant matrix
    X_n = np.linalg.solve(A_n,B_n) #solution
    X = list(reversed(list(-1*X_n))) + [-a1,a1] + list(X_n) #Total solution

def f(x):
    return x**4 -5*x**2 + 10*x


def derivative(f,x,h):
    if n!=1 and n%2!=0:
        print("n must be 1 or an even positive integer.")
        return
    
    if n==1:
        return (f(x+h) - f(x))/h
    if n==2:
        num=f(x+h) - f(x-h)
        den =2*h
        return num/den
    
    global X
    numerator = 0
    denominator = 0
    for k in range(-n,n+1):
        if k<0:
            numerator += X[k+n]*f(x + k*h)
            denominator += k*X[k+n]
        elif k>0:
            numerator += X[k+n-1]*f(x + k*h)
            denominator += k*X[k+n-1]
    denominator = denominator*h
    return numerator/denominator

def sign(x):
    if x<0: 
        return -1
    if x==0:
        return 0
    if x>0:
        return 1
    

error = 0
def accurate_derivative(f,x,tolerance,left = 1, right = 0.1): #If the derivative at a point is so large, increase tolerance or else recursion depth will exceed. all the best!!!
    global error
    left_val = derivative(f,x,left)
    right_val = derivative(f,x,right)
    error1 = right_val - left_val
    if abs(error1)<tolerance:
        return right_val
    else:
        if sign(error1)==sign(error) or error==0:
            error = error1
            return accurate_derivative(f,x,tolerance,right,2*right)
        if sign(error1)!=sign(error) and error!=0:
            return accurate_derivative(f,x,tolerance,left,right/4)


    


print(accurate_derivative(f,5,10**-9))
