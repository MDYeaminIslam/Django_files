#dictionary
#key _ value pair
newDict = {"k1":"Yeamin","k2":"Islam","k3":24}
print(newDict)
newDict["k4"] = "Jamalpur"
print(newDict)
del newDict["k3"]
print(newDict)

#creating new dictionary using dict() constructor
value = dict(key1 = "Md",key2 = "Yeamin",key3 = "Islam")
print(value)

#creating new dictionary using zip() function
value2 = dict(zip(["k1","k2","k3"],["Apple","Banana","Orange"])) #first [] indicates key and second [] indicates values
print(value2)

#creating new dictionary where we'll pass tuple
value3 = dict([("k1","Treee"),("k2","Animal")])
print(value3)
print(value3.pop("k2"))

#list value will contain key value of dictionary