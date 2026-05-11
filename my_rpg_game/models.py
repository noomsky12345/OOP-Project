import datetime

class CardSet:
    def __init__(self, set_id, name, stock, price, img_path):
        self.set_id = set_id
        self.name = name
        self.__stock = stock  # Private (Encapsulation)
        self.price = price
        self.img_path = img_path

    @property
    def stock(self):
        return self.__stock

    def reduce_stock(self, qty):
        if qty <= self.__stock:
            self.__stock -= qty
            return True
        return False

class Order:
    def __init__(self, customer_name, card_set_obj, quantity):
        self.customer_name = customer_name
        self.card_set = card_set_obj  # Composition
        self.quantity = quantity
        self.status = "Pending"  # Pending -> Paid -> Opened
        self.timestamp = datetime.datetime.now()

    def get_total(self):
        return self.quantity * self.card_set.price