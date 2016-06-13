from accounting import employee
class HourlyEmployee(Employee):

    def __init__(self, employee_id, first_name,  last_name, hrly_rt, dues):
        Employee.__init__(self, employee_id, first_name,  last_name)

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def set_weekly_dues(self, weekly_dues):
        self.__weekly_dues = weekly_dues

    def get_hourly_rate(self):
        return self.__hourly_rate

    def get_weekly_dues(self):
        return self.__weekly_dues
