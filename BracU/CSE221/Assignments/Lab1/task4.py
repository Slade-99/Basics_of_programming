# Task 4


file_1 = open("input4.txt", "r")


x = file_1.read()

list_1 = x.split("\n")[1:]

id = list_1[0].split(" ")
marks = list_1[1].split(" ")


for i in range(1, len(marks)):

  key = int(marks[(i)])
  key_2 = int(id[i])

  j = i-1
  while j >= 0 and key < int(marks[j]):
    marks[j + 1] = int(marks[j])
    id[j+1] = int(id[j])
    j -= 1
  marks[j + 1] = key
  id[j+1] = key_2


for i in range(len(marks)):
  for j in range(i+1, len(marks)):
    if marks[i] == marks[j] and id[i] < id[j]:
      x = id[i]
      y = id[j]
      id[j] = x
      id[i] = y


i = len(marks)-1
file_2 = open("output4.txt", "w+")

while i >= 0:

  file_2.write(f"ID: {id[i]} Mark: {marks[j]}\n")
  i -= 1

file_2.close()
