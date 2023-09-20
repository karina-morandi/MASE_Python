from AccountObj import Account


class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.__interest_rate = interest_rate

    def calculate_interest(self):
        interest_earned = (self.__interest_rate/100) * super().get_acc_balance()
        super().deposit(interest_earned)
        print("Interest earned €{0}".format(interest_earned))
        print("Your new balance is €{0}".format(self.get_acc_balance()))

