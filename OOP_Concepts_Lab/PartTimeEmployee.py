from EmployeeObj import Employee


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def display_info(self):
        super().display_info()
        print("Hourly Rate: €{0}".format(self.hourly_rate))
        print("Hours Worked: {0}".format(self.hours_worked))
