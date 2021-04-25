"""
Stack to queue converter.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack
from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    '''
    Convert stack to queue
    '''
    res = ArrayQueue()
    temp = []
    for item in stack:
        temp.append(item)

    for i in range(len(temp)-1, -1, -1):
        res.add(temp[i])

    return res
