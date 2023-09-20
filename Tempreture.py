cel = float(input("Enter the tempreture in Celsius: "))

def ternIntoFehrenheit(cel):
    fehren = cel * 9/5 + 32

    return print(f"The tempreture in fehrenheit is {fehren} ")

print()
print("___________________________________")
ternIntoFehrenheit(cel)