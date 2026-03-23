# vấn đề: Mô hình hóa một người dùng trong một hệ thống quản lý người dùng. 
# Một người dùng sẽ có các thuộc tính như user_id, name và email. 
# Cần có một phương thức để hiển thị thông tin của người dùng.
# ý tưởng: Tạo một lớp User để đại diện cho người dùng.
# Lớp này sẽ có ba thuộc tính: user_id, name và email. 
# Ngoài ra, lớp này sẽ có một phương thức display() để hiển thị thông tin của người dùng.
# kết luận: Lớp User sẽ giúp mô hình hóa một người dùng trong hệ thống quản lý người dùng, 
# cho phép lưu trữ thông tin của người dùng và hiển thị thông tin đó một cách hiệu quả.

class User: 
    def __init__(self, user_id, name, email): 
        self.__user_id = user_id 
        self.__name = name 
        self.__email = email 
        
    def get_name(self): 
        return self.__name 
    
    def display(self): 
        print(f"User: {self.__name} ({self.__email})")