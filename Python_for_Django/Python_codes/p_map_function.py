# map function. It takes two parameter. One is function and another is iterable object
def func(n):
    return n**3

value = [3,4,1,0,6]

#we can give set,tuple,list
newList = list(map(func,value)) #it'll take two parameter
print(newList)

l = ["Yeamin","Daffodil","Dhakaa"]
list2 = list(map(list,l)) #here we will give only function name not with () brackets
print(list2)