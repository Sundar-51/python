#Polymorphism - different object and classes shares the same method
class Dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + "says woof!"

class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + "says meow!"

niko=Dog("niko")
felix=Cat("felix")
print (niko.speak())
print (felix.speak())
for pet in [niko,felix]:
    print (type(pet))
def pet_speak(pet):
    print (pet.speak())
pet_speak(felix)

