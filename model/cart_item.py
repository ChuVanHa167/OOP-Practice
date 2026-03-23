# vấn đề: Mô hình hóa một mục trong giỏ hàng của một cửa hàng trực tuyến. 
# Mỗi mục trong giỏ hàng sẽ bao gồm sản phẩm và số lượng của sản phẩm đó. 
# Ngoài ra, cần có một phương thức để tính tổng giá trị của mục trong giỏ hàng dựa trên giá của sản phẩm và số lượng.
# ý tưởng: Tạo một lớp CartItem để đại diện cho một mục trong giỏ hàng. 
# Lớp này sẽ có hai thuộc tính: product (đại diện cho sản phẩm) và quantity (số lượng của sản phẩm). 
# Ngoài ra, lớp này sẽ có một phương thức get_total() để tính tổng giá trị của mục trong giỏ hàng bằng cách nhân giá của sản phẩm với số lượng.
# kết luận: Lớp CartItem sẽ giúp mô hình hóa một mục trong giỏ hàng của cửa hàng trực tuyến, 
# cho phép tính toán tổng giá trị của mục dựa trên giá của sản phẩm và số lượng. 
# Điều này sẽ giúp quản lý giỏ hàng hiệu quả hơn và cung cấp thông tin chính xác về tổng giá trị của các mục trong giỏ hàng.

class CartItem: 
    def __init__(self, product, quantity): 
        self.product = product 
        self.quantity = quantity 
        
    def get_total(self): 
        return self.product.price * self.quantity