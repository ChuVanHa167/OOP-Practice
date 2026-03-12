class OrderService: 
    def checkout(self, order, payment):
        total = order.get_total() 
        print(f"Order total: ${total}") 
        payment.pay(total) 
        order.complete_order() 
        print("Order completed")