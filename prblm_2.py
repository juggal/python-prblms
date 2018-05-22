num = int(input("Enter any number:"))
check = int(input("Enter another no:"))
if num % 4 == 0:
    print('Number is divisible by 4')
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
if check % num == 0:
    print("It divides evenly")
else:
    print("It does not divides evenly")
