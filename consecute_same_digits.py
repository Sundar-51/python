def has_33(nums):
    for i  in range (0,len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            print ('True')
            return True
    print ('false')
    return False
has_33([1,3,1])
has_33([1,3,3])

def paper_doll(text):
    result=''
    for char in text:
        result += char*3
        #print (result)
    return result
paper_doll('missisipi')
print (paper_doll('missisipi'))

