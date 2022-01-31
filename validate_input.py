def user_choice():
    #VARIABLES
    #Initial
    choice = 'WRONG'
    acceptable_range = range(0,10)

    within_range= False

    #TWO CONDITIONS TO CHECK
    #DIGIT OR WITHIN_RANGE=FALSE


    while choice.isdigit()==False or within_range==False:
        choice=input("Please enter a number between (0-10): ")

        #DIGIT_CHECK
        if choice.isdigit()==False:
            print ("Sorry, that is not a digit! ") 
        #RANGE CHECK
        if choice.isdigit()==True:
            if int(choice) in acceptable_range:
                print ("Thanks! for providing the proper input..........")
                within_range=True
            else:
                print ('Sorry! You have entered the input beyond the limit.............')
                within_range=False
    print (int(choice))
    return int(choice)
user_choice()

#some_value='100'
#some_value.isdigit()