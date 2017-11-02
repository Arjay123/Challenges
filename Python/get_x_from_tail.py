# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

def GetNode(head, position):
    mark = head
    while head:
        if position < 1 and head.next:
            mark = mark.next
        head = head.next
        position -= 1
    return mark.data
  
  