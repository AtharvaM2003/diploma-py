def selection(array,size):
    for i in range(size):
        min=i
        for j in range (i+1,size):
            if array[j]<array[min]:
                min=j
        (array[i],array[min])=(array[min],array[i])

arr=[10,20,2,5,13]
size=len(arr)
selection(arr,size)
print("Sorted Element: ",arr)
