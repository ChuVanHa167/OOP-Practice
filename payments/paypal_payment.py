# vấn đề: Mô hình hóa một phương thức thanh toán bằng PayPal trong một hệ thống thanh toán. 
# Cần có một lớp PaypalPayment kế thừa từ lớp Payment và triển khai phương thức pay() để xử lý thanh toán bằng PayPal.
# ý tưởng: Tạo một lớp PaypalPayment kế thừa từ lớp Payment.    
# Lớp này sẽ triển khai phương thức pay() để xử lý thanh toán bằng PayPal. 
# Trong phương thức pay(), có thể in ra một thông báo để mô phỏng quá trình xử lý thanh toán bằng PayPal.
# kết luận: Lớp PaypalPayment sẽ giúp mô hình hóa một phương thức thanh toán bằng PayPal trong hệ thống thanh toán, 
# cho phép xử lý thanh toán bằng PayPal một cách hiệu quả và cung cấp thông tin về quá trình thanh toán.

from payments.payment import Payment 
class PaypalPayment(Payment): 
    def pay(self, amount): 
        print(f"Processing PayPal payment: ${amount}")