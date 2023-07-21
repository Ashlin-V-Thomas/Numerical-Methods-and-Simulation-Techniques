#Program to find the root of a function using Newton-Raphson method.

from math import exp

def f(x): #function whose roots have to be found out.
    return exp(-x) - 5*x

def d_f(x): #derivative of f(x)
    return -1*exp(-x) - 5

def find_root(f,d_f,x_1,tolerance):
    x_n1 = x_1
    if d_f(x_n1)==0:
        print("Change the choice of x_1.")
        return
    else:
        x_n2 = x_1 - f(x_1)/ d_f(x_1)
    while abs((x_n2 - x_n1))>=tolerance:
        x_n1 = x_n2
        if d_f(x_n1)==0:
            print("Change the choice of x_1.")
            return
        else:
            x_n2 = x_n1 - f(x_n1)/ d_f(x_n1)
    
    if int(f(x_n2)*100) == 0:
        return x_n2
    else:
        print("Try reducing the tolerance.")
        return
    
root = find_root(f,d_f,7,10**-3)
if root is not None:
    print(root , "is the root of the function.")