# Task 5


file_1 = open("input5.txt", "r")


x = file_1.read()

list_1 = x.split("\n")[1:]
names = []
times = []
time_sliced = []
destination = []

for i in range(len(list_1)):
    names.append(list_1[i][0:list_1[i].find(" ")+1])

for i in range(len(list_1)):
    times.append(list_1[i][list_1[i].find(" ", -8, -1):])

for i in range(len(list_1)):
    time_sliced.append(list_1[i][0:list_1[i].find(" ", -10, -1)])

for i in range(len(list_1)):
    destination.append(time_sliced[i][time_sliced[i].rfind(" "):])


for i in range(len(names)-1):
    for j in range(len(names)-i-1):
        if names[j] > names[j+1]:
            names[j], names[j+1] = names[j+1], names[j]
            times[j], times[j+1] = times[j+1], times[j]
            destination[j], destination[j+1] = destination[j+1], destination[j]

for i in range(len(names)-1):
    for j in range(len(names)-i-1):
        if names[j] == names[j+1] and times[j] < times[j+1]:
            names[j], names[j+1] = names[j+1], names[j]
            times[j], times[j+1] = times[j+1], times[j]
            destination[j], destination[j+1] = destination[j+1], destination[j]


print(names)
print(times)
print(destination)


file_2 = open("output5.txt", "w+")
for i in range(len(names)):
    file_2.write(
        f"{names[i]} will departure for {destination[i]} at {times[i]}\n")

file_2.close()
