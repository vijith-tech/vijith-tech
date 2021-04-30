#loop step by step values are print
#list items by using for loop
fruit = ["apple", "orange", "mango", "pineapple"]
for x in fruit:
    print(x)

fruit = ["apple", "orange", "mango", "pineapple"]
for x in fruit:
    print(x)
    if x == "mango":
        break

fruit = ["apple", "orange", "mango", "pineapple"]
for x in fruit:
    if x == "mango":
        continue
    print(x)

#range
for x in range(2, 6):
    print(x)

colour = ["gold"]
name = ["vijith"]
for x in colour:
    for y in name:
        print(x,y)

# pass statement

for x in [0, 1, 7]:
    pass
print(x)








