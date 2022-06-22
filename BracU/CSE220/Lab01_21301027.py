#Task1

source_1 = [10, 20, 30, 40, 50, 60]


def shiftLeft(source_1, k):
    for i in range(len(source_1)-k):
        source_1[i] = source_1[i+k]

    for j in range(len(source_1)-k, len(source_1)):

        source_1[j] = 0

    print(source_1)

shiftLeft(source_1, 3)


#Task 2

source_2 = [10, 20, 30, 40, 50, 60]


def rotate_left(source, k):

    new = [0]*k

    i = 0
    while(i <= k-1):
        new[i] = source[i]
        i += 1

    j = 0
    while(j <= len(source)-k-1):
        source[j] = source[j+k]
        j += 1

    m = 0
    while(m < len(new)):
        source[len(source)-1-m] = new[len(new)-1-m]
        m += 1

    print(source)


rotate_left(source_2, 3)


#Task 3

source_3 = [10, 20, 30, 40, 50, 60]


def shiftright(source, k):

    i = len(source) - 1

    while(i-k >= 0):
        source[i] = source[i-k]
        i -= 1

    for j in range(k):
        source[j] = 0

    print(source)


shiftright(source_3, 3)

#Task 4

source_4 = [10, 20, 30, 40, 50, 60]


def rotateRight(source, k):

    lost_array = [0]*k

    i = len(source) - 1

    for j in range(k):
        lost_array[j] = source[i]
        i -= 1

    n = len(source) - 1

    while(n-k >= 0):
        source[n] = source[n-k]
        n -= 1

    for x in range(k):
        source[x] = lost_array[k-x-1]

    print(source)


rotateRight(source_4, 3)

#Task 5

source_5 = [10, 20, 30, 40, 50, 0, 0]


def remove(source, size, ind):
    str = ind + 1
    while(str <= size):
        source[str-1] = source[str]
        str += 1

    source[size-1] = 0

    print(source)


remove(source_5, 5, 2)


#Task 6

source_6 = [10, 2, 30, 2, 50, 2, 2, 0, 0]



def removeAll(source,size,given):

    for i in range(size-1):
        if source[i] == given:
            for j in range(i,size-1):
                source[j] = source[j+1]






    count = 0
    for k in range(size):
        if source[k] == given:
            count += 1


    str = size-1

    for l in range(count):
        source[str] = 0
        str -= 1

    print(source)

removeAll(source_6,7,2)

#Task 7


source_7 = [10, 3, 1, 2, 10]


def split(source):

    total = 0
    total_2 = 0
    Flag = False
    for i in range(len(source)-1):

        for j in range(i+1):
            total += source[j]

        for k in range(i+1, len(source)):
            total_2 += source[k]

        if total == total_2:
            Flag = True

        else:
            total = 0
            total_2 = 0

    print(Flag)


split(source_7)

#Task 8


def series(n):
    len_array = n*n
    source = [0]*len_array

    for i in range(1, n+1):

        start = n*i - i

        for j in range(n-i+1):

            source[start] = i
            start += n

    print(source)


series(3)

# Task 9

input_9 = [1, 2, 2, 3, 4, 4, 4]


def max_bunch_count(input):

    max_count = 0

    count = 1

    for i in range(1, len(input)):

        for j in range(i, len(input)):
            if input[j-1] == input[j]:
                count += 1
            else:
                break

        if count > max_count:
            max_count = count
            count = 1
        else:
            count = 1

    print(max_count)


max_bunch_count(input_9)

#Task 10

input_10 = [4, 5, 6, 6, 4, 3, 6, 4]


def repetition(input):

    max = 0

    for i in range(len(input)):
        if input[i] > max:
            max = input[i]

    new_array = [0]*(max+1)

    for j in range(len(input)):
        new_array[input[j]] += 1

    flag = False

    for k in range(len(new_array)):
        if new_array[k] != 0:
            val = new_array[k]

            for l in range(k+1, len(new_array)):

                if new_array[l] == val:
                    flag = True

                    break
                else:
                    continue

            if flag == True:
                break
            else:
                continue

    print(flag)


repetition(input_10)
