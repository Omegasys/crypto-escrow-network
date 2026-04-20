import time
from wallet_2A_6F import MixerWallet

class Mixer:
    def __init__(self, io_ports=32, delay_range=(1, 9)):
        self.io_ports = io_ports
        self.delay_range = delay_range

    def apply_delay(self):
        """Applies a random delay between 1 and 9 seconds to hinder time-based attacks."""
        delay = random.randint(self.delay_range[0], self.delay_range[1])
        time.sleep(delay)
        print(f"Applied delay of {delay
