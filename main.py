from model.product import Product 
from model.cart_item import CartItem 
from model.cart import Cart 
from model.order import Order 
from payments.credit_card_payment import CreditCardPayment 
from services.order_service import OrderService 

product1 = Product(1, "Laptop", 1000) # tạo một sản phẩm với id 1, tên "Laptop" và giá 1000
product2 = Product(2, "Mouse", 50) 
cart = Cart() # tạo một giỏ hàng mới
cart.add_item(CartItem(product1, 1)) # thêm một mục vào giỏ hàng với sản phẩm là product1 và số lượng là 1 
cart.add_item(CartItem(product2, 2)) 
order = Order(cart) # tạo một đơn hàng mới với giỏ hàng đã tạo ở trên
payment = CreditCardPayment() # tạo một phương thức thanh toán bằng thẻ tín dụng mới
order_service = OrderService() # tạo một dịch vụ đặt hàng mới
order_service.checkout(order, payment) # gọi phương thức checkout() của dịch vụ đặt hàng để xử lý thanh toán và hoàn tất đơn hàng 