class FoodDeliverySystem:
    
    order_id = 0
    orders_log = {}

    def __init__(self):
        self.menu = {
            "Burger": 150,
            "Pizza": 250,
            "Pasta": 200,
            "Salad": 120,
            "Beverages": 130,
            "Noodles": 150,
            "Sushi": 270,
            "Bakery":350
            # Add more items to the menu
        }
        self.bill_amount = 0
        
    def display_menu(self):
        """
        Return the menu details in the following format:
        {
            "Burger" :  150
            "Pizza"  :  250
            "Pasta"  :  200
            "Salad"  :  120
            "Beverages" :  130
            "Noodles" :  150
            "Sushi"  :  270
            "Bakery" :  350
        }
        """
        return self.menu
        
    def place_order(self, customer_name, order_items):
        """
        Return orders log after order placed by a customer with status as "Placed", otherwise return "order placement failed"
        Format:
        orders_log = {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity"}, status = "Placed}}
        """
        for item in order_items:
            if item not in self.menu:
                return "order placement failed"
        FoodDeliverySystem.order_id += 1
        FoodDeliverySystem.orders_log[FoodDeliverySystem.order_id] = {
            "customer_name": customer_name,
            "order_items": order_items,
            "status": "Placed"
        }
        return {FoodDeliverySystem.order_id: FoodDeliverySystem.orders_log[FoodDeliverySystem.order_id]}
        
    def pickup_order(self, order_id):
        """
        status: Picked Up	
        Return the changed status of the order: {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity"}, status = "Picked Up"}}
        """
        if order_id in FoodDeliverySystem.orders_log:
            FoodDeliverySystem.orders_log[order_id]['status'] = "Picked Up"
            return FoodDeliverySystem.orders_log[order_id]['status']
        return "Order not found"
        
    def deliver_order(self, order_id):
        """
        status: Delivered
        Return the delivery status of order (delivered or not delivered)
        """
        if order_id in FoodDeliverySystem.orders_log:
            if FoodDeliverySystem.orders_log[order_id]['status'] == "Picked Up":
                FoodDeliverySystem.orders_log[order_id]['status'] = "Delivered"
                return "Delivered"
            return "Order not picked up"
        return "Order not found"
        
    def modify_order(self, order_id, new_items):
        """
        Return the modified order with items available in menu only if the order is not picked up:
        {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity", new_items}, status = "Placed"}}
        """
        if order_id in FoodDeliverySystem.orders_log:
            if FoodDeliverySystem.orders_log[order_id]['status'] == "Placed":
                for item in new_items:
                    if item not in self.menu:
                        return "Invalid item in new_items"
                FoodDeliverySystem.orders_log[order_id]['order_items'].update(new_items)
                return FoodDeliverySystem.orders_log[order_id]
            return "Order already picked up or delivered"
        return "Order not found"
    
    def generate_bill(self, order_id):
        """
        if the sum of all items > 1000
        Amount = Sum of all items placed + 10% of total sum
        if sum of all items < 1000
        Amount = Sum of all items placed + 5% of total sum
        Return the total bill amount
        """
        if order_id in FoodDeliverySystem.orders_log:
            order_items = FoodDeliverySystem.orders_log[order_id]['order_items']
            total = sum(self.menu[item] * quantity for item, quantity in order_items.items())
            if total > 1000:
                total_bill_amount = total + (0.10 * total)
            else:
                total_bill_amount = total + (0.05 * total)
            return total_bill_amount
        return "Order not found"
        
    def cancel_order(self, order_id):
        """
        Cancel order items for the customer if the order is not Picked Up and remove order details from orders log
        Return the order logs. For example, if you have 3 orders, but the third order is cancelled, you need remove this from the orders log and just return the first two orders:
        {1: {"customer_name":"clientA", "order_items":{"Burger":1,"Pasta":2},"status":"Delivered"}, 2: {"customer_name":"clientB", "order_items":{"Salad":2,"Sushi":4, "Beverages":6, "Bakery":2},"status":"Placed"}}
        """
        if order_id in FoodDeliverySystem.orders_log:
            if FoodDeliverySystem.orders_log[order_id]['status'] == "Placed":
                del FoodDeliverySystem.orders_log[order_id]
        return FoodDeliverySystem.orders_log
