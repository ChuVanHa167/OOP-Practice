from model.product import Product 
from model.cart_item import CartItem 
from model.cart import Cart 
from model.order import Order 
from payment.credit_card_payment import CreditCardPayment 
from services.order_service import OrderService 

product1 = Product(1, "Laptop", 1000) 
product2 = Product(2, "Mouse", 50) 
cart = Cart() 
cart.add_item(CartItem(product1, 1)) 
cart.add_item(CartItem(product2, 2)) 
order = Order(cart) 
payment = CreditCardPayment() 
order_service = OrderService() 
order_service.checkout(order, payment)