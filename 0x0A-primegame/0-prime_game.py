#!/usr/bin/python3

"""define is winner"""


def isWinner(x, nums):
    """
        Determines the winner of a series of prime game rounds.

        In each round, Maria and Ben take turns to pick prime
        numbers starting from the smallest.
        All multiples of the chosen prime are removed from the
        list of available numbers.
        The player who cannot make a move loses the round.

        Parameters:
                x (int): The number of rounds to be played.
                nums (list): A list of integers, where each integer
                represents the maximum number in the range for each round.

        Returns:
            str: The name of the player with the most wins ("Maria" or "Ben").
            If there's a tie, returns None.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)

    """
        Generate a list of prime numbers up to
        max_n using the Sieve of Eratosthenes
    """
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    """
        Count primes up to each number
    """
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if prime_counts[num] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
