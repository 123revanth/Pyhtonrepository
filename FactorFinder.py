from re import I


def factorFinder(num):
    
    returned = list()

    for i in range(1, num):
        if(num%i == 0):
            returned.append(i)

    returned.append(num)    
    return returned
        

num = int(input("Enter a number"))

arr = factorFinder(num)

print(arr)
