Lower_Limit = int(input("Enter the lower limit:"))
Upper_Limit = int(input("Enter the upper limit:"))

x = int(input("enter the first value:"))
y = int(input("enter the second value:"))

desired_numbers = []

for i in range(Lower_Limit + 1, Upper_Limit):
    if(x and y > 0):
        if(i%x == 0 and i%y == 0):
            desired_numbers.append(i)
    
    i += 1

print(desired_numbers)
