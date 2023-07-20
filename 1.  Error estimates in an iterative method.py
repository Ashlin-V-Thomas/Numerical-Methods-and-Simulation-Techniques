#A python program that finds exp(n) by iterating using the taylor series expansion of exp(x) until the approximate relative error falls below certain value.
#It displays the values and errors in each iteration.

import math
from prettytable import PrettyTable

def expo(x, allowed_error):
    table1 = PrettyTable(["Number of iteration", "Value of function", "Fractional relative error", "Approxiamte relative error"])
    approx_rel_error = 1000
    n = 0
    prev_funcn_val = 0
    funcn_val = 0
    frac_rel_error = 0
    true_value = math.exp(x)
    while approx_rel_error>= allowed_error : 
        prev_funcn_val = funcn_val
        funcn_val += x**n/math.factorial(n)
        frac_rel_error = (true_value - funcn_val)*100/true_value
        if n==0:
            table1.add_row([n+1,funcn_val,frac_rel_error, "-"])
            n+=1
        else:
            approx_rel_error = (funcn_val - prev_funcn_val)*100/funcn_val
            table1.add_row([n+1,funcn_val,frac_rel_error, approx_rel_error])
            n+=1
    print(table1)

    

expo(0.5, 0.05)