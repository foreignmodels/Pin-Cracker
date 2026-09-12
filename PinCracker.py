# PinCracker.py
# https://cs50.harvard.edu/college/2021/fall/notes/cybersecurity/
# https://docs.python.org/3/library/itertools.html
# https://docs.python.org/3/library/time.html#module-time

import random
import time

pin = random.randint(0000, 10000) # Generates a random pin between 0000 and 9999
print (f"Generated pin: {pin:04d}") # Prints random pin with 4 digits

def brute_force(pin):
    import itertools

    start_time = time.perf_counter() # Starts a timer to see how long it takes for brute force to crack the pin
    attempts = 0 # Counts how many attempts it takes to brute force the pin

    for attempt in itertools.product(range(0, 10), repeat=4): # Gets all possible 4 digit combinations and creates tuples for each of them
        attempts += 1 # Adds 1 to the brute force attempt counter
        attempt_pin = ''.join(map(str, attempt)) # Converts tuple to string
        if int(attempt_pin) == pin: # Checks if the guessed pin matches the generated pin
            end_time = time.perf_counter() # Ends timer for brute force
            duration = end_time - start_time # Calculates brute force time
            print(f"Pin cracked: {attempt_pin}") # Prints the cracked pin
            print(f"Brute force attempts: {attempts}") # Prints number of brute force attempts
            print(f"Brute force time: {duration:.6f} seconds") # Prints brute force time
            return attempts, duration # Returns brute force attempts and time

def random_guess(pin):
    attempts = 0 # Counts how many times a random pin is guessed
    start_time = time.perf_counter() # Starts a timer to see how long it takes for random guessing to crack the pin

    while True:
        attempts += 1 # Increases random guess attempt counter
        guess_pin = random.randint(0000, 10000) # Generates a random pin between 0000 and 9999
        if guess_pin == pin: # Checks if the guessed pin matches the generated pin
            end_time = time.perf_counter() # Ends timer for random guessing
            duration = end_time - start_time # Calculates random guessing time
            print(f"Pin cracked: {guess_pin:04d}") # Prints the cracked pin with 4 digits
            print(f"Random guess attempts: {attempts}") # Prints number of random guess attempts
            print(f"Random guess time: {duration:.6f} seconds") # Prints random guessing time
            return attempts, duration # Returns random guess attempts and time

# Runs both methods and compares their performance
bf_attempts, bf_time = brute_force(pin)
rg_attempts, rg_time = random_guess(pin)

# Comparing the performance of brute force and random guessing
print("\nComparison:")
print(f"Generated PIN:        {pin:04d}")
print(f"Brute force attempts: {bf_attempts}")
print(f"Brute force time:     {bf_time:.6f} seconds")
print(f"Random attempts:      {rg_attempts}")
print(f"Random time:          {rg_time:.6f} seconds")
