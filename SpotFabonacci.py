def spotFabonacci(arr):
    for i in range(2, len(arr)):

        IsAFabanacci = True

        if(arr[i-2] + arr[i-1] != arr[i]):
            IsAFabanacci = False

        if(IsAFabanacci == True):
            return 1
        else:
            return 0

arr = list()

arr = input("Enter a array")

if(spotFabonacci(arr) == 1):
    print("This is a fabonacci sequence")
else:
    print("This is not a fabonacci sequence")
