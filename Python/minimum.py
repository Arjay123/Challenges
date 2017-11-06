def mini(arr, lo=0, hi=None):
    if not hi:
        hi = len(arr) - 1

    if hi < lo:
        return -1
        
    if lo == hi:
        return arr[lo]

    mid = (hi-lo)/2 + lo

    if arr[mid] < arr[mid-1]:
        print "A"
        return arr[mid]
    elif arr[hi] < arr[mid]:
        print "B"
        return mini(arr, mid+1, hi)
    else:
        print "C"
        return mini(arr, lo, mid-1)

arr = [3,4,5,1,2]
print mini(arr), arr

arr = [1,2,3,4,5]
print mini(arr), arr

arr = [2,3,4,5,1]
print mini(arr), arr

arr = []
print mini(arr), arr