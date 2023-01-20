
# task 1a



file_3 = open("input1a.txt", "r+")


x = file_3.read()

list_1 = x.split("\n")
list_2 = []
print(list_1)

for i in list_1:
    if (int(i)) % 2 == 0:
        list_2.append(f"{int(i)} is an Even number")
    else:
        list_2.append(f"{int(i)} is an Odd number")
file_3.close()

file_4 = open("output1a.txt", "w+")
for i in list_2:
    file_4.write(f"{i}\n")

file_4.close()


# Task 1b


file_1 = open("input1b.txt", "r")


x = file_1.read()

list_1 = x.split("\n")[1:]
list_2 = []
list_3 = []
list_4 = []

file_1.close()
for i in list_1:
    list_2.append(i[10:])


for i in list_2:
    x = i.find(" ")
    list_3.append(int(i[0:x]))
    list_3.append(int(i[x+3:]))

y = 0
for i in range(0, len(list_3), 2):

    if "+" in list_2[y]:
        list_4.append(
            f"The result of {list_3[i]}+{list_3[i+1]} is {list_3[i]+list_3[i+1]}")
        y += 1
    elif "-" in list_2[y]:
        list_4.append(
            f"The result of {list_3[i]}-{list_3[i+1]} is {list_3[i]-list_3[i+1]}")
        y += 1
    elif "*" in list_2[y]:
        list_4.append(
            f"The result of {list_3[i]}*{list_3[i+1]} is {list_3[i]*list_3[i+1]}")
        y += 1
    else:
        list_4.append(
            f"The result of {list_3[i]}/{list_3[i+1]} is {list_3[i]/list_3[i+1]}")
        y += 1


file_2 = open("output1b.txt", "w+")
for i in list_4:
    file_2.write(f"{i}\n")

file_2.close()
