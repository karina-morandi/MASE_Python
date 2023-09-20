class Car:
    def __init__(self, make, model):
        self._make = make
        self.__model = model

    # Public method to access make
    def get_make(self):
        return self._make

    # Public method to set make
    def set_make(self, make):
        self._make = make

    # Private method to access model
    def __get_model(self):
        return self.__model

    # Private method to set model
    def __set_model(self, model):
        self.__model = model

    # Public method to call the private set_model method
    def update_model(self, model):
        self.__set_model(model)

    # Public method to display car details
    def display_details(self):
        print("Car Details: {0}, {1}".format(self._make, self.__model))