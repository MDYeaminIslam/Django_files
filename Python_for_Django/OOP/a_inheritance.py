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
class B(A):
    def __init__(self,name,job):
        #super() is a powerfull function which is used to call the parent class constructor in the child class. we can access any element of the parent class by using super() function.
        super().__init__(name) #give the parameter of the parent class constructor.
        self.job = job

    #here hello() method of class B will override the hello() method of the class A it's just happend because we are working with class B and before that this class B doesn't have any method and constructore.And now class B has method this why it will override the meethod of class A and similar case to __init__() method.
    def hello(self):
        print(f"{self.name} is a {self.job}")

#this is multilevel inheritance
#class B inherits class A and class C inherits class B
class C(B):
    pass

#here c will use the constructor of class B
newobj = C
#print(dir(newobj)) it will show all the methods and attributes of the class C

