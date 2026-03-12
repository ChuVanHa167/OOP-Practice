# OOP-Practice
thực hành OOP
## Mini Project: Hệ Thống Đặt Hàng E-Commerce

---

# 1. Giới thiệu

Repository này là **phần 1 trong chuỗi thực hành Software Design** gồm 4 phần:

1. OOP Practice
2. SOLID Practice
3. Design Pattern Practice
4. Architecture Integration (OOP + SOLID + DP)

Repository này **chỉ tập trung vào OOP**.

Mục tiêu là hiểu rõ **4 trụ cột của OOP** thông qua một bài thực hành thực tế.

---

# 2. Mục tiêu học tập

Sau khi hoàn thành repo này bạn sẽ:

* Hiểu cách **mô hình hóa hệ thống bằng object**
* Áp dụng **4 đặc trưng của OOP**
* Hiểu cách **các object tương tác với nhau**
* Xây dựng một hệ thống nhỏ theo **domain model**

---

# 3. 4 đặc trưng OOP sẽ được áp dụng

## Encapsulation (Đóng gói)

Dữ liệu của object phải được bảo vệ.

Ví dụ:

```python
self.__balance
```

Không cho phép truy cập trực tiếp từ bên ngoài.

---

## Abstraction (Trừu tượng)

Ẩn đi chi tiết phức tạp bên trong object.

Ví dụ:

```python
payment.pay()
```

Người sử dụng class **không cần biết bên trong thanh toán hoạt động thế nào**.

---

## Inheritance (Kế thừa)

Cho phép class con kế thừa logic từ class cha.

Ví dụ:

```
Payment
 ├── CreditCardPayment
 └── PaypalPayment
```

---

## Polymorphism (Đa hình)

Cùng một interface nhưng hành vi khác nhau.

Ví dụ:

```python
payment.pay()
```

CreditCardPayment và PaypalPayment sẽ xử lý khác nhau.

---

# 4. Bài toán thực hành

Xây dựng **hệ thống đặt hàng đơn giản cho một cửa hàng online**.

Hệ thống cho phép:

* Người dùng tạo tài khoản
* Thêm sản phẩm vào giỏ hàng
* Tạo đơn hàng
* Thanh toán bằng nhiều phương thức

---

# 5. Chức năng hệ thống

## User

Người dùng có thể:

* xem sản phẩm
* thêm sản phẩm vào giỏ hàng
* đặt hàng

---

## Cart

Giỏ hàng có thể:

* thêm sản phẩm
* xóa sản phẩm
* tính tổng tiền

---

## Order

Đơn hàng có thể:

* tạo từ giỏ hàng
* tính tổng tiền
* thanh toán

---

## Payment

Hệ thống hỗ trợ:

* Credit Card
* Paypal

---

# 6. Cấu trúc project

Tạo cấu trúc thư mục như sau:

```
repo1-oop-order-system

src/

models/
    user.py
    product.py
    cart.py
    cart_item.py
    order.py

payments/
    payment.py
    credit_card_payment.py
    paypal_payment.py

services/
    order_service.py

main.py
```

---

# 7. Domain Model của hệ thống

Các object chính:

```
User
Product
Cart
CartItem
Order
Payment
```

Quan hệ giữa chúng:

```
User
 └── Cart
        └── CartItem
               └── Product

Cart → Order

Order → Payment
```

---

# 8. Thực hành từng bước

## Bước 1 — Tạo class Product

Tạo file:

```
models/product.py
```

Code:

```python
class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name} - ${self.price}")
```

Giải thích:

Product đại diện cho **một sản phẩm trong hệ thống**.

Thuộc tính:

```
id
name
price
```

Method `display()` chỉ dùng để in thông tin sản phẩm.

---

## Bước 2 — Tạo class User

File:

```
models/user.py
```

Code:

```python
class User:

    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name
        self.__email = email

    def get_name(self):
        return self.__name

    def display(self):
        print(f"User: {self.__name} ({self.__email})")
```

Giải thích:

Ở đây áp dụng **Encapsulation**.

Các biến:

```
__user_id
__name
__email
```

được đặt là **private** để tránh bị sửa trực tiếp.

---

## Bước 3 — Tạo CartItem

File:

```
models/cart_item.py
```

Code:

```python
class CartItem:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total(self):
        return self.product.price * self.quantity
```

Giải thích:

CartItem đại diện cho:

```
1 sản phẩm + số lượng
```

---

## Bước 4 — Tạo Cart

File:

```
models/cart.py
```

Code:

```python
class Cart:

    def __init__(self):
        self.items = []

    def add_item(self, cart_item):
        self.items.append(cart_item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.get_total()
        return total
```

Giải thích:

Cart chứa nhiều CartItem.

Method:

```
add_item()
get_total()
```

cho phép thêm sản phẩm và tính tổng tiền.

---

## Bước 5 — Tạo Order

File:

```
models/order.py
```

Code:

```python
class Order:

    def __init__(self, cart):
        self.cart = cart
        self.status = "CREATED"

    def get_total(self):
        return self.cart.get_total()

    def complete_order(self):
        self.status = "COMPLETED"
```

Giải thích:

Order được tạo từ Cart.

Order có:

```
cart
status
```

---

## Bước 6 — Tạo Abstraction Payment

File:

```
payments/payment.py
```

Code:

```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Giải thích:

Đây là **Abstraction**.

Payment chỉ định nghĩa **interface** cho thanh toán.

---

## Bước 7 — Tạo Payment Methods

Credit Card:

```
payments/credit_card_payment.py
```

```python
from payments.payment import Payment

class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Processing credit card payment: ${amount}")
```

Paypal:

```
payments/paypal_payment.py
```

```python
from payments.payment import Payment

class PaypalPayment(Payment):

    def pay(self, amount):
        print(f"Processing PayPal payment: ${amount}")
```

Giải thích:

Đây là:

* Inheritance
* Polymorphism

Hai class kế thừa từ Payment nhưng xử lý khác nhau.

---

## Bước 8 — Tạo OrderService

File:

```
services/order_service.py
```

```python
class OrderService:

    def checkout(self, order, payment):

        total = order.get_total()

        print(f"Order total: ${total}")

        payment.pay(total)

        order.complete_order()

        print("Order completed")
```

Giải thích:

Service này điều phối:

```
Order
Payment
```

---

## Bước 9 — Demo chương trình

File:

```
main.py
```

Code:

```python
from models.product import Product
from models.cart_item import CartItem
from models.cart import Cart
from models.order import Order

from payments.credit_card_payment import CreditCardPayment

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
```

---

# 9. Output mong muốn

```
Order total: $1100
Processing credit card payment: $1100
Order completed
```

---

# 10. OOP được áp dụng trong project

Encapsulation

```
User private fields
```

Abstraction

```
Payment abstract class
```

Inheritance

```
CreditCardPayment → Payment
PaypalPayment → Payment
```

Polymorphism

```
payment.pay()
```

---

# 11. Những lỗi phổ biến

Không nên:

* viết tất cả logic vào 1 class
* truy cập trực tiếp biến private
* để class có quá nhiều trách nhiệm

---

# 12. Sau khi hoàn thành repo này

Bạn sẽ tiếp tục:

```
repo2-solid-order-system
```

Refactor hệ thống theo **SOLID principles**.
