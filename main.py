import timeit
import random




#https://chat.openai.com/share/660da20c-99f6-4e15-9d37-00519578ae21
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr




# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position





def add_times(n,insertion_times,merge_times):
        # https://www.geeksforgeeks.org/generating-random-number-list-in-python/

        rand_lst = []
        for i in range(n):
            rand_lst.append(random.randint(0,n))


        #copy of the list for merge sort to be called on

        rand_lst_copy = rand_lst.copy()

        #backup lst to have the sorts recall for each iteration within the timer loop

        backup_lst = rand_lst.copy()

        total_merge_time = 0
        for i in range(1000):
            sorted_lst = merge_sort(rand_lst)


            #https://chat.openai.com/share/f0bf813a-e992-492d-95b4-63ca8ce34069
            total_merge_time += timeit.timeit(lambda: merge_sort(rand_lst), number=1)




        merge_times.append(total_merge_time)

        total_insert_time = 0
        for i in range(1000):
            rand_lst_copy = backup_lst[:]
            total_insert_time += timeit.timeit(lambda: insertionSort(rand_lst_copy), number=1)

        insertion_times.append(total_insert_time)



def main():
    insertion_times= []
    merge_times = []

    num_values = []

    for i in range(0,1000,25):
        add_times(i, insertion_times, merge_times)
        num_values.append(i)






    print(insertion_times)
    print(merge_times)
    print(num_values)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()