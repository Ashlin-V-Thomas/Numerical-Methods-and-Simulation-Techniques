#The program takes input a dataset as a dictionary and finds out a polynomial that fits all data points and prints the value of that polynomial for certain x.

dataset = { 1:1 , 2:1.4142 , 3:1.7321 , 4:2} #We input data for finding square root of numbers.

def interpolate(dataset,x):
    #The function returns the value of interpolation polynomial at x.
    out = 0
    for k in dataset.keys():
        term = dataset[k]
        for i in dataset.keys():
            if i!=k:
                term = term*(x - i)/(k - i)
        out += term
    return out


print(interpolate(dataset, 2.5)) #returns an approximate value for sqrt(2.5).