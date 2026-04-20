class PaymentVerification:
    def __init__(self, transaction):
        self.transaction = transaction

    def verify_payment(self):
        """Verifies the payment status of a transaction."""
        if self.transaction.status == "completed":
            print(f"Payment of {self.transaction.amount} successfully verified.")
            return True
        else:
            print(f"Payment verification failed for {self.transaction.amount}.")
            return False
