myList = ["apple","banana","orange","mango","grapes","watermelon","pineapple","strawberry","kiwi"]
myList2 = [1,2,3,4,5,6,7,8]
#zip() return tuple value and merge two list
#enumerate() helps to print value with their index value as a tuple

#for index,fruits in enumerate(myList):
    #print(f"{fruits} is at index {index}")
    
for i,j in zip(myList,myList2):
    print(i,j)

for i in sorted(myList):
    print(i)