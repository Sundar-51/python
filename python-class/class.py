mylist=[1,2,3]



class SampleWord():
    pass

my_sample=  SampleWord()
type(my_sample)
print (type(my_sample))

class Dog():
    def __init__(self,breed):#init called automatically when we create infrastructure of the class
        self.breed=breed
my_dog=Dog(breed='Lab')
type(my_dog)
print (type(my_dog))
my_dog.breed
print (my_dog.breed)
my_dog.breed

class Dog2():
    def __init__(self,mybreed):#init called automatically when we create infrastructure of the class
        #Attributes
        #We take in argument {mybreed}
        #Assign it using self.attribute_name {breed}
        self.breed=mybreed
my_dog=Dog2(mybreed='Huskie')
type(my_dog)
print (type(my_dog))
my_dog.breed
print (my_dog.breed)
my_dog.breed

class Dog3():
    def __init__(self,breed,name,spots):#init called automatically when we create infrastructure of the class
        self.breed=breed
        self.name=name

        #Exppect boolean True/False
        self.spots=spots

my_dog=Dog3(breed='lab',name='Sammy',spots=False)
type(my_dog)
print (type(my_dog))
my_dog.breed
print (my_dog.name)
my_dog.name