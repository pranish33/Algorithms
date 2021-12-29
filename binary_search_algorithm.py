#defining function for the binary search 
def binary_search_algorithm(list, target):
    #Creating variable for last and first element in array
    first = 0
    last = len(list) - 1
    #comparing first and last element 
    
    while first <= last:
        # Initialing mid-point element and search for the searched element  
        midpoint = (first+last) // 2

        if list[midpoint] == target:
            return midpoint

        elif list[midpoint] < target:
            first =  midpoint+1

        else:
            last = midpoint-1

    return None

#another method for verifying binary_search_algorithm
def verify(index):
    if index is not None:
        print("Target found at index", index)

    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = binary_search_algorithm(numbers, 9)
verify(result)