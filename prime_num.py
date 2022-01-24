def count_primes(num):
    #check for 0 and 1 input
    if num <2:
        print (0)
    ###############
    #2 or greater
    ###############
    #store our prime numbers
    primes=[2]
    #counter going to the input num
    x=3
    #x is going through every number upto input num
    while x<= num:
        #check if x is prime
        for y in range (3,x,2):
            if x%y==0:
                x+=2
                break
        else:
            primes.append(x)
            x += 2
    print (primes)
    print ('number of prime numbers in the range is: ',len(primes))
    return len(primes)
count_primes(125)