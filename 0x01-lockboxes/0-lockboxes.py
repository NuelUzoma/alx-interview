#!/usr/bin/python3
"""
This is a function that determines if boxes with same keys can be opened
Box is a list of lists
Assume all keys are positive integers
"""


def canUnlockAll(boxes):
    """The function prototype for the program"""
    n = len(boxes)
    first_box = set([0])
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < n and key not in first_box:
                first_box.add(key)
                queue.append(key)

    return len(first_box) == n
