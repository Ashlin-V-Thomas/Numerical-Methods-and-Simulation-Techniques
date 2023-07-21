#Inputting the degree and coefficients of polynomial
n = int(input("Enter the degree of the polynomial = "))
a = list(range(0,n+1))
for i in reversed(a):
    temp = float(input(f'Enter a{i} = '))
    a[i] = temp

def p(x): #polynomial function
    global a
    global n
    out = 0
    for i in range(0,len(a)):
        out += a[i]*x**i
    return out

x_max = n*max([abs(a[i])/abs(a[n]) for i in range(0,len(a))]+[1])

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

find_all_roots(p,-x_max,x_max,10**-3)
new_roots = []
for i in sorted(roots): 
    if i not in new_roots: #to avoid repetiton and to sort
        new_roots.append(i)

if len(new_roots)==0:
    print(f'The polynomial has no real roots.')
else:
    print(f'{new_roots} are the real roots of the polynomial.')