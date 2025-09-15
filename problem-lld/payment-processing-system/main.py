from abc import ABC, abstractmethod
class PaymentStrategy():
    @abstractmethod
    def process_payment(self, amount: float):
        pass


class CreaditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, holder_name: str):
        self.card_number = card_number
        self.holder_name = holder_name

    def process_payment(self, amount):
        print(f"Payment: Success, amount: {amount}, account holder: {self.holder_name}, card_number: ****{self.card_number[-4:]}")
        print(f"")
        return True
    
class PaypalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email_id = email

    def process_payment(self, amount):
        print(f"Payment:Success, amount: {amount} ---paypal----")
        return True
    
class BankTransferPayment(PaymentStrategy):
    def __init__(self, account_number: str, IFSC_number: str):
        self.account_number = account_number
        self.IFSC_number = IFSC_number

    def process_payment(self, amount):
        print(f"Bank transfer is successful.Amount: {amount}")
        return True
    
# PaymentProcessor class --> The Context class, which will eventually do the payment using particular strategy.

class PaymentProcessor():
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def execute_payment(self, amount: float):
        self.strategy.process_payment(amount)


if __name__ == "__main__":
    card_payment = CreaditCardPayment("8767567865431890", "John")
    payment = PaymentProcessor(card_payment)
    payment.execute_payment(100)