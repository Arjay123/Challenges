# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

def FindMergeNode(headA, headB):
    stackA = []
    stackB = []
    
    while headA:
        stackA.append(headA.data)
        headA = headA.next
        
    while headB:
        stackB.append(headB.data)
        headB = headB.next
    
    merge = None
    while stackA[-1] == stackB[-1]:
        merge = stackA.pop()
        stackB.pop()
        
    return merge