"""
ring_buffer.py

Models a ring buffer.
"""

import stdarray
import stdio
import sys


def create(capacity):
    """
    Create and return a ring buffer, with the given maximum capacity and
    with all elements initialized to None. A ring buffer is represented as
    a list of four elements: the buffer (buff) itself as a list; number of
    elements (size) currently in buff; the index (first) of the least
    recently inserted item; and the index (last) one beyond the most recently
    inserted item.
    """

    return [stdarray.create1D(capacity, None), None, None, None]


def capacity(rb):
    """
    Return the capacity of the ring buffer.
    """

    return len(rb[0])


def size(rb):
    """
    Return the number of items currently in the buffer rb.
    """

    return rb[1]


def is_empty(rb):
    """
    Return True if the buffer rb is empty and False otherwise.
    """

    return size(rb) == 0


def is_full(rb):
    """
    Return True if the buffer rb is full and False otherwise.
    """

    return size(rb) == capacity(rb)


def enqueue(rb, x):
    """
    Add item x to the end of the buffer rb.
    """

    if is_full(rb):
        sys.exit("Error: cannot enqueue a full buffer")

    # size, first and last are 'None' when buffer is empty
    if rb[1] is None:
        rb[1] = 0
    if rb[2] is None:
        rb[2] = 0
    if rb[3] is None:
        rb[3] = 0

    # add x to buffer at the last index
    rb[0][rb[3]] = x

    # increment size
    rb[1] += 1

    # increment last cyclically
    rb[3] += 1
    if rb[3] >= capacity(rb):
        rb[3] = 0


def dequeue(rb):
    """
    Delete and return item from the front of the buffer rb.
    """

    if is_empty(rb):
        sys.exit("Error: cannot dequeue an empty buffer")

    # get the value of the item at the first index and delete it
    item = rb[0][rb[2]]
    rb[0][rb[2]] = None

    # decrement size
    rb[1] -= 1

    # increment first cyclically
    rb[2] += 1
    if rb[2] >= capacity(rb):
        rb[2] = 0

    # Reset first and last to None if buffer is empty (not necessary)
    if (is_empty(rb)):
        rb[1] = None
        rb[2] = None
        rb[3] = None

    return item


def peek(rb):
    """
    Return (but do not delete) item from the front of the buffer rb.
    """

    if is_empty(rb):
        sys.exit("Error: cannot peek an empty buffer")

    return rb[0][rb[2]]


def _main():
    """
    Test client [DO NOT EDIT].
    """

    N = int(sys.argv[1])
    rb = create(N)
    for i in range(1, N + 1):
        enqueue(rb, i)
    t = dequeue(rb)
    enqueue(rb, t)
    stdio.writef('Size after wrap-around is %d\n', size(rb))
    while size(rb) >= 2:
        x = dequeue(rb)
        y = dequeue(rb)
        enqueue(rb, x + y)
    stdio.writeln(peek(rb))


if __name__ == '__main__':
    _main()
