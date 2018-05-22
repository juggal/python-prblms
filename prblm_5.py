import random
a = random.sample(range(0, 30), 8)
b = random.sample(range(0, 40), 8)
print(a)
print(b)
c = []
for i in a:
    if i in b:
        if i in c:
            print("These are the duplicates", i)
        else:
            c.append(i)

print(c)
