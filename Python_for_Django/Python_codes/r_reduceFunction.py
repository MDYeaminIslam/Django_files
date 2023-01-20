#reduce function 
#we can find out fibonacci series using reduce function
from functools import reduce
List = [1,2,3,4,5,2,6]
#taking two parameter
def func(x,y):
    return x + y

sum = reduce(func,List) #take first two value than add ,take next value add to previous value and continue till last value
print(sum)
    