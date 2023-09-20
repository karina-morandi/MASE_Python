from Product_Obj import Product

def main():
    # create two product objects
    product1 = Product("Stanley 13 Ounce Wood Hammer", 12.99, 62)
    product2 = Product("National Hardware 3/4 Wire Nails", 5.06, 50)

    #print data for product 1 to console
    #Could print the info in this way
    print("PRODUCT DATA")
    print("Name:\t\t\t\t\t{:s}".format(product1.name))
    print("Price:\t\t\t\t\t€{:.2f}".format(product1.price))
    print("Discount percent:\t\t{:d}%".format(product1.discountPercent))
    print("Discount amount:\t\t€{:.2f}".format(product1.get_discount_amount()))
    print("Discount price:\t\t\t€{:.2f}".format(product1.get_discount_price()))

    #Or using the function in Product_Obj.py
    product2.get_product_details()

if __name__ == "__main__":
    main()