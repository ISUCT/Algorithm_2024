import math

def calculate(x):
    return (((math.asin(x))**2 + (math.acos(x))**4)**3)

def taskone(x_s,x_e,x_k):
    results=[]
    while x_s < x_e:
        results.append(calculate(x_s))
        x_s+=x_k
    return results

def tasktwo(x1,x2,x3,x4,x5):
    results2=[]
    for a in x1,x2,x3,x4,x5:
        results2.append(calculate(a))
    return results2


