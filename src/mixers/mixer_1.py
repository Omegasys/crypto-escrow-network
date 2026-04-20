import random
import time
from wallet_2A_6F import MixerWallet
from mixer_utils import apply_delay

class Mixer1:
    def __init__(self, io_ports=32, delay_range=(1, 9)):
        self.io_ports = io_ports
        self.delay_range = delay_range
        self.wallets = [MixerWallet(balance=0.0, address=f"Mixer1 Wallet {i}") for i in range(1, io_ports+1)]

    def mix(self, amount, sender_wallet):
        """Mixes funds by transferring to one of the IO ports and applying delay."""
        target_wallet = random.choice(self.wallets)
        apply_delay(self.delay_range)
        sender_wallet.transfer(target_wallet, amount)
        print(f"Transferred {amount} from {sender_wallet.address} to {target_wallet.address} in Mixer 1")
        return target_wallet
