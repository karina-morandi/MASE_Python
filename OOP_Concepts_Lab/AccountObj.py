class Account:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        print("The account was successfully created")
        self.account_info()

    def account_info(self):
        print("Name: {0}\t Balance: {1}".format(self.get_acc_name(), self.get_acc_balance()))

    def get_acc_name(self):
        return self.__name

    def get_acc_balance(self):
        return self.__balance

    def deposit(self, amt):
        self.__balance += amt
        print("You have successfully deposited:\t€{0}".format(amt))
        print("Your new balance is:\t€{0}".format(self.get_acc_balance()))

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def withdraw(self, amt):
        if self.__balance <= 0 or amt > self.__balance:
            print("Sorry, insufficient funds. Your balance is: €{0}".format(self.get_acc_balance()))
        else:
            self.__balance -= amt
            print("You have successfully withdrawn €{0}".format(amt))
            print("Your new balance is €{0}".format(self.get_acc_balance()))
