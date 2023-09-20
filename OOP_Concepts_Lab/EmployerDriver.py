from FullTimeEmployee import FullTimeEmployee
from PartTimeEmployee import PartTimeEmployee


def main():
    # Creating instances of the derived classes
    employee1 = FullTimeEmployee("John Smith", 1001, 60000)
    employee2 = PartTimeEmployee("Jane Doe", 2002, 15.50, 20)

    # Using overriden methods
    print("Full-Time Employee:")
    employee1.display_info()
    print("\nPart-Time Employee:")
    employee2.display_info()

    # Using subclass-specific methods
    print("\nPart-Time Employee Pay:")
    print("{0} earned €{1:.2f}".format(employee2.get_employee_name(), employee2.calculate_pay()))


if __name__ == "__main__":
    main()
