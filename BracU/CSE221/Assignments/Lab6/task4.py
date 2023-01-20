def input_process():

    file_1 = open("input4.txt", "r")


    x = 0

    info = []



    while (x!=[0,0]):

        line = file_1.readline().strip("\n").split(" ")
        start = int(line[0])
        end = int(line[1])

        info.append([start,end])

        x = [start,end]








    file_1.close()

    info = info[0:-1]

    return info


x = input_process()



def processing(x):

    output = []

    for i in range(len(x)):
        start = x[i][0]
        end = x[i][1]
        number_sets = []
        i = start
        while i<=end:

            a = i**0.5
            b = int(a)
            c = a-b
            if c==0:
                number_sets.append(i)
            i += 1


        output.append(number_sets)



    return output


y = processing(x)

def result(y):
    file_2 = open("output4.txt", "w")

    for i in y:
        file_2.write(f"{len(i)} \n")

    file_2.close()




result(y)