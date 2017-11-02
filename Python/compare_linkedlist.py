# https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
def CompareLists(headA, headB):
    if not headA and not headB:
        return 1
    
    if not headA or not headB or headA.data != headB.data:
        return 0
    
    return CompareLists(headA.next, headB.next)
  