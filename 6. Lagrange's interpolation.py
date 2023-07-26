#The program takes input a dataset as a dictionary and finds out a polynomial that fits all data points and prints the value of that polynomial for certain x.

dataset = { 1:1 , 2:1.4142 , 3:1.7321 , 4:2} #We input data for finding square root of numbers.

def interpolate(x):
    #The function returns the value of interpolation polynomial at x.
    global dataset
    out = 0
    for k in dataset.keys():
        term = dataset[k]
        for i in dataset.keys():
            if i!=k:
                term = term*(x - i)/(k - i)
        out += term
    return out


print(interpolate( 2.5)) #returns an approximate value for sqrt(2.5).

#plotting the function
import matplotlib.pyplot as plt
import numpy as np

keys = list(dataset.keys())
values = list(dataset.values())
plt.plot(keys,values, "o", markersize = "4")

X = np.arange(-20,20.1,0.1)
interpolate_v = np.vectorize(interpolate)
Y = interpolate_v(X)
plt.plot(X,Y)
plt.show()