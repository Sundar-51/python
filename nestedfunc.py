name = "HELLO THIS IS MY FUNCTION"
def greet():
    name='Sammy'
    def hello():
        print ('hello ',name)
    hello()
    return ('hello',name)
greet()
print (name)

x=50
def func():
    global x
    #x=50
    print (f'X is {x}')
    x='NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
func()
print (x)