mylist = ["Nepal","Vutan","India","Bangladesh","England","USA","canada"]
mylist2 = ["Nepal","Vutan","India","Bangladesh","England","USA"]
mylist.sort(key=str.lower, reverse=False) #sorted according to first letter ascii value
mylist2.sort(reverse=True)
print(mylist)
print(mylist2)