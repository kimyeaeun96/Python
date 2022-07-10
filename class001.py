class Supermarket:
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer
 
    def printLocation(self):
        print(self.location)
 
    def changeCategory(self, new_product):
        self.product = new_product
 
    def showList(self):
        print(self.product)
 
    def enterCustomer(self):
        self.customer = self.customer + 1
 
    def showInfo(self):
        print(self.name, self.location, self.product, self.customer)
