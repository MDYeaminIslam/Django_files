#lamda function/Anonymous function.It has only single expression but hav multiple value
def add(x,y):
    return x+y

result = lambda x,y: x+y
print(result(10,12))
#another way to present lambda function
print((lambda a,b:a*b)(10,9))