#comprehension
#iterable - List, Tuple, Set, Dictionary, Range

MyList = [1,2,3,4,5,6,7,8,9,10]

#from LIst
newList = [i+1 for i in MyList]
newDict = {i: i*i for i in MyList}
newSet = {i**3 for i in MyList}
newTuple = tuple(i**4 for i in MyList)
newTlist = [(i, i**2, i**3) for i in MyList]
print("New List: ",newList)
print("New Dictionary: ",newDict)
print("New Set: ",newSet)
print("New Tuple:",newTuple)
print(newList)
print(newTlist)

#from Dictionary
newDict = {"name": "Yeamin","age":24,"address":"Dhaka","position":"Student"}

NewList = [key for key,values in newDict.items()] #get the keys/values from dictionary 
print(NewList)

#put all the letter from a string into a list
stringList = [letter.upper() for letter in "WaterMelon"]
print(stringList)
