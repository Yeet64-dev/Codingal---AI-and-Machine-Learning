num = int(input("Enter the largest number: "))
num2 = int(input("Enter the smallest number: "))
HCF = 1
for i in range(1,num2+1):
    if num % i == 0 and num2 % i == 0:
        HCF = i
print("The HCF of", num, "and", num2, "is", HCF)
