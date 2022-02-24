def oddoreven(number):
    if(number % 2 == 0):
        return 0
    else:
        return 1

def primeornot(number):
    if(oddoreven(number) == 0):
        return 4
    else:
        checker = 0
        for i in range(3, number):
            if(number % i == 0):
                checker = 1
        
        if(checker == 0):
            return 2
        else:
            return 4

num1 = int(input("Enter until which number to find prime numbers"))
cointainer = 0
counter = 0

for i in range(2, num1):
    cointainer = primeornot(i)
    if(cointainer == 2):
        print i
        counter = counter + 1

print "The number of prime numbers in the range is",  + counter
    
    
