"""
INITIAL LIST
SHUFFLE LIST
USER GUESS
CHECK
"""
"""
example = [1,2,3,4,5,6,7]
from random import shuffle
from tabnanny import check
shuffle (example)
print (example)
"""
from random import shuffle
from tabnanny import check

mylist= [' ','O',' ']
#print ('This is mylist : \n',mylist)

def shuffle_list(mylist):
    shuffle(mylist)
    return (mylist)
#print ('The shuffled list is : \n',shuffle_list(mylist))


def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("Pick a number between 0,1 and 2: \n")
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O' :
        print("Congratulations! You have won the game.......")
    else:
        print("Sorry! you have lost the game")
        print (mylist)


#INITIAL LIST
mylist = [' ', 'O', ' ']

#SHUFFLE LIST
mixedup_list= shuffle_list(mylist)

#USER GUESS
guess=player_guess()

#CHECK GUESS
check_guess(mixedup_list,guess)
