class Employee:

    def __init__(self, employee_id, first_name, last_name)
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name


    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_full_name(self):
        return self.__last_name + ', ' + self.__first_name

