list_1  = [1,6,12,7,2,9,4,3,9,5,8]


for i in range(len(list_1)-1):
    for j in range(len(list_1)-i-1):
        if list_1[j] > list_1[j+1]:
            fix = list_1[j]
            list_1[j] = list_1[j+1]
            list_1[j+1] = fix

print(list_1)
#  Binary Search
target =5
x = 0
y = len(list_1)-1
while x<=y:
    mid_index =(x+y)//2
    if list_1[mid_index]== target:
        print(mid_index)
        break
    elif list_1[mid_index] > target:
        y = mid_index -1

    else:
        x = mid_index+1


# Linear search 
for i in list_1:
    if i == target:
        print(i)
    
        
# Selection sort

for i in range(len(list_1)-1):
  min = list_1[i]
  min_index = i
  for j in range(i+1,len(list_1)):
    if list_1[j] < min:
      min = list_1[j]
      min_index = j
  
  list_1[min_index] = list_1[i]
  list_1[i] = min

