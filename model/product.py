# vấn đề: Mô hình hóa một sản phẩm trong một cửa hàng trực tuyến. 
# Một sản phẩm sẽ có các thuộc tính như id, name và price.
# Cần có một phương thức để hiển thị thông tin của sản phẩm.
# ý tưởng: Tạo một lớp Product để đại diện cho sản phẩm.    
# Lớp này sẽ có ba thuộc tính: id, name và price. 
# Ngoài ra, lớp này sẽ có một phương thức display() để hiển thị thông tin của sản phẩm.
# kết luận: Lớp Product sẽ giúp mô hình hóa một sản phẩm trong cửa hàng trực tuyến, 
# cho phép lưu trữ thông tin của sản phẩm và hiển thị thông tin đó một cách hiệu quả.   

class Product: 
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    
    def display(self):
        print(f"{self.name} - {self.price}")