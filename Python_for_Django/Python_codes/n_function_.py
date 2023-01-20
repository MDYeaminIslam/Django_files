#this are the parameters
#def name(fname, lname):
    #print(f"Full Name: {fname} {lname}")
    
#name("Md.Yeamin","Islam") #this are the arguments
#we have to give same amount of arguments as the parameters we have given.


#if we don't know the amount of arguments we can use artibitrary arguments.
def fun1(*name):
    print(name[2])
    
fun1("MD","Yeamin","Islam",24,"Dhaka")



def hello2(fname="Md.Yeamin",lname="Islam"):
   print(f"My Full Name: {fname} {lname}")

hello2()    

#Arbitrary Keyword Arguments (kwargs)
#this one is acts like dictionary
def name2(**kwargs):
    print(kwargs["fname"])
    
name2(fname="Md. Yeamin",lname="Islam",age=25)

def name3(*args,**kwargs):
    print(args,kwargs)

name3("MD","Yeamin","Islam",24,"Dhaka",fname="Md. Rabiul",lname="Islam",age=53)



