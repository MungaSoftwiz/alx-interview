#!/usr/bin/python3
""" Define lockboxed module """
from collections import deque


def canUnlockAll(boxes):
    """ Determines if all boxes can be opened """
    n = len(boxes)
    visited = set()
    visited.add(0)  # Mark first box as visited
    queue = deque([0])  # Start BFS from first box

    while queue:
        current_box = queue.popleft()
        keys = boxes[current_box]

        for key in keys:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == n
