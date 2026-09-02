num = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
HCF = 1
if num > num2:
    for i in range(1,num2+1):
        if num % i == 0 and num2 % i == 0:
            HCF = i
if num2 > num:
    for i in range(1,num+1):
        if num % i == 0 and num2 % i == 0:
            HCF = i
print("The HCF of", num, "and", num2, "is", HCF)