#Object Oriented Programming
#Inheritance

#creating a class
#parent class
class A:
    #creating a constructor which is a method and it is called when an object/instance is created.
    def __init__(self,name):
        self.name = name #storing the name parameter in the name attribute of the class
    
    def hello(self):
        print("Hello form class A")

#obj = A("Yeamin")     #creating an object/instance of the class A
#obj.hello()  

#creating a class B which inherits the class A
#child class of class A
class B():
    def __init__(self,job):
        self.job = job

    #here hello() method of class B will override the hello() method of the class A it's just happend because we are working with class B and before that this class B doesn't have any method and constructore.And now class B has method this why it will override the meethod of class A and similar case to __init__() method.
    def hello(self):
        print("Hello form class B")

#this is multilevel inheritance
#In multiple inheritance we can access first class methods and constructor
#and in multilevel inheritance we can access latest class methods and constructor 
#class B inherits class A and class C inherits class B
#here c will inherit the class A and class B together
class C(A,B):
    def __init__(self,name,job):
        #accessing parent class constructor.
        A.__init__(self,name)
        B.__init__(self,job)
        
        
    
    def hello(self):
        super().hello() #here super() will call the hello() method of the class A because this method follow __mro__() sequence.
        B.hello() #calling particular class method
        print(f"{self.name} is a {self.job}")

#here c will use the constructor of class B
newobj = C("Yeamin","Programmer")
newobj.hello()
print(C.__mro__)
#MRO->(Method Resolution Order)
#This MRO will show the order of inheritance of the class C.Accessing sequence of classess.
#print(dir(newobj)) it will show all the methods and attributes of the class C

