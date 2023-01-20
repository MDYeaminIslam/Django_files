#higher order function
"""def hof(fn):
    print(fn.__name__) #this will print the name of the function
    fn()
    
def greet():
    print("Hello World")

def hello():
    print("Hello Bohubrihi")

hof(hello) #here we are passing function as a parameter and we don't need to give () after function name

#doing the filter function and this is build in function"""

li = [1,2,3,4,5,6,7,8,9,10]

def myFilter(fun,li):
    newL = [] #create a new empty list
    for i in li:
        if fun(i):
            newL.append(i)
    return newL

newList = list(myFilter(lambda x:x%2==0,li))
print(newList)