from ast import Pass


def vol(rad):
    print ((4/3)*(3.14)*(rad**3))

vol(2)

def num_check(num,low,high):
    print (num in range (low,high+1))
num_check(6,2,7)

def up_low(s):
    lowercase=0
    uppercase=0
    for char in s:
        if char.isupper():
            uppercase+=1
            print (uppercase)
        elif char.islower():
            lowercase+=1
            print (lowercase)
        else :
            pass
    print (f'the count of uppercase letters is {uppercase}', f'the count of lowercase is {lowercase}')
up_low("hi, hello How Are You?")

def up_low2(s):
    d={'lower':0,    'upper':0}
    for char in s:
        if char.isupper():
            d['upper']+=1
            #print (upper)
        elif char.islower():
            d['lower']+=1
            #print (lower)
        else :
            pass
    print (f'the count of uppercase letters is {d["upper"]}', f'the count of lowercase is {d["lower"]}')
up_low2("hi, How Are You?")

def unique_list(lst):
    print (list(set(lst)))
    return set (lst)
unique_list([1,2,5,3,4,4,5,5,6,6,2,'a','a','b'])

def unique_list2(lst):
    seen_numbers=[]
    for number in lst:
        if number not in seen_numbers:
            seen_numbers.append(number)
    print (seen_numbers)

unique_list2([1,2,5,3,4,4,5,5,6,6,7,2,'a','a','b'])


def multiply(numbers):
    total=1
    for num in numbers:
        total=total*num
    print (total)

multiply([1,4,2,-9])

def palindrome(string_given):
    #REMOVE SPACE FROM STRING
    string_given=string_given.replace(' ','')
    print (string_given)
    #CHECK STRING IS == REVERSAL OF STRING
    rev=string_given[::-1]
    if string_given==rev:
        print ("The given string ",string_given," is a palindrome")
    else:
        print ("The given string ",string_given," is not a palindrome")
palindrome("race car")

import string
def ispanagram(str1, alphabet=string.ascii_lowercase):

    #Create a set of alphabet
    alphaset=set(alphabet)
    print (alphaset)
    #remove the spaces from the input string
    str1=str1.replace(' ','')
    print (str1)
    #convert all into lowercase
    str1=str1.lower()
    print (str1)
    #grab all unique letters from the string set ()
    str1=set(str1)
    print (str1)
    #alphabet string == string set input
    #return str1==alphaset
    if str1==alphaset:
        print (" its a panagram")
    else:
        print (" its NOT a panagram")

ispanagram("The quick brown fox jumps over the lazy dogs")
print (ispanagram("The quick brown fox jumps over the lazy dogs").sort(key=sort_key, reverse=False))


