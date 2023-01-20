# filter function always return True or False

listValue = [1,3,4,6,88,4,2,9,5]

#here n is the amount of listValue
def func(n):
    return n%2==1 #here n will return True or false value and filter function also work where only they get True value

newList = list(filter(func,listValue))
print(newList)