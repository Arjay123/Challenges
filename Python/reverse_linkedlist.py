"""
 https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
 
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    """
    Iterative
    ---------
    
    curr, prev = head, None
    while curr:
        nex = curr.next
        curr.next = prev
        prev = curr
        curr = nex
    return prev
    """
    
    return ReverseUtil(head)
    
    

def ReverseUtil(curr, prev=None):
    nex = curr.next
    curr.next = prev
    
    if not nex:
        return curr
    return ReverseUtil(nex, curr)
    
        


  
  
  
  
  
  
