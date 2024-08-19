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
