# PinCracker.py
# https://cs50.harvard.edu/college/2021/fall/notes/cybersecurity/
# https://docs.python.org/3/library/itertools.html
# https://docs.python.org/3/library/time.html#module-time
# https://codereview.stackexchange.com/questions/213313/brute-force-password-cracker-in-python

import random
import time

pin = random.randint(0000, 9999)
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
            return attempts, duration

def random_guess(pin):
    attempts = 0
    start_time = time.perf_counter()

    guesses = list(range(0000, 10000))
    random.shuffle(guesses)

    for guess_pin in guesses:
        attempts += 1
        if guess_pin == pin:
            end_time = time.perf_counter()
            duration = end_time - start_time
            return attempts, duration

def run_trials(test_trials, possible_pins):
    bf_total = 0
    rg_total = 0

    for _ in range(test_trials):
        trial_pin = random.randint(0, possible_pins - 1)
        bf_attempts, _ = brute_force(trial_pin)
        rg_attempts, _ = random_guess(trial_pin)
        bf_total += bf_attempts
        rg_total += rg_attempts

    return bf_total / test_trials, rg_total / test_trials

def expected_attempts_gaussian(N):
    return (N + 1) / 2

# Runs both methods
bf_attempts, bf_time = brute_force(pin)
rg_attempts, rg_time = random_guess(pin)

# Comparing the performance of brute force and random guessing
expected = expected_attempts_gaussian(10000)
print("\nComparison:")
print(f"Brute force attempts: {bf_attempts}")
print(f"Brute force time: {bf_time:.6f} seconds")
print(f"Random attempts: {rg_attempts}")
print(f"Random time: {rg_time:.6f} seconds")
print("\nTheory vs. Simulation:")
print(f"Expected avg attempts: {expected:.1f} (Expected Guesses: (n+1)/2)")
print("\nMonte Carlo check:")
for num_trials in (10, 100, 1000, 3000, 5000):
    bf_avg, rg_avg = run_trials(num_trials, 10000)
    print(f"{num_trials:>5} trials -> brute force avg: {bf_avg:>8.1f}   random avg: {rg_avg:>8.1f}")