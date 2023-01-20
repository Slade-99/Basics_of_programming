



def input_process():
    file_1 = open("input3.txt","r")

    tasks_count = int(file_1.readline().strip("\n"))
    sequence = file_1.readline().strip("\n").split(" ")
    calls = file_1.readline().strip("\n")


    final_calls = []

    for i in calls:
        final_calls.append(i)



    durations = []
    for i in sequence:
        durations.append(int(i))



    return final_calls,durations


x = input_process()


calls = x[0]
durations = x[1]


def processing(calls,durations):

    all_picked = []
    Jack_picked = []
    Jill_picked = []

    for i in calls:
        if i == "J":
            min = 9999
            for i in durations:
                if i<min and i not in Jack_picked:
                    min = i

            Jack_picked.append(min)
            all_picked.append(min)

        else:
            max = 0

            for i in Jack_picked:
                if i>max and i not in Jill_picked:
                    max = i

            Jill_picked.append(max)
            all_picked.append(max)

    final = []
    final.append(all_picked)
    final.append(Jack_picked)
    final.append(Jill_picked)

    return final


y = processing(calls,durations)

print(y)
Overall = y[0]
Jack = y[1]
Jill = y[2]

print(Jill)
def results(Overall,Jack,Jill):

    file_2 = open("output3.txt","w")
    print(Jill)
    for i in Overall:
        file_2.write(f"{i} ")
    file_2.write("\n")

    jack_total = 0
    for i in Jack:
        jack_total += i

    jill_total = 0

    for j in Jill:
        jill_total += j

    file_2.write(f"Jack will work for {jack_total} hours \n")
    file_2.write(f"Jill will work for {jill_total} hours \n")




    file_2.close()



results(Overall,Jack,Jill)