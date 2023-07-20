# This method is used to find roots of a function f(x) in an interval (a,b), wher f(x) is continuous.
#In case, there are more than one roots of f in (a,b), the function will return only one. Adjust the interval accordingly to get other roots.

from math import exp

def f(x):
    #roots of f(x) will be found out.
    return 4*x - exp(x)

def find_root(f,a,b,tolerance):
    #f is the function and (a,b) is the interval.
    #tolerence is the maximum acceptable absolute error.
    if abs(b-a)<tolerance:
        if f(a)==0:
            return a
        if f(b)==0:
            return b
        if f(a)*f(b)<0:
            return (a+b)/2
        if f(a)*f(b)>0:
            return None
    
    elif f(a)*f(b)>0:
        mid = (a+b)/2
        left = find_root(f,a,mid,tolerance)
        right = find_root(f,mid,b,tolerance)
        if left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None
        
    else:
        mid = (a+b)/2
        if f(mid)==0:
            return mid
        elif f(a)*f(mid)<0:
            return find_root(f,a,mid,tolerance)
        else:
            return find_root(f,mid,b,tolerance)
        

root = find_root(f,0,10,10**-3)
if root is None:
    print(f'The function has no roots in the given interval.')
else:
    print(f'{root} is a root of the function.')
        
