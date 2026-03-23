# vấn đề: Mô hình hóa một đơn hàng trong một cửa hàng trực tuyến. 
# Một đơn hàng sẽ bao gồm một giỏ hàng và trạng thái của đơn hàng (ví dụ: "CREATED", "COMPLETED"). 
# Cần có một phương thức để tính tổng giá trị của đơn hàng dựa trên giỏ hàng 
# và một phương thức để hoàn thành đơn hàng bằng cách thay đổi trạng thái của nó.
# ý tưởng: Tạo một lớp Order để đại diện cho đơn hàng. 
# Lớp này sẽ có hai thuộc tính: cart (đại diện cho giỏ hàng) và status (trạng thái của đơn hàng). 
# Lớp Order sẽ có một phương thức get_total() để tính tổng giá trị của đơn hàng 
# bằng cách gọi phương thức get_total() của giỏ hàng 
# và một phương thức complete_order() để hoàn thành đơn hàng bằng cách thay đổi trạng thái của nó thành "COMPLETED".
# kết luận: Lớp Order sẽ giúp mô hình hóa một đơn hàng trong cửa hàng trực tuyến, 
# cho phép tính toán tổng giá trị của đơn hàng dựa trên giỏ hàng và quản lý trạng thái của đơn hàng một cách hiệu quả.  

class Order: 
    def __init__(self, cart): 
        self.cart = cart 
        self.status = "CREATED" 
        
    def get_total(self): 
        return self.cart.get_total() 
    
    def complete_order(self): 
        self.status = "COMPLETED"