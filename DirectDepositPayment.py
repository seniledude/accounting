from accounting import BankAccount


class DirectDepositStatement:
    def __init__(self, amt):
        self.__amt = amt

    def make_deposit(self):
        return BankAccount.deposit()
