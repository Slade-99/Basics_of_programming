


def input_process():

    file_1 = open("input1.txt","r")
    tasks = int(file_1.readline().strip("\n0"))
    start_time = []
    end_time = []
    for i in range(tasks):
        x = file_1.readline().strip("\n").split(" ")
        start_time.append(int(x[0]))
        end_time.append(int(x[1]))


    output = []
    output.append(tasks)
    output.append(start_time)
    output.append(end_time)


    file_1.close()

    return output


x = input_process()

tasks = x[0]
start_time = x[1]
end_time = x[2]




final = []

for i in range(len(end_time)):
  final.append([end_time[i], start_time[i]])


final.sort()

start_time = []
end_time = []


for i in final:

  end_time.append(i[0])
  start_time.append(i[1])


def task_selector(start_time, end_time, n):

  output = []

  output.append([start_time[0], end_time[0]])

  k = 0

  i = 1
  while (i < n):
    if start_time[i] >= end_time[k]:
      output.append([start_time[i], end_time[i]])
      k = i
    i += 1
  return output


x = task_selector(start_time, end_time, tasks)


def result(x):
    file_2 = open("output1.txt","w")
    file_2.write(f"{len(x)}\n")
    for i in x:
        file_2.write(f"{i[0]}  {i[1]}\n")




result(x)