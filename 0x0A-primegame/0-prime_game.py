#!/usr/bin/python3
"""
A solution to the Prime Game problem
"""


def primes(n):
    """ Return list of prime numbers between 1 and n inclusive
    Args:
        n: upper boundary of range. lower boundary is always 1
    """
    prime = []
    siever = [True] * (n + 1)
    for p in range(2, n + 1):
        if (siever[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                siever[i] = False
    return prime


def isWinner(x, nums):
    """Determines winner of Prime Game
    Args:
        x: number of rounds of game
        nums: upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
