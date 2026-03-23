# vấn đề: Mô hình hóa một phương thức thanh toán bằng thẻ tín dụng trong một hệ thống thanh toán. 
# Cần có một lớp CreditCardPayment kế thừa từ lớp Payment và triển khai phương thức pay() để xử lý thanh toán bằng thẻ tín dụng.
# ý tưởng: Tạo một lớp CreditCardPayment kế thừa từ lớp Payment.    
# Lớp này sẽ triển khai phương thức pay() để xử lý thanh toán bằng thẻ tín dụng. 
# Trong phương thức pay(), có thể in ra một thông báo để mô phỏng quá trình xử lý thanh toán bằng thẻ tín dụng.
# kết luận: Lớp CreditCardPayment sẽ giúp mô hình hóa một phương thức thanh toán bằng thẻ tín dụng trong hệ thống thanh toán, 
# cho phép xử lý thanh toán bằng thẻ tín dụng một cách hiệu quả và cung cấp thông tin về quá trình thanh toán.

from payments.payment import Payment 

class CreditCardPayment(Payment): 
    def pay(self, amount): 
        print(f"Processing credit card payment: ${amount}")