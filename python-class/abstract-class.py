class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract')

class Dog(Animal):
    def speak (self):
        return self.name+ "Says woof!"
class Cat(Animal):
    def speak (self):
        return self.name+ "Says meow!"

fido=Dog("fido ")
isis=Cat("Isis ")
print (fido.speak())
print (isis.speak())