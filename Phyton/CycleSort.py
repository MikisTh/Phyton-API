def cycle_sort(array):
   
    for currentIndex in range(0, len(array) - 1):       
        item = array[currentIndex];

        currentIndexCopy = currentIndex;       
        for i in range(currentIndex + 1, len(array)):
            if array[i] < item: currentIndexCopy += 1
            i += 1
        
        if currentIndexCopy == currentIndex:
            currentIndex += 1
            continue
    
        while item == array[currentIndexCopy]: currentIndexCopy += 1

        temp = array[currentIndexCopy]
        array[currentIndexCopy] = item
        item = temp
       
        while currentIndexCopy != currentIndex:

            currentIndexCopy = currentIndex
           
            i = currentIndex + 1
            while i < len(array):
                if array[i] < item: currentIndexCopy += 1
                i += 1
      
            while item == array[currentIndexCopy]: currentIndexCopy += 1

            temp = array[currentIndexCopy]
            array[currentIndexCopy] = item
            item = temp

        currentIndex += 1

if __name__ == '__main__':
    array = [12, 11, 15, 10, 9, 1, 2, 3, 13, 14, 4, 5, 6, 7, 8]
    cycle_sort(array)
    print(array)
