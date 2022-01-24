def two_word_string(text):
    wordlist = text.split()
    first_word=wordlist[0]
    second_word=wordlist[1]
    return first_word[0] == second_word[0]
two_word_string('Lovely Love')

def two_word_string2(text):
    wordlist = text.split()
    first_word=wordlist[0]
    second_word=wordlist[1]
    if wordlist[0][0] == wordlist[1][0]:
        print (wordlist[0],wordlist[1])
    else:
        print ('string not matching')
two_word_string2('Lovely love')

def two_word_different_case_string2(text):
    wordlist = text.lower().split()
    first_word=wordlist[0]
    second_word=wordlist[1]
    if wordlist[0][0] == wordlist[1][0]:
        print (wordlist[0],wordlist[1])
    else:
        print ('string not matching')
two_word_different_case_string2('Lovely love')

