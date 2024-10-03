#!/usr/bin/python3
"""Use sieve of Eratosthens to play prime game
"""


def sieve_of_eratosthenes(n):
    """Generate/precompute prime numbers from 1 to n"""
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if primes[i] == True:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def count_number_of_primes(max_n):
    """Count the number of possible primes"""
    primes = sieve_of_eratosthenes(max_n)
    primes_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        primes_count[i] = primes_count[i - 1] + (1 if primes[i] else 0)
    return primes_count


def get_relevent_sublist(xround, nums):
    """Recursively build the sublist of test cases"""
    sublist = nums[:min(xround, len(nums))]
    if xround > len(sublist):
        sublist += nums
        return get_relevent_sublist(xround, sublist)
    return sublist


def play_game(xround, nums):
    """Play game accoring to xround"""
    max_n = max(nums[:max(xround, len(nums))])
    sublist = get_relevent_sublist(xround, nums)
    primes_count = count_number_of_primes(max_n)
    result = {'Ben': 0, 'Maria': 0}
    for n in sublist:
        if primes_count[n] % 2 == 0:
            result['Ben'] = result.get('Ben') + 1
        else:
            result['Maria'] = result.get('Maria') + 1
    return result

def isWinner(x, nums):
    """Game winner"""
    result = play_game(x, nums)
    winner = max(result, key=result.get)
    return winner
