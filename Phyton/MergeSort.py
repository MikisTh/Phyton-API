def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2 
        left_array = array[:middle]  
        right_array = array[middle:]  
        merge_sort(left_array) 
        merge_sort(right_array)

        left_index = 0
        right_index = 0
        current_index = 0
 
        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index] < right_array[right_index]:
                array[current_index] = left_array[left_index]
                left_index += 1
            else:
                array[current_index] = right_array[right_index]
                right_index += 1
            current_index += 1
 
        while left_index < len(left_array):
            array[current_index] = left_array[left_index]
            left_index += 1
            current_index += 1
    
        while right_index < len(right_array):
            array[current_index] = right_array[right_index]
            right_index += 1
            current_index += 1

if __name__ == '__main__':
    array = [12, 11, 15, 10, 9, 1, 2, 3, 13, 14, 4, 5, 6, 7, 8]
    merge_sort(array)
    print(array)

// 
# Helper merge sort function
def mergeSort(arr):
   # Clone the array for the merge later
   arrClone = arr.clone()
   mergeSortAux(arr, arrClone, 0, len(arr) - 1)

# Actual merge sort 
def mergeSortAux(arr, arrClone, low, high):
   if low < high:
       mid = (low + high) / 2
       # Sort left
       mergeSortAux(arr, arrClone, low, mid)
       # Sort right
       mergeSortAux(arr, arrClone, mid + 1, high)
       # Merge
       merge(arr, arrClone, low, mid, high)

# Merge definition that sorts two sub arrays
def merge(arr, arrClone, low, mid, high):
   i = low
   j = mid + 1
   # Copy the clone array parts over
   for k in range(low, high):
       arrClone[k] = arr[k]

   for k in range(low, high):
       if i > mid:
           arr[k] = arrClone[j]
           j += 1
       elif j > high:
           arr[k] = arrClone[i]
           i += 1
       elif arrClone[i] > arrClone[j]:
           arr[k] = arrClone[j]
           j += 1
       else:
           arr[k] = arrClone[i]
           i += 1
