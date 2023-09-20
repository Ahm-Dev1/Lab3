employees = {}



while True :

    name = input("Enter employee name: ")
    if name == "no":
         break
    salary = int(input("Enter the salary: "))

    employees[name] = salary
    print('Employee added') 

print("")
print("_________________________________________")
print('End of adding')
print(f"The employees dectionary: {employees}")


