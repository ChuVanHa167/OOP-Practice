# vấn đề: Mô hình hóa một phương thức thanh toán trong một hệ thống thanh toán. 
# Cần có một lớp Payment với một phương thức trừu tượng pay() để đại diện cho các phương thức 
# thanh toán khác nhau như thẻ tín dụng, PayPal, v.v.
# ý tưởng: Tạo một lớp Payment là một lớp trừu tượng với một phương thức trừu tượng pay(). 
# Các lớp cụ thể như CreditCardPayment sẽ kế thừa từ lớp Payment 
# và triển khai phương thức pay() để xử lý thanh toán theo cách riêng của chúng.
# kết luận: Lớp Payment sẽ giúp mô hình hóa một phương thức thanh toán trong hệ thống thanh toán, 
# cho phép mở rộng dễ dàng để hỗ trợ nhiều phương thức thanh toán khác nhau bằng cách tạo các lớp con kế thừa 
# và triển khai phương thức pay() theo cách riêng của chúng.    

from abc import ABC, abstractmethod 

class Payment(ABC): 
    @abstractmethod 
    
    def pay(self, amount): 
        pass