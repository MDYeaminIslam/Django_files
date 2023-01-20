mylist = ["Nepal","Vutan","India","Bangladesh","England","USA"]
#print(mylist[::2]) #it'll take one gape and print next value
#print(mylist[:4:2]) #last digit is for creating gap and print value
#mylist.append("Uk")
#print(mylist)
#adding new list
mylist.append(["Dhaka","Kolkata"])
mylist.extend(["Khulna","Barisal","Noakhali"])
print(mylist)
mylist.insert(3,"UAE") #first index in index value,than value
print(mylist)
mylist.pop()
print(mylist)