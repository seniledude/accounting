from accounting import employee
class SalariedEmployee(employee):

    def __init__(self,salary, commission_rate, weekly_dues):
        Employee.__init__(self, employee_id, first_name, last_name)
        self.__salary = salary
        self.__commission_rate = commission_rate
        self.__weekly_dues = weekly_dues


    def set_salary(self, salary):
        self.__salary = salary

    def set_salary(self, commission_rate):
        self.__commission_rate = commission_rate

    def set_weekly_dues(self, weekly_dues):
        self.__weekly_dues = weekly_dues

    def get_weekly_dues(self):
        return self.__weekly_dues

    
