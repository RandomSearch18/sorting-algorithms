"""An implementation of quick sort, based on the pseudocode provided in the "Implementing Quick Sort" lesson"""

def partition(array: list, start: int, end: int):
    pivot_pointer = start
    pivot = array[start]

    left_pointer = start + 1
    right_pointer = end

    done = False
    while not done:
        while left_pointer <= right_pointer and array[left_pointer] <= pivot:
            # Slide to the right
            left_pointer += 1
        
        while array[right_pointer] >= pivot and right_pointer >= left_pointer:
            # Slide to the left
            right_pointer -= 1

        if right_pointer < left_pointer:
            break

        # Swap the list items
        array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
    
    # Swap the pivot with array[right_pointer]
    array[pivot_pointer], array[right_pointer] = array[right_pointer], array[pivot_pointer]

    # The item at right_pointer is now in the correct position (relative to the other items)
    return right_pointer


def quick_sort(array: list, start: int, end: int):
    """Uses the quick sort algorithm to sort the provided list in-place
    
    - Only sorts a section of the list, as specified by the `start=` and `end=` parameters.
    - Returns a reference to the sorted list

    Parameters:
    - `array` - The list to sort. Items must be compatible with the `<`and `>`operators
    - `start` - The index of the first item to be sorted
    - `end` - The index of the last item to be sorted
    """
    if start < end:
        # Partition the list
        split_point = partition(array, start, end)

        # Sort each half
        quick_sort(array, start, split_point - 1)
        quick_sort(array, split_point + 1, end)
    
    return array


if __name__ == "__main__":
    demo_list = [9, 5, 4, 15, 3, 8, 11]
    print(demo_list)
    quick_sort(demo_list, 0, len(demo_list) - 1)
    print(demo_list)
