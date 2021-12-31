def selection_sort(num):
    for i in range(0, len(num)-1):
        midIndex = i
        for j in range(i+1, len(num)):
            if num[j] < num[minIndex]:
                minIndex= j
        if minIndex != i:
            num[i], num[minIndex] = num[minIndex], num[i]
            
            
num = [1,7,5,3,2,4,6,8,9]
selection_sort(num)
print(num)