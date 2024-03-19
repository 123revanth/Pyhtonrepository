x = int(input("enter the first number"))
y = int(input("enter the second number"))

truth = 0

if x > y :
    truth = 1

HCF = []

key = int(input("enter one for HCF and zero for LCM"))

if truth == 1:
       for i in range(1, x + 1):
           if x%i == 0 and y%i == 0:
                HCF.append(i)
else:
       for i in range(1, y + 1):
           if x%i == 0 and y%i == 0:
                HCF.append(i)

if key == 1:
    m = len(HCF) - 1
    ValueHCF = HCF.pop(m)
    print(ValueHCF)
    quit()

if key == 0:
     a = len(HCF) - 1
     z = HCF.pop(a)
     LCM = x * y 
     LCM /= z
     print(LCM)




