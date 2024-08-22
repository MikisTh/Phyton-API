def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
                if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)

def selectionSort(arr):
   # Iterate the entire array, except the last element.
   for i in range(len(arr) - 1):
       min = i
       # Iterate the remaining array
       for j in range(i + 1, len(arr)):
           if arr[j] < arr[min]:
               min = j
       # In place  swap
       tmp = arr[min]
       arr[min] = arr[i]
       arr[i] = tmp
