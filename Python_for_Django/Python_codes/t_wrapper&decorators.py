#Wrapper Functions and Decorators

#another new higher order function
"""def myfunc():
    def hello():
        print("I am hello function from myfunc().")
        
    return hello
value = myfunc() #here value also holding a function
value()"""

#wrapper
def myWrapper(fn):
    def test():
        print("I am from test! Before")
        fn()
        print("I am from test! After")
        
    return test
@myWrapper #this is decorator and it is easy the task of set a variable than call the function and this is same as #hello = myWrapper(greet) calling
def greet():
    print("This is from greeting function")
    
def hello():
    print("This is from hello function")

#hello = myWrapper(greet)
#hello()
greet()
hello()