class Wallet:
    def __init__(self, balance=0.0, address=None):
        self.balance = balance
        self.address = address if address else "1A2b3C4d5E6f7G8h9I0j1K2L3M4n5P6q7R8S9T0"

    def create_wallet(self, initial_balance=0.0):
        """Creates a new wallet with an initial balance."""
        self.balance = initial_balance
        print(f"New wallet created with address: {self.address} and balance: {self.balance}")
        return self

    def transfer(self, recipient_wallet, amount):
        """Transfers cryptocurrency to another wallet."""
        if self.balance >= amount:
            self.balance -= amount
            recipient_wallet.balance += amount
            print(f"Transferred {amount} to {recipient_wallet.address}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        """Returns the current balance of the wallet."""
        return self.balance
