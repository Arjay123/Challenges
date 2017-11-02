# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

def MergeLists(headA, headB):
    if not headA and not headB:
        return
    
    if not headA:
        return headB
    
    if not headB:
        return headA
    
    if headA.data < headB.data:
        small = headA
        small.next = MergeLists(headA.next, headB)
    else:
        small = headB
        small.next = MergeLists(headA, headB.next)
    return small