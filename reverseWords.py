from tkinter import N


def convert(string):
    listed = list(string.split(" "))
    return listed

string = raw_input("Enter a string:")

arr = list()

arr = convert(string)

arr.reverse()

for i in range(0, len(arr)):
    print arr[i]
