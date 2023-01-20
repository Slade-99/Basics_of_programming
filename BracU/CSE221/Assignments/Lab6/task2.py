

def input_process():

    file_1 = open("input2.txt", "r")
    x = file_1.readline().strip("\n").split(" ")

    tasks = int(x[0])
    members = int(x[1])
    start_time = []
    end_time = []
    for i in range(tasks):
        x = file_1.readline().strip("\n").split(" ")
        start_time.append(int(x[0]))
        end_time.append(int(x[1]))

    output = []
    output.append(tasks)
    output.append(members)
    output.append(start_time)
    output.append(end_time)

    file_1.close()

    return output


x = input_process()

tasks = x[0]
members = x[1]
start_time = x[2]
end_time = x[3]


final = []

for i in range(len(end_time)):
  final.append([end_time[i], start_time[i]])


final.sort()

start_time = []
end_time = []


for i in final:

  end_time.append(i[0])
  start_time.append(i[1])






def task_selector(start_time, end_time, n,members):



  output = []

  for i in range(members):



    ending = 0


    for j in range(len(start_time)):
        test = [start_time[j],end_time[j]]
        if test not in output and start_time[j]>= ending:
            output.append([start_time[j], end_time[j]])
            ending = end_time[j]



  return output


x = task_selector(start_time, end_time, tasks, members)




def result(x):
    file_2 = open("output2.txt", "w")
    file_2.write(f"{len(x)}\n")




result(x)