def square(num):
    #print (num**2)
    return num**2
mynums=[1,2,3,4,5]
for item in map(square,mynums):
    print (item)
print (list (map(square,mynums)))
square(6)

def splicer(mystring):
    if len(mystring)%2==0:
        print ('EVEN')
        return 'EVEN'
    else:
        print (mystring[0])
        return mystring[0]
names=['Sundar','eve','jack']
list(map(splicer,names))
print (list(map(splicer,names)))

def check_even(num):
    print (num%2==0)
    return num%2==0

mynums=[1,2,3,4,5,6]
print (list(filter(check_even,mynums)))

def square(num):
    result = num **2
    print (result)
    return result
square(3)

square=lambda num:print (num**2)
square(4)

print (list(map(lambda num:num**2,mynums)))
print (list(filter(lambda num:num%2,mynums)))

print (names)

print (list(map(lambda x:x[0],names)))
names_n=(list(map(lambda x:x[0],names)))
for n in names_n:
    #print (n.upper())
    print (list(n.upper()))
print (list(n.upper()))