from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt

dataset = { 1:0.5 , 2:2.5 , 3:2, 4:4, 5:3.5, 6:6, 7:5.5}
keys = list(dataset.keys())
values = list(dataset.values())

#Printing datatable
table1 = PrettyTable(["i", "x", "y", "x^2" , "xy"])
n = len(keys)
count = 1
Σx2 = 0
Σxy = 0
for i in keys:
    table1.add_row([count , i , dataset[i], i**2, i*dataset[i]])
    Σx2 += i**2
    Σxy += i*dataset[i]
    count+=1
table1.add_row(["TOTAL - ", '', '', '', ''])
table1.add_row(['', sum(keys), sum(values), Σx2, Σxy])
table1.title = " Input data "
print()
print(table1)
print()

#Finding slope and intercept
A = np.array( [[n,sum(keys)] , [sum(keys) , Σx2]] )
B = np.array( [sum(values) , Σxy])
X = np.linalg.solve(A,B)
def f(x):
    return X[0] + X[1]*x

#Error analysis
error_sum = 0
for i in keys:
    error_sum += (dataset[i] - f(i))**2
error_y = (error_sum/ (n - 2))**0.5
delta = n*Σx2 - sum(keys)**2
error_slope = error_y * (n/delta)**0.5
error_intercept = error_y * (Σx2/delta)**0.5

#Printing slopes,intercepts and errors
table2 = PrettyTable()
table2.title = "Slope, Intercept and Errors"
table2.add_row(["Slope" , round(X[1],4) ])
table2.add_row(["Intercept" , round(X[0],4) ])
table2.add_row(["Error in y", round(error_y,4) ])
table2.add_row(["Delta" , round(delta,4) ])
table2.add_row(["Error in slope", round(error_slope,4) ])
table2.add_row(["Error in intercept", round(error_intercept,4) ])
print(table2)
print()

#Printing the function values
table3 = PrettyTable(["x" , "y = a_0 + a_1 x"])
table3.title ="Function values"
for i in keys:
    table3.add_row([i, round(f(i),3)])
print(table3)

#Plotting the line 
plt.plot(keys, values, "o", markersize = 4)
x1 = np.array(keys+[0,max([keys[len(keys)-1] , values[len(values)-1]])+2])
f_v = np.vectorize(f)
y1 = f_v(x1)
plt.plot(x1,y1, label = f'Least-square fit line : y = {round(X[1],2)}±{round(error_slope,2)}x + {round(X[0],2)}±{round(error_intercept,2)}')
plt.xlim(0,max([keys[len(keys)-1] , values[len(values)-1]])+1)
plt.ylim(0,max([keys[len(keys)-1] , values[len(values)-1]])+1)
plt.xlabel("x")
plt.ylabel ( "y")
plt.legend()
plt.show()

