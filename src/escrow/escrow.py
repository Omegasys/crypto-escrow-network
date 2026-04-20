from wallet_internal import InternalWallet
from wallet_2A_6F import MixerWallet

class Escrow:
    def __init__(self, buyer_wallet: InternalWallet, seller_wallet: InternalWallet):
        self.buyer_wallet = buyer_wallet
        self.seller_wallet = seller_wallet
        self.escrow_balance = 0.0
        self.locked = False

    def lock_funds(self, amount: float):
        """Locks funds in escrow from the buyer's wallet."""
        if self.buyer_wallet.get_balance() >= amount:
            self.buyer_wallet.transfer(self, amount)  # Transferring funds to escrow
            self.escrow_balance += amount
            self.locked = True
            print(f"Funds of {amount} locked in escrow.")
        else:
            print("Insufficient funds in buyer's wallet to lock funds.")

    def release_funds(self):
        """Releases funds to the seller after confirming conditions."""
        if self.locked:
            self.seller_wallet.deposit(self.escrow_balance)
            print(f"Released {self.escrow_balance} to seller.")
            self.escrow_balance = 0.0
            self.locked = False
        else:
            print("No funds are locked in escrow.")

    def cancel_escrow(self):
        """Cancels escrow and returns funds to the buyer."""
        if self.locked:
            self.buyer_wallet.deposit(self.escrow_balance)
            print(f"Escrow canceled. {self.escrow_balance} returned to buyer.")
            self.escrow_balance = 0.0
            self.locked = False
        else:
            print("No funds are locked in escrow.")
