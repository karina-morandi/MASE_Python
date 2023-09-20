from EmployeeObj import Employee


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary

    def display_info(self):
        super().display_info()
        print("Salary: €{0:.2f}".format(self.salary))
