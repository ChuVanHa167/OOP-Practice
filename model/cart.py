# vấn đề: Mô hình hóa một giỏ hàng trong một cửa hàng trực tuyến. 
# Giỏ hàng sẽ chứa nhiều mục, mỗi mục đại diện cho một sản phẩm và số lượng của sản phẩm đó. 
# Cần có một phương thức để tính tổng giá trị của giỏ hàng dựa trên giá của từng sản phẩm và số lượng của chúng.
# ý tưởng: Tạo một lớp Cart để đại diện cho giỏ hàng. 
# Lớp này sẽ có một thuộc tính items, là một danh sách chứa các mục trong giỏ hàng. 
# Lớp Cart sẽ có một phương thức add_item() để thêm một mục vào giỏ hàng và một phương thức get_total() để tính tổng giá trị của giỏ hàng 
# bằng cách gọi phương thức get_total() của từng mục trong giỏ hàng và cộng chúng lại.
# kết luận: Lớp Cart sẽ giúp mô hình hóa một giỏ hàng trong cửa hàng trực tuyến, 
# cho phép quản lý các mục trong giỏ hàng và tính toán tổng giá trị của giỏ hàng một cách hiệu quả.

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