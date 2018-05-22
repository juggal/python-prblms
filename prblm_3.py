list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = []
num = int(input("Enter any number:"))
for i in list_1:
    if i < num:
        list_2.append(i)
    else:
        break
print(list_2)
