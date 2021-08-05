def linear_search(list, target):

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

     


def verify(index):

    if index is not None:
        print("The Target found at index: ", index)

    else:
        print("The Target not found. ")


numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 8)

verify(result)
        