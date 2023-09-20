from CarObj import Car


def main():
    print("Example to demonstrate encapsulation")
    # Creating an instance of the Car class
    my_car = Car("Toyota", "Corolla")

    # Accessing and modifying make using public methods
    print(my_car.get_make())  # Output: "Toyota"
    my_car.set_make("Honda")
    print(my_car.get_make())  # Output: "Honda"

    # Accessing and modifying model using public methods
    my_car.update_model("Civic")
    my_car.display_details()  # Output "Car Details: Honda, Civic"

    # Trying to access private attributes directly (not recommended)
    print(my_car._make)  # Output: "Honda"
    print(my_car.__model)


if __name__ == "__main__":
    main()
