# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

'''
To implement a queue w/ two stacks, we have two stacks: one for enqueue and
one for dequeue.

1. Performing enqueue is simple, simply push the new element into the enqueue
stack.

2. To perform a dequeue, we need to retrieve the element that is at the front
of the queue, when translated to our stack it is the element that is at the
back (or bottom) of the stack. In order to retrieve this element and preserve
the order, we pop all elements from the enqueue stack and push them into the
dequeue stack.

Note that we should only 'empty' the enqueue stack if the dequeue stack is
empty to presere queue order.

Then to dequeue we simply pop from the dequeue stack.

3. To perform a peek we follow the same logic as a dequeue, but instead return
the first element in the dequeue stack without popping it out.

Optimizations:
    - Since dequeue and peek both require emptying of the enqueue stack, we
      can perform the 'emptying' code if we know that the query is not an
      enqueue

Assumptions:
    - It is guaranteed that a valid answer always exists for each peek query
        - If we were to take this assumption away, we can check if the dequeue
          stack contains elements before performing a peek or dequeue query


'''
en_stack = []
de_stack = []

q = int(raw_input())
for _ in range(q):
    query = map(int, raw_input().split(' '))

    if query[0] == 1: #enqueue
        en_stack.append(query[1])
    else:
        if not de_stack:
            while en_stack:
                de_stack.append(en_stack.pop())

        if query[0] == 2: #dequeue
            de_stack.pop()
        else: #peek
            print de_stack[-1]