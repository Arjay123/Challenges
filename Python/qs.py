"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        print(str(pivot) + ":", array[pivot], array)
        if start < pivot - 1: quicksort(array, start, pivot-1)
        if end > pivot: quicksort(array, pivot, end)
    return array


def partition(arr, start, end):
    mid = (end + start)/2
    pivot = arr[mid]
    left = start
    right = end
    while left <= right:
        while arr[left] < pivot:
            left = left + 1
        while arr[right] > pivot:
            right = right - 1

        if left <= right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1

    return left


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test, 0, len(test) - 1)
