def division(a):
    if a < 4:
        b = a/(a-3)
    return b

a = input("Enter a greater number than 3:")

try:
    returned = division(a)
    print(returned)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
