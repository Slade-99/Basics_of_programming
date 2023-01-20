# Task 3


flag = False


def bubbleSort(arr):
  for i in range(len(arr)-1):

    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        flag = True

        arr[j], arr[j+1] = arr[j+1], arr[j]

    if not flag:
      return


"""As a flag is being used so in the first complete traversal of the inner loop
   if it is found that there are no swappings then the outer loop stops and hence
   the operation comes to an end. So, the list has only been traversed n-1 times and hence
   the time complexity for best case will be Theta(n) """
