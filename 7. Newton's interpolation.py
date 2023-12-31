#The program takes input a dataset as a dictionary and finds out a polynomial that fits all data points(except the last) and prints the value of that polynomial for certain x.

dataset = { 1:0 , 2:0.3010, 3:0.4771,  4:0.6021 } #We input the dataset given by the function f(x) = logx
keys = list(dataset.keys())

def div_diff(inlist):
    #Function to find divided difference.
    global dataset
    if len(inlist) == 1:
        return dataset[inlist[0]]
    else:
        n = len(inlist) - 1
        return (div_diff(inlist[1:]) - div_diff(inlist[:n]))/( inlist[n] - inlist[0])
    
def interpolate_coefficients():
    #The function returns the list of coefficients of interpolation polynomial at x.
    global keys, dataset
    out = [dataset[keys[0]]]
    for k in range(1,len(keys)):
        out.append(div_diff(keys[:k+1]))
    return out

coefficients = interpolate_coefficients()

def interpolate(x):
    global coefficients,dataset
    out = coefficients[0]
    for k in range(1,len(coefficients)):
        term = coefficients[k]
        for i in range(0,k):
            term = term*(x - keys[i])
        out += term
    return out
    

print(interpolate(2.5)) #returns an approximate value of log(2.5)
        

#plotting the function
import matplotlib.pyplot as plt
import numpy as np

values = list(dataset.values())
plt.plot(keys,values, "o", markersize = 4)

X = np.arange(-10,10.1,0.1)
interpolate_v = np.vectorize(interpolate)
Y = interpolate_v(X)
plt.plot(X,Y)
plt.show()

