def bubbleSort(arr):
    """
    This function will sort a list of array using bubble sort algorithm 
    Input parameter list 
    Return value: None
    """
    for i in range(len(arr)-1, 0, -1):
        swap = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                swap = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if swap == False:
            break


arr = [5, 4, 3, 2, 1]
bubbleSort(arr)
print("Array after sorting using bubble sort algorithm: ", arr)
