import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

dataset = { 0:2.1, 1:7.7, 2:13.6 , 3:27.2, 4:40.9, 5:61.1}
m = 2 #degree of polynomial
keys = list(dataset.keys())
values = list(dataset.values())

power_sums = [len(keys)] 
for i in range(1,2*m+1):
    element = 0
    for j in keys:
        element += j**i
    power_sums.append(element)

a = [] #coefficient matrix as 2-d list
for i in range(0,m+1):
    a.append(power_sums[i:i+m+1])
print()

b = [] #constants list
for i in range(0,m+1):
    term = 0
    for j in keys:
        term += dataset[j]*j**i
    b.append(term)

A = np.array(a)
B = np.array(b)
X = np.linalg.solve(A,B) #solving

table1 = PrettyTable()
table1.title = "Coefficients"
for i in range(0,m+1):
    table1.add_row([f'a{i}' , round(X[i],4)])
print(table1)
print()

def f(x):
    out = 0
    for i in range(0,m+1):
        out += X[i]*x**i
    return out

#Error analysis
Sr = 0
for i in keys:
    Sr += (dataset[i] - f(i))**2
Ss = (Sr / ( len(keys) - (m+1)))**0.5
mean_y = sum(values)/len(keys)
Sy = 0
for i in values:
    Sy += ( i - mean_y)**2
r2 = (Sy - Sr)/Sy
table2 = PrettyTable()
table2.title = "Error Analysis"
table2.add_row(["S_r" , Sr])
table2.add_row(["Standard deviation(S_s)" , Ss])
table2.add_row(["r^2" , r2])
print(table2)

#plotting
plt.plot(keys, values, "o", markersize = 4)
x1 = np.arange(keys[0], keys[len(keys)-1]+0.1,0.1)
f_v = np.vectorize(f)
y1 = f_v(x1)

plt.plot(x1,y1)
plt.show()

