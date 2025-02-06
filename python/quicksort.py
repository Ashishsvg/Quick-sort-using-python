def quick_sort(arr):
    # Base case: if the list is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot element (here, we choose the last element as pivot)
    pivot = arr[-1]
    
    # Partition the list into two sub-arrays: one with elements smaller than pivot
    # and one with elements greater than pivot
    smaller = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    
    # Recursively sort the sub-arrays and combine them with the pivot
    return quick_sort(smaller) + [pivot] + quick_sort(greater)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print(f"Sorted array: {sorted_arr}")
