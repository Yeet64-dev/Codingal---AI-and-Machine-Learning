def binary_to_decimal(bin):
    decimal = 0
    for i in range(len(bin)):
        decimal += int(bin[len(bin) - 1 - i]) * (2 ** i)
    return decimal
bin = input("Enter Your Binary: ")
print(" Decimal : " + str(binary_to_decimal(bin)))