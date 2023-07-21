#Program to find root of a function using secant method.

def f(x): #function whose roots have to be found out.
    return x**3 - 7*x**2 +14*x -8


def find_root(f,x_1,x_2, tolerance):
    #The function returns only one root of f. For other roots, try chaanging x_1 and x_2.
    x_n = x_1
    x_n1 = x_2
    x_n2 = x_n1 - ( f(x_n1)*(x_n1 - x_n) / (f(x_n1) - f(x_n)) )
    while abs(x_n2 - x_n1) > tolerance:
        #print(x_n2)
        x_n = x_n1
        x_n1 = x_n2
        x_n2 = x_n1 - ( f(x_n1)*(x_n1 - x_n) / (f(x_n1) - f(x_n)) )
    return x_n2

print(find_root(f,4,10,10**-3))
