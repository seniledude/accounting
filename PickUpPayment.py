from accounting import TimeCard
from accounting import Employee


class PickupPayment:
    def __init__(self):
        amt = TimeCard.calculate_daily_pay()
        print("A check for " + amt + "is waiting for " + Employee.get_full_name() + "at the PostMaster.")