class Dog():
    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    species='mammal'
    def __init__(self,breed,name,spots):#init called automatically when we create infrastructure of the class
        self.breed=breed
        self.name=name

        #Exppect boolean True/False
        self.spots=spots

    #OPERATIONS/ ACTIONS ----->Methods
    def bark(self,number):
        #in this example number is user defined so self cannot work
        print ("WOOF! My Name is ",(self.name),"my number is ",(number))
my_dog=Dog('lab','Sammy',False)
type(my_dog)
print (type(my_dog))
#ATTRIBUTES NEVER HAD OPEN AND CLOSE PARANTHESIS
my_dog.name
print (my_dog.name)
my_dog.species
print (my_dog.species)
my_dog.bark(10)
my_dog.bark('10')
#print (my_dog.bark())

class Circle():
    #CLASS OBJECT ATTRIBUTE
    pi=3.14

    def __init__(self,radius=1):
        self.radius=radius
        Circle.area=radius*radius*self.pi
        print (self.radius)
        #both class name and self work as same
        print (Circle.area)
    def get_circumference(self):
        print (self.radius*self.pi *2)
        return self.radius*self.pi *2
my_circle= Circle(30)
my_circle.radius

my_circle.get_circumference()