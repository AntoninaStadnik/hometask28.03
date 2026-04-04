# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька рахунків, добавте їх у список та для
# кожної викличте відповідні методи.

class CreditCardPayment:
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def pay(self):
        print(f"Payment via Card {self.amount}{self.currency}")


class PayPalPayment:
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def pay(self):
        print(f"Payment via PayPal {self.amount}{self.currency}")


class CryptoPayment:
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def pay(self):
        print(f"Payment via Crypto {self.amount}{self.currency}")


def create_payment() -> CreditCardPayment | PayPalPayment | CryptoPayment | None:
    payment = input("Select payment type: card, paypal, crypto): ")
    amount = int(input("Enter amount: "))
    currency = input("Enter currency: ")

    if payment == "card":
        return CreditCardPayment(amount, currency)

    elif payment == "paypal":
        return PayPalPayment(amount, currency)

    elif payment == "crypto":
        return CryptoPayment(amount, currency)

    else:
        print("No such payment type")
        return None


bills = []

for _ in range(3):
    bill = create_payment()
    if bill is not None:
        bills.append(bill)


for bill in bills:
    bill.pay()