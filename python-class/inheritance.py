class Animal():
    def __init__(self):
        print ("ANIMAL CREATED")

    def who_am_i(self):
        print ("I am an animal")
    
    def eat(self):
        print ("I am eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)

        Animal.who_am_i(self)

        print ('Dog Created')
    def who_am_i(self):
        print ("I am a dog")
myanimal=Animal()
mydog=Dog()
#even though if u have not imported eat method still u can use
mydog.who_am_i()

