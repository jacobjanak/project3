"""
guitar_string.py

Models a guitar string.
"""

import math
import random
import ring_buffer
import stdarray
import stdio
import sys

# Sampling rate.
SPS = 44100


def create(frequency):
    """
    Create and return a guitar string of the given frequency, using a sampling
    rate given by SPS. A guitar string is represented as a ring buffer of
    of capacity N (SPS divided by frequency, rounded up to the nearest
    integer), with all values initialized to 0.0.
    """

    rb = ring_buffer.create(math.ceil(SPS / frequency))

    # replace all the None values in the buffer with 0.0
    for i in range(len(rb[0])):
        rb[0][i] = 0.0

    # Initialize size and the first and last values to index 0
    rb[1] = len(rb[0])
    rb[2] = 0
    rb[3] = 0

    return rb


def create_from_samples(init):
    """
    Create and return a guitar string whose size and initial values are given
    by the list init.
    """

    # create the string
    string = ring_buffer.create(len(init))

    # Replace the values within the buffer with sample value
    for i in range(len(string[0])):
        string[0][i] = init[i]

    # Initialize size and the first and last values to index 0
    string[1] = len(init)
    string[2] = 0
    string[3] = 0

    return string


def pluck(string):
    """
    Pluck the given guitar string by replacing the buffer with white noise.
    """

    for i in range(ring_buffer.capacity(string)):
        string[0][i] = random.random() - 0.5


def tic(string):
    """
    Advance the simulation one time step on the given guitar string by applying
    the Karplus-Strong update.
    """

    # get values of the first two elements in the buffer
    value1 = ring_buffer.dequeue(string)
    value2 = ring_buffer.peek(string)

    # apply the Karplus-Strong update
    ring_buffer.enqueue(string, .996 / 2 * (value1 + value2))


def sample(string):
    """
    Return the current sample from the given guitar string.
    """

    return ring_buffer.peek(string)


def _main():
    """
    Test client [DO NOT EDIT].
    """

    N = int(sys.argv[1])
    samples = [.2, .4, .5, .3, -.2, .4, .3, .0, -.1, -.3]
    test_string = create_from_samples(samples)
    for t in range(N):
        stdio.writef('%6d %8.4f\n', t, sample(test_string))
        tic(test_string)


if __name__ == '__main__':
    _main()
