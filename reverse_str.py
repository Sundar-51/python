def reverse_str(text):
    wordlist=text.split()
    reverse_word_list=wordlist[::-1]
    print (reverse_word_list)
    return reverse_word_list

reverse_str('hi hello how are you')

mylist=['a','b','c']
x='--'.join(mylist)
print (x)