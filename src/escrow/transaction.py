class Transaction:
    def __init__(self, sender_wallet, receiver_wallet, amount, status="pending"):
        self.sender_wallet = sender_wallet
        self.receiver_wallet = receiver_wallet
        self.amount = amount
        self.status = status

    def initiate_transaction(self):
        """Initiates a transaction from sender to receiver."""
        if self.sender_wallet.get_balance() >= self.amount:
            self.sender_wallet.transfer(self.receiver_wallet, self.amount)
            self.status = "completed"
            print(f"Transaction of {self.amount} completed from {self.sender_wallet.address} to {self.receiver_wallet.address}")
        else:
            print("Insufficient funds in sender's wallet!")

    def cancel_transaction(self):
        """Cancels the transaction and refunds the sender's wallet."""
        if self.status == "pending":
            print(f"Transaction of {self.amount} canceled.")
        else:
            print(f"Transaction is already {self.status}. Cannot cancel.")

    def get_status(self):
        """Returns the status of the transaction."""
        return self.status
