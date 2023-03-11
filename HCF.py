n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))

arr1 = []
arr2 = []

for i in range(0, n1+1):
    if(i != 0):
        if(n1%i == 0):
            arr1.append(i)

for i in range(0, len(arr1)):
    print(arr1[i])

print("_______")


for i in range(1, n2):
    if(n2%i == 0):
        arr2.append(i)

for i in range(0, len(arr2)):
    print(arr2[i])

largest = 0

for i in range(0,len(arr1)):
    for j in range(0, len(arr2)):
        if(arr1[i] == arr2[j]):
            if(largest <= arr1[i]):
                largest = arr1[i]

print("highest common factor")
print(largest)
