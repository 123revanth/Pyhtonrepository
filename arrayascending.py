from re import L


list = []

n = int(input("enter the number of inputs"))

tempinput = 0

for i in range(n):
    tempinput = int(input())
    list.append(tempinput)

print("-------------------")

smallesnum = list[0]              

l = 0

newlist = []

while(l <= n):
    for i in range(n):
        if(list[i] <=  smallesnum):
            smallesnum = list[i]

    newlist.append(smallesnum)
    smallesnum = 0
    i = i + 1

for i in range(n):
    print(newlist[i])
