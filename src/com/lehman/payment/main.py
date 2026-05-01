from credit_card_payment import CreditCardPayment
from meal_plan_payment import MealPlanPayment
from financial_aid_payment import FinancialAidPayment
from payment import Payment


def exercise_3_polymorphism():
    print("\n--- Exercise 3: Polymorphism ---")

    payments = [
        CreditCardPayment("Alice", 250.00, "1234"),
        MealPlanPayment("Bob", 75.50, "MP-2026"),
        FinancialAidPayment("Jane Smith", 1200.00, "Pell Grant")
    ]

    for payment in payments:
        print(payment.process_payment())
        print(payment.get_status())


if __name__ == "__main__":
    print("--- Exercise 1 & 2: Classes and Inheritance ---")

    payment1 = Payment("John Doe", 100.00)
    payment2 = CreditCardPayment("Jane Smith", 300.00, "5678")

    print(payment1.get_status())
    print(payment1.process_payment())
    print(payment1.get_status())

    print(payment2.process_payment())
    print(payment2.get_status())

    exercise_3_polymorphism()