# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

def has_cycle(head):
    nex = head.next
    while nex and nex.next:
        if head == nex:
            return True
        head = head.next
        nex = nex.next.next
    return False
    