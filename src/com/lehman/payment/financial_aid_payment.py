from payment import Payment

class FinancialAidPayment(Payment):
    def __init__(self, payer_name, amount, aid_type):
        super().__init__(payer_name, amount)
        self.aid_type = aid_type

    def process_payment(self):
        self._is_processed = True
        return f"Financial aid payment of ${self.amount:.2f} for {self.payer_name} from {self.aid_type} has been processed."