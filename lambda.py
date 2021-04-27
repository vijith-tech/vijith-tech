x = lambda number: number + 20
print(x(20))
print(x(200))
print(x(39))


# lambda 2
x= lambda a, b: a * b
print(x(5,6))

# lambda function
def myfun(n):
    return lambda a: a * n
double = myfun(4)
print(double(20))

def myfun (n):
    return  lambda a: a * n
trouble = myfun(5)
print(trouble(5))

