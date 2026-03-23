# vấn đề: Mô hình hóa một dịch vụ đặt hàng trong một cửa hàng trực tuyến. 
# Dịch vụ này sẽ có một phương thức checkout() để xử lý quá trình thanh toán và hoàn tất đơn hàng.
# ý tưởng: Tạo một lớp OrderService để đại diện cho dịch vụ đặt hàng.   
# Lớp này sẽ có một phương thức checkout() để xử lý quá trình thanh toán và hoàn tất đơn hàng. 
# Trong phương thức checkout(), có thể tính tổng giá trị của đơn hàng bằng cách 
# gọi phương thức get_total() của đơn hàng, sau đó gọi phương thức pay() của phương thức thanh toán 
# để xử lý thanh toán, và cuối cùng gọi phương thức complete_order() của đơn hàng để hoàn tất đơn hàng.
# kết luận: Lớp OrderService sẽ giúp mô hình hóa một dịch vụ đặt hàng trong cửa hàng trực tuyến, 
# cho phép xử lý quá trình thanh toán và hoàn tất đơn hàng một cách hiệu quả, cung cấp thông tin 
# về tổng giá trị của đơn hàng và trạng thái của đơn hàng sau khi hoàn tất.

class OrderService: 
    def checkout(self, order, payment):
        total = order.get_total() 
        print(f"Order total: ${total}") 
        payment.pay(total) 
        order.complete_order() 
        print("Order completed")