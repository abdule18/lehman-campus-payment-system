from payment import Payment

class MealPlanPayment(Payment):
    def __init__(self, payer_name, amount, meal_plan_id):
        super().__init__(payer_name, amount)
        self.meal_plan_id = meal_plan_id

    def process_payment(self):
        self._is_processed = True
        return f"Meal plan payment of ${self.amount:.2f} for {self.payer_name} using plan ID {self.meal_plan_id} has been processed."