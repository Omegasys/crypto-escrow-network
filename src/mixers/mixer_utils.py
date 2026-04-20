import random
import time

def apply_delay(delay_range):
    """Applies a random delay between `delay_range[0]` and `delay_range[1]` seconds."""
    delay = random.randint(delay_range[0], delay_range[1])
    time.sleep(delay)
    print(f"Applied a random delay of {delay} seconds.")
