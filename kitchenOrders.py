class KitchenOrders:
    def __init__(self):
        self.orders = []

    def enqueue(self, item):
        self.orders.append(item)
        print(self.orders)
    
    def dequeue(self):
        self.orders.pop(0)
        print("Order Complete. Remaining Orders...", self.orders)

    def is_empty(self):
        return len(self.queue) == 0

queue = KitchenOrders()
queue.enqueue("Chicken Tenders")
queue.enqueue("Burger")
queue.enqueue("French Fries")
queue.dequeue()
