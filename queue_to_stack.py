"""
Queue to stack converter.
"""

from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack    # or from linkedstack import LinkedStack


def queue_to_stack(queue):
    '''
    Convert queue to stack
    '''
    res = ArrayStack()
    temp = []
    for item in queue:
        temp.append(item)

    for i in range(len(temp)-1, -1, -1):
        res.add(temp[i])

    return res
