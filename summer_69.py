def summer_69(arr):
    total =0
    add=True
    for num in arr:
        while add:
            if num!=6:
                total+=num
                break
            else:
                add=False
            while num!=9:
                break
            else:
                add=True
                break
    print (total)
    return total
summer_69([2,1,6,9,11])