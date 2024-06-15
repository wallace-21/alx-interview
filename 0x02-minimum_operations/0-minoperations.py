#!/usr/bin/python3

"""declare a function minOperations"""


def minOperations(n):
    """a function given calculates the min
       number of operations needed
       Returns:
         - returns the sum of prime factors
           of (n)
    """

    """ stores the prime numbers used to divide (n) with
    """
    prime_used = []
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 29, 31, 37, 41, 43, 47]

    if n == 0 or n < 0:
        return (0)

    for prime in primes:
        while n % prime == 0:

            prime_used.append(prime)
            n //= prime

        if n == 1:
            break
    return(sum(prime_used))
