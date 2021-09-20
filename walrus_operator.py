# walrus operator, never used it due to the fact that it was introduced in python 3.8

def someFunc(x):
    return x+ 1

if (x:= someFunc(6)) >=7:
    print(x)

#also fun fact
(y:= someFunc(2))
print(y)
print(x)