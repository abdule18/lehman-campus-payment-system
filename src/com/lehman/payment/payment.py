class Payment:
    def __init__(self, payer_name, amount):
        self.payer_name = payer_name
        self.amount = amount
        self._is_processed = False

    def process_payment(self):
        self._is_processed = True
        return f"{self.payer_name}'s payment of ${self.amount:.2f} has been processed."

    def get_status(self):
        status = "Processed" if self._is_processed else "Pending"
        return f"Payment for {self.payer_name} is currently {status}."