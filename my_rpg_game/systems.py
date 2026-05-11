from models import Order

class Inventory:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def get_all(self):
        return self.__items

    def find_item(self, set_id):
        return next((i for i in self.__items if i.set_id == set_id), None)

class LiveManager:
    def __init__(self):
        self.inventory = Inventory()
        self.__orders = []

    def create_order(self, customer, set_id, qty):
        item = self.inventory.find_item(set_id)
        if item and item.stock >= qty:
            if item.reduce_stock(qty):
                new_order = Order(customer, item, qty)
                self.__orders.append(new_order)
                return new_order, "Success"
        return None, "สินค้าไม่พอ!"

    def get_queue(self):
        # จ่ายแล้วขึ้นก่อน ตามด้วยรอจ่าย (Opened ไม่แสดง)
        paid = [o for o in self.__orders if o.status == "Paid"]
        pending = [o for o in self.__orders if o.status == "Pending"]
        return paid + pending

    def get_total_sales(self):
        return sum(o.get_total() for o in self.__orders if o.status != "Pending")

    def confirm_payment(self, customer_name):
        for o in reversed(self.__orders):
            if o.customer_name == customer_name and o.status == "Pending":
                o.status = "Paid"
                return True
        return False

    def finish_order(self):
        paid_orders = [o for o in self.__orders if o.status == "Paid"]
        if paid_orders:
            paid_orders[0].status = "Opened"
            return True
        return False