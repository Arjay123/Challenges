import random

def quicksort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, end)

def partition(arr, start, end):

    # get random pivot
    i = random.randrange(start, end+1)

    # swap pivot w/ end element
    swap(arr, i, end)

    i = start - 1
    pivot = arr[end]
    for j in range(start, end+1):
        if arr[j] < pivot:
            i = i+1
            swap(arr, i, j)
    swap(arr, i+1, end)
    return i+1


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14, 2]
quicksort(test, 0, len(test) - 1)
print(test)

s = "test"
print s[0]