#Comprehension
#make a list of squares normal/old way
myList = [1,2,6,3,5,8]
newList = []

for i in myList:
    newList.append(i*i)

print(newList)

#do the same thing in the comprehension way
comlist = [i*i for i in myList if i%2==0]
print(comlist)
