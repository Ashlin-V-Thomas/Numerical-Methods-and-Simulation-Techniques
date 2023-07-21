# This method is used to find roots of a function f(x) in an interval [a,b], wher f(x) is continuous.

from math import sin

def f(x):
    #roots of f(x) will be found out.
    return sin(x)

def find_root(f,a,b,tolerance):
    #f is the function and [a,b] is the interval.
    #tolerence is the maximum acceptable absolute error.
    #In case, there are more than one roots of f in [a,b], the function will return only one. 
    
    if f(a)==0:
        return a
    
    if f(b)==0:
        return b
    
    if abs(b-a)<tolerance:
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

roots = []
def find_all_roots(f,a,b,tolerance):
    #This function finds all roots in the interval by adjusting the intervals after each root is found out.
    global roots
    root = find_root(f,a,b,tolerance)
    if root is None:
        return
    else:
        roots.append(root)
        if root==a:
            find_all_roots(f,a+tolerance,b,tolerance)
        else:
            find_all_roots(f,a,root-tolerance,tolerance)
        if root ==b:
            find_all_roots(f,a,b-tolerance,tolerance)
        else:
            find_all_roots(f,root+tolerance,b,tolerance)

find_all_roots(f,-10,10,10**-3)
new_roots = []
for i in sorted(roots): 
    if i not in new_roots: #to avoid repetiton and to sort
        new_roots.append(i)

if len(new_roots)==0:
    print(f'The function has no roots in the given interval.')
else:
    print(f'{new_roots} are the roots of the function in the given interval.')
        
