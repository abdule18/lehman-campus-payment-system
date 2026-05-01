from payment import Payment

class CreditCardPayment(Payment):
    def __init__(self, payer_name, amount, card_last_four):
        super().__init__(payer_name, amount)
        self.card_last_four = card_last_four

    def process_payment(self):
        self._is_processed = True
        return f"Credit card payment of ${self.amount:.2f} for {self.payer_name} using card ending in {self.card_last_four} has been processed."