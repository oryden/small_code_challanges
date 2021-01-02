"""
https://projecteuler.net/problem=31

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
import timeit
import sys
from functools import wraps


DENOMINATIONS = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1] # List of all possible denominations (ordering not important)

# Caching to improve performance by ~10,000
MEMO_RESULTS = {}
ACTIVATE_CACHING = True
DEBUG_CACHING = False
if ACTIVATE_CACHING and DEBUG_CACHING:
    sys.setrecursionlimit(5000)


def memo():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if ACTIVATE_CACHING:
                key = ':'.join(str(arg) for arg in list(args))
                if key in MEMO_RESULTS:
                    if DEBUG_CACHING:
                        result = f(*args, **kwargs)
                        assert(MEMO_RESULTS[key] == result)
                    else:
                        result = MEMO_RESULTS[key]
                else:
                    result = f(*args, **kwargs)
                    MEMO_RESULTS[key] = result
            else:
                result = f(*args, **kwargs)
            return result
        return decorated_function
    return decorator


@memo()
def find_combinations_of_coins(target, max_coin_amount):
    """
    Recursively find the total number of combinations of coins that can be used to add up to the total amount
    :param target: integer target amount that the coins must add up to
    :param max_coin_amount: integer largest coin available to use, to iteratively reduce to a trivial problem of 1p's
    :return: integer number of combination
    """
    # Terminate conditions
    if max_coin_amount == 1:
        return 1
    if target == 0:
        return 1
    # If not terminating then partition by the max_coin_amount and reducing it to iteratively reduce the problem
    total_combinations = 0
    next_max_coin_amount = max([coin for coin in DENOMINATIONS if coin < max_coin_amount])
    for amount_of_max_coin in range(int(target / max_coin_amount) + 1):
        new_target = target - amount_of_max_coin * max_coin_amount
        total_combinations += find_combinations_of_coins(new_target, next_max_coin_amount)
    return total_combinations


if __name__ == '__main__':

    final_combinations = find_combinations_of_coins(200, 200)
    print(final_combinations)
    print(timeit.timeit('find_combinations_of_coins(200, 200)', number=100,
                        setup="from __main__ import find_combinations_of_coins"))
