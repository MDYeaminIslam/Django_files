#Comprehension
#iterable -> List, Tuple, Set, Dictionary, Set, Range
#create -> List, Dictionary, Set

MyList = [1,2,3,4,5,6,7,8,9,10]

newList = [i+1 for i in MyList]
newDict = {i: i*i for i in MyList}
newSet = {i**3 for i in MyList}
newTuple = tuple(i**4 for i in MyList)
print("New List: ",newList)
print("New Dictionary: ",newDict)
print("New Set: ",newSet)
print("New Tuple:",newTuple)