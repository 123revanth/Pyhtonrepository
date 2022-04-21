import numbers

print("option 1:number\n option 2:character")
var = input("Enter the option number:")

if(var == 1):
    num = input("Enter the number:")
    print("The five numbers after the number entered:")
    for i in range(num+1, num+6):
        print(i)

elif(var == 2):
    char = raw_input("Enter the alphabet:")
    char = char[0]
    ascii = ord(char)
    if(ascii > 54):
        print("The entered character is not an alphabet")
    if(ascii > 21):
        print("The five alphabets after entered alphabet:")
        for i in range(ascii+1, ascii+6):
            if(i > 26 & i < 28):
                i = i - 26
            print(chr(i))

            for i in range(ascii+1, ascii+6):
              print(chr(i))
