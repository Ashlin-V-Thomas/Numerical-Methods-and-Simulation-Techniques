#Program to find the root of a function using secant method.

def f(x): #function whose roots have to be found out.
    return x**2 -5*x +6


def find_root(f,x_1,x_2, tolerance):
    #The function returns only one root of f. For other roots, try changing x_1 and x_2.
    x_n = x_1
    x_n1 = x_2
    if f(x_n)==f(x_n1):
        print(" Try a different choice of x_1 and x_2.")
        return None
    x_n2 = x_n1 - ( f(x_n1)*(x_n1 - x_n) / (f(x_n1) - f(x_n)) )
    while abs(x_n2 - x_n1) > tolerance:
        x_n = x_n1
        x_n1 = x_n2
        if f(x_n)==f(x_n1):
            print(" Try a different choice of x_1 and x_2.")
            return None
        else:
            x_n2 = x_n1 - ( f(x_n1)*(x_n1 - x_n) / (f(x_n1) - f(x_n)) )
    if int(f(x_n2)*100) == 0:
        return x_n2
    else:
        print("Try reducing the tolerance.")
        return

root = find_root(f,0,10,10**-3)
if root is not None:
    print(root , "is the root of the function.")

