
def old_macdonald(name):
    first_letter=name[0]
    inbetween=name[1:3]
    fourth_letter=name[3]
    rest=name[4:]
    a= ((first_letter.upper())+(inbetween)+(fourth_letter.upper())+(rest))
    print (a)
    return first_letter.upper()+inbetween+fourth_letter.upper()+rest
 
old_macdonald('macdonald')

def old_macdonalds(name):
    first_half= name[:2]
    second_half=name[2:]
    a=(first_half.capitalize())+(second_half.capitalize())
    print (a)
    return first_half.capitalize()+second_half.capitalize()

old_macdonalds('mcdonald')

