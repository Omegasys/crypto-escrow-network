import random
import time

def apply_random_delay(min_delay=1, max_delay=9):
    """Applies a random time delay between min_delay and max_delay."""
    delay = random.randint(min_delay, max_delay)
    time.sleep(delay)
    print(f"Applied a random delay of {delay} seconds.")
