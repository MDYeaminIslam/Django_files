#looping
#for i in tuple,list,dictionary,range,set
#creating a list of tuple
myTuple = ("a","b","c","d","e")

myList = [("a",1,"BDT"),("b",2,"USD"),("c",3,"INR"),("d",4,"CAD")]
for x,y,z in myList:
    print(f"{x},{y},{z}")


myDict = {"Name":"Md. Yeamin Islam","Age":24,"Country":"Bangladesh"}

for key,value in myDict.items():
    print(f"{key}=>{value}")


#looping using range
for i in range(2,51,2):
    print(i)