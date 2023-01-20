# map function.

def func(n):
    return n*n*n

value = [3,4,1,0,6]

#we can give set,tuple,list
newList = list(map(func,value)) #it'll take two parameter
print(newList)

l = ["Yeamin","Daffodil","Dhakaa"]
list2 = list(map(list,l)) #here we will give only fucntion name not with () brackets
print(list2)