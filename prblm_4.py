num = int(input("Enter any number:"))
list = []
for i in range(1, num+1):
    if num % i == 0:
        list.append(i)
print(list)
