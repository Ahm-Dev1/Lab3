numbers = []
count = 1
while count <= 10:
    num = int(input("Enter a number: "))
    numbers.append(num)
    count += 1

def largestnumber(numbers):
    biggest_num = numbers[0]

    for num in numbers:
        if num > biggest_num:
            biggest_num = num

    return print(f"The largest number is {biggest_num}")
print()
print("_____________________________________")
largestnumber(numbers)
# x = 0
# for i in numbers:
#     if numbers[i] > x:
#         x = numbers[i]

# print(f"The largest number is {x}")
