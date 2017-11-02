# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem


def RemoveDuplicates(head):
    if not head:
        return
    
    nex = head.next
    while nex and nex.data == head.data:
        nex = nex.next
    head.next = RemoveDuplicates(nex)
    return head