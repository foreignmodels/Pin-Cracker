# PinCracker.py
# https://cs50.harvard.edu/college/2021/fall/notes/cybersecurity/
# https://docs.python.org/3/library/itertools.html
# https://docs.python.org/3/library/time.html#module-time
# https://codereview.stackexchange.com/questions/213313/brute-force-password-cracker-in-python

import random
import time

pin = random.randint(0000, 10000)
print (f"Generated pin: {pin:04d}")

def brute_force(pin):
    import itertools

    start_time = time.perf_counter() # Timer for brute force
    attempts = 0 # Attempts for brute force

    for attempt in itertools.product(range(0, 10), repeat=4): # Gets all possible 4 digit combinations and creates tuples for each of them
        attempts += 1
        attempt_pin = ''.join(map(str, attempt)) # Converts tuple to string
        if int(attempt_pin) == pin:
            end_time = time.perf_counter()
            duration = end_time - start_time
            print(f"Brute force attempts: {attempts}")
            print(f"Brute force time: {duration:.6f} seconds")
            return attempts, duration

def random_guess(pin):
    attempts = 0
    start_time = time.perf_counter()

    guesses = list(range(0, 10000))
    random.shuffle(guesses)

    for guess_pin in guesses:
        attempts += 1
        if guess_pin == pin:
            end_time = time.perf_counter()
            duration = end_time - start_time
            print(f"Random guess attempts: {attempts}")
            print(f"Random guess time: {duration:.6f} seconds")
            return attempts, duration

def expected_attempts_gaussian(keyspace_size):
    # Average attempts to find 1 specific value among N equally likely
    # values = average of 1, 2, 3, ... N = Gaussian sum / N = (N+1)/2
    return (keyspace_size + 1) / 2

# Runs both methods
bf_attempts, bf_time = brute_force(pin)
rg_attempts, rg_time = random_guess(pin)

# Comparing the performance of brute force and random guessing
expected = expected_attempts_gaussian(10000)
print("\nComparison:")
print(f"Generated PIN:        {pin:04d}")
print(f"Brute force attempts: {bf_attempts}")
print(f"Brute force time:     {bf_time:.6f} seconds")
print(f"Random attempts:      {rg_attempts}")
print(f"Random time:          {rg_time:.6f} seconds")
print(f"Expected avg attempts:    {expected:.1f}  (Gaussian summation: (N+1)/2)")