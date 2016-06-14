from accounting import PickupPayment
from accounting import MailPayment
from accounting import DirectDepositPayment


class PaymentMethod:
    def __init__(self, payment_method):
        self.__payment_method = payment_method

    def make_payment(self):
        if self.__payment_method == "Pickup":
            return PickupPayment
        elif self.__payment_method == "Direct Deposit":
            return DirectDepositStatement.make_deposit()
        elif self.__payment_method == "Mail Payment":

