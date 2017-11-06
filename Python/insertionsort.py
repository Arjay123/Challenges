# def sort(a):
#     # start at key=index 1
#     # while key > keyindex-1, swap
#     # increment key
#     if len(a) <= 1:
#         return a

#     key = 1
#     for key in range(0, len(a)):

#         curr = key
#         prev = key-1

#         while curr > 0 and a[curr] < a[prev]:
#             a[prev] = a[prev] ^ a[curr]
#             a[curr] = a[curr] ^ a[prev]
#             a[prev] = a[curr] ^ a[prev]

#             curr -= 1
#             prev -= 1
            
#     return a


# a = [1, 2, 3, 6, 5, 3 ,2 , 7, 8]
# print sort(a)

# """
# swap:

# x = 3, bin(x) = 101
# y = 2, bin(y) = 010

# 1). x = 111
# 2). y = 101
# 3). x = 010
# """

def insertionsort(a):
    if len(a) <= 1:
        return a

    for key in range(1, len(a)):
        prev = key
        curr = key-1
        while prev > 0 and a[prev] < a[curr]:
            a[prev] = a[prev] ^ a[curr]
            a[curr] = a[curr] ^ a[prev]
            a[prev] = a[curr] ^ a[prev]

            curr -= 1
            prev -= 1


    return a


print insertionsort([3, 1, 2, 6, 8])