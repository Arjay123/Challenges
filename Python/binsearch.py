def search(arr, key):
    lo = 0
    hi=len(arr)-1
    while hi >= lo:
        mid = ((hi-lo)/2) + lo
        if arr[mid] < key:
            lo = mid+1
        elif arr[mid] > key:
            hi = mid-1
        else:
            return mid
    return -1

def search_re(arr, key, lo=0, hi=None):
    if not hi:
        hi = len(arr)-1

    if hi < lo:
        return -1

    mid = ((hi-lo)/2) + lo
    if arr[mid] < key:
        return search_re(arr, key, mid+1, hi)
    elif arr[mid] > key:
        return search_re(arr, key, lo, mid-1)
    else:
        return mid



arr = [1,2,3,4,5]

