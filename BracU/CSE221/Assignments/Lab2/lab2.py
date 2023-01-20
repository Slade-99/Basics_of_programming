

# Task 1
file_1 = open("input1.txt", "r")


file = file_1.read()

full = file.split("\n")[1:]
id = full[0].split(" ")
marks = full[1].split(" ")


for i in range(len(marks)-1):
    temp = int(marks[i+1])
    temp_1 = int(id[i+1])
    j = i
    while j >= 0:
        if(int(marks[j]) < int(temp)):
            marks[j+1] = int(marks[j])
            id[j+1] = int(id[j])
        else:
            break
        j = j - 1
    marks[j+1] = temp
    id[j+1] = temp_1

file_2 = open("output1.txt", "w+")
for i in id:
    file_2.write(f"{i} ")

file_2.close()



# Task 2(i)
"""
The recursive tree has n leaves in each level and the
height of the recursive tree is log(n)

So, the time complexity will be nlog(n)
"""


# Task 2 (ii)


file_1 = open("input2.txt", "r")


file = file_1.read()

full = file.split("\n")[1:]
A = full[0].split(" ")

p = 0

r = len(A) - 1


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    arrayL = [0]*(n1+1)
    arrayR = [0]*(n2+1)
    for i in range(n1):
        arrayL[i] = int(A[p+i])

    for j in range(n2):
        arrayR[j] = int(A[q+j+1])

    arrayL[-1] = 9999
    arrayR[-1] = 9999

    i = 0
    j = 0
    k = p
    while k <= r:

        if arrayL[i] <= arrayR[j]:
            A[k] = arrayL[i]
            i += 1
        else:
            A[k] = arrayR[j]
            j += 1

        k += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


for i in range(len(A)):
    A[i] = int(A[i])


merge_sort(A, p, r)
file_2 = open("output2.txt", "w+")
for i in A:
    file_2.write(f"{i} ")

file_2.close()



# Task 3(i)

file_1 = open("input3(i).txt", "r")


file = file_1.read()

full = file.split("\n")[1:]
arr = full[0].split(" ")

low = 0
high = len(arr) - 1


def quickSort(arr, low, high):
    if(low < high):
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if(arr[j] < pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


for i in range(len(arr)):
    arr[i] = int(arr[i])

quickSort(arr, low, high)


file_2 = open("output3(i).txt", "w+")
for i in arr:
    file_2.write(f"{i} ")

file_2.close()


# Task 3 (II)


file_1 = open("input3(ii).txt", "r")


file = file_1.read()

full = file.split("\n")[:1]
values = file.split("\n")[1:]
for i in range(len(values)):
    values[i] = int(values[i][-1])

arr = full[0].split(" ")


def partition(arr, low, high):
    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if(arr[j] < pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return arr[i + 1]


for i in range(len(arr)):
    arr[i] = int(arr[i])

file_2 = open("output3(ii).txt", "w+")
for i in values:
    x = partition(arr, 0, i-1)
    file_2.write(f"{x}\n")

file_2.close()



# Task 4(a)

file_1 = open("input4.txt", "r")


x = file_1.read()

list_1 = x.split("\n")


print(list_1)


class task:

    def __init__(self):
        self.list_queue = []

    def bubble_sort(self):
        for i in range(len(self.list_queue)-1):
            for j in range(len(self.list_queue)-i-1):
                if int(self.list_queue[j][-1]) > int(self.list_queue[j+1][-1]):
                    self.list_queue[j], self.list_queue[j +1] = self.list_queue[j+1], self.list_queue[j]

    def enqueue(self, name):

        self.list_queue.append(name)
        self.bubble_sort()

    def printQueue(self):
        print(self.list_queue)

    def seeDoctor(self):
        removed = self.list_queue[0][:-1]
        self.list_queue = self.list_queue[1:]
        print(removed)


v1 = task()
for i in range(len(list_1)):
    if list_1[i] != "see doctor":

        v1.enqueue(list_1[i])

        v1.printQueue()
    else:
        v1.seeDoctor()
        v1.printQueue()





# Task 4(b)


file_1 = open("input4.txt", "r")


x = file_1.read()

list_1 = x.split("\n")


print(list_1)


class task_2:

    def __init__(self):
        self.list_queue = []

    def swim(self, name):
        if name not in self.list_queue:
            self.list_queue.append(name)
        index = self.list_queue.index(name)

        if index == 0:
            return
        else:
            scaled = index + 1
            parent = self.list_queue[(scaled//2)-1]

            if parent[-1] <= name[-1]:

                return
            else:
                self.list_queue[(
                    scaled//2)-1], self.list_queue[index] = self.list_queue[index], self.list_queue[(scaled//2)-1]

                if scaled//2 == (scaled//2) and (scaled-1)//2 == (scaled//2):
                   self.list_queue[index -1], self.list_queue[index] = self.list_queue[index], self.list_queue[index-1]

                self.swim(name)
                return



    def printQueue(self):
        print(self.list_queue)

    def seeDoctor(self):
        self.list_queue[0], self.list_queue[-1] = self.list_queue[-1], self.list_queue[0]
        x = self.list_queue[-1]
        self.list_queue = self.list_queue[:-1]
        print(x)
        self.sink(1)

    def sink(self, scaled):
        if len(self.list_queue) == 0:
            return
        else:
            left = (2*scaled) - 1
            right = (2*scaled+1) - 1
            if left < len(self.list_queue) and right < len(self.list_queue):
                if self.list_queue[left][-1] <= self.list_queue[right][-1]:
                    if self.list_queue[left][-1] <= self.list_queue[scaled-1][-1]:
                        self.list_queue[scaled - 1], self.list_queue[left] = self.list_queue[left], self.list_queue[scaled-1]
                        self.sink(left+1)
                else:
                    if self.list_queue[right][-1] <= self.list_queue[scaled-1][-1]:
                        self.list_queue[scaled -1], self.list_queue[right] = self.list_queue[right], self.list_queue[scaled-1]
                        self.sink(right+1)

            elif left < len(self.list_queue) and right > len(self.list_queue):
                if self.list_queue[left][-1] <= self.list_queue[scaled-1][-1]:
                    self.list_queue[scaled -1], self.list_queuen[left] = self.list_queue[left], self.list_queue[scaled-1]


v2 = task_2()
for i in range(len(list_1)):
    if list_1[i] != "see doctor":
        v2.swim(list_1[i])
        v2.printQueue()
    else:
        v2.seeDoctor()
        v2.printQueue()


"""
4c) There is a difference in the final output and it is because the heap sort is not a stable algorithm and when there are
    multiple same values , they get scrambled up and does not remain in their original order.


"""
