# def merge(a, b):
#     """
#     Given two sorted arrays, returns 1 sorted array by merging the two arrays,
#     using two finger algorithm
#     """

#     aPointer = 0
#     bPointer = 0
#     merged = []

#     #compare pointer elements
#     while aPointer < len(a) and bPointer < len(b):
#         if a[aPointer] < b[bPointer]:
#             merged.append(a[aPointer])
#             aPointer += 1
#         else:
#             merged.append(b[bPointer])
#             bPointer += 1
#     return merged + a[aPointer:] + b[bPointer:]


# def sort(a):
#     if len(a) == 0 or len(a) == 1:
#         return a
#     L = sort(a[:len(a)/2])
#     R = sort(a[len(a)/2:])
#     return merge(L, R)



# a = [1, 3, 5, 7, 2, 4, 6, 8]

# print sort(a)



def mergesort(a):
    if len(a) <= 1:
        return a

    a1 = mergesort(a[:len(a)/2])
    a2 = mergesort(a[len(a)/2:])

    return merge(a1, a2)

def merge(a, b):
    """
    Combines two already sorted arrays in sorted order using two-finger method.
    Two pointers keep track of current iteration in array, performs check
    between integers and inserts smallest one into array and updates index for
    that 'pointer'
    """
    newarr = []
    aPointer = 0
    bPointer = 0

    while aPointer < len(a) and bPointer < len(b):
        if a[aPointer] < b[bPointer]:
            newarr.append(a[aPointer])
            aPointer += 1
        else:
            newarr.append(b[bPointer])
            bPointer += 1
    return newarr + a[aPointer:] + b[bPointer:]

a = [1, 8, 2, 1, 1, 22, 3, 5, 9]
b = [2, 4, 6, 8]

print mergesort(a)






















