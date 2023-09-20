class Product:

    # a constructor that initializes 3 attributes
    def __init__(self, name, price,discount_percent):
        self.name = name
        self.price = price
        self.discountPercent = discount_percent

    # a method that uses two attributes
    def get_discount_amount(self):
        return self.price * self.discountPercent / 100

    # a method that calls another method
    def get_discount_price(self):
        return self.price - self.get_discount_amount()

    def get_product_details(self):
        details = """\nName:\t{0}\nPrice:\t€{1}\nDiscounted:{2}%\nDiscount:\t€{3:.2f}\nNewPrice:\t€{4:.2f}""".format(self.name, self.price, self.discountPercent, self.get_discount_amount(), self.get_discount_price())
        print(details)