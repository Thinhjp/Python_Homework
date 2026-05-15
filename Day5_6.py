# # Bài tập 1: Xây dựng class Product
# # Xây dựng một class Product với các yêu cầu sau:
# # • Thuộc tính: product_id, name, price, quantity (tồn kho), category
# # • Hàm __init__() khởi tạo các thuộc tính trên
# # • Phương thức apply_discount(discount_percent): giảm giá sản phẩm (trả về giá sau giảm)
# # • Phương thức is_in_stock(): kiểm tra xem sản phẩm còn trong kho hay không
# # Yêu cầu: Viết code và chạy với 2-3 sản phẩm khác nhau.

# from decimal import Decimal 
# # Sử dụng Decimal để xử lý giá tiền chính xác hơn, tránh lỗi làm tròn khi dùng float

# class Product:
#     def __init__(self, product_id: int, name: str, price: float, quantity: int, category: str):
#         # Kiểm tra dữ liệu đầu vào hợp lệ
#         if price < 0 or quantity < 0: # Giá và số lượng không thể là số âm
#             raise ValueError("Giá và Số lượng tồn kho không được là số âm.") 
#         # raise là Control Flow Interruption (Ngắt luồng) báo lỗi ngay khi dữ liệu âm
        
            
#         self.product_id = product_id
#         self.name = name
#         self.price = Decimal(str(price)) # Ép chuỗi rồi đưa cho Decimal tính
#         self.quantity = quantity
#         self.category = category

#     def apply_discount(self, discount_percent: float) -> float:
#         # Kiểm tra phần trăm giảm giá hợp lệ
#         if not (0 <= discount_percent <= 100):
#             raise ValueError("Phần trăm giảm giá phải nằm trong khoảng 0-100.")
            
#         # Tính giá sau khi áp dụng giảm giá
#         discount_amount = self.price * (Decimal(str(discount_percent)) / Decimal('100'))
#         # ép float discount_percent thành String rồi tính bằng Decimal
#         # '100' định nghĩa chuỗi thay cho str, không cần cũng được vì là số nguyên.
#         discounted_price = self.price - discount_amount

#         return discounted_price 

#     def is_in_stock(self) -> bool:
#         """
#         Kiểm tra sản phẩm còn trong kho không.
#         """ 
#         # """ """ Docstring giải thích chức năng của hàm.
#         return self.quantity > 0

#     def __str__(self):
#         """ Phiên dịch viên String để hiển thị thông tin sản phẩm một cách dễ đọc. """
#         stock_status = "Còn hàng" if self.is_in_stock() else "Hết hàng"
#         return f"[{self.product_id}] {self.name} - Giá: {self.price:,.0f}đ - Tình trạng: {stock_status}"
#         # f"" format chuỗi. :,.0f có dấu phẩy ngăn cách hàng nghìn và không thập phân.No float.

# # Test case.

# if __name__ == "__main__":
#     # 1. Khởi tạo sản phẩm
#     p1 = Product(product_id=101, name="Bàn phím cơ Keychron", price=1500000, quantity=10, category="Electronics")
#     p2 = Product(product_id=102, name="Chuột Logitech G102", price=450000, quantity=0, category="Electronics")
#     p3 = Product(product_id=103, name="Balo Laptop", price=600000, quantity=5, category="Fashion")

#     products = [p1, p2, p3]

#     print("--- LIST THUỘC TÍNH ---")
#     for p in products:
#         print(p)

#     print("\n--- TEST FUNCTION ---")
    
#     # Kiểm tra tồn kho và áp dụng giảm giá
#     for p in products:
#         if p.is_in_stock():
#             # Chạy campaign: Giảm 20% cho tất cả hàng còn trong kho
#             new_price = p.apply_discount(20)
#             print(f"Khuyến mãi! {p.name} giảm 20% chỉ còn: {new_price:,.0f}đ")
#         else:
#             print(f"Rất tiếc! {p.name} đã hết hàng, không thể áp dụng khuyến mãi.")

# Bài tập 2: Xây dựng class Customer với Encapsulation
# Xây dựng class Customer (khách hàng) với:
# • Thuộc tính public: customer_id, name
# • Thuộc tính protected: _email
# • Thuộc tính private: __password, __credit_balance (số dư tài khoản)
# • Hàm getter và setter cho __credit_balance (setter chỉ cho phép giá trị >= 0)
# • Phương thức add_credit(amount): nạp tiền vào tài khoản
# • Phương thức use_credit(amount): sử dụng tiền từ tài khoản (kiểm tra đủ số dư)
# Yêu cầu: Kiểm tra access control - đảm bảo không thể truy cập trực tiếp __password từ bên ngoài.

from decimal import Decimal 

class Customer:
    """
    Lớp đại diện cho đối tượng Khách hàng trong hệ thống.
    Quản lý thông tin định danh và số dư tài khoản an toàn thông qua Encapsulation và Strict Typing.
    """
    
    def __init__(self, customer_id: str, name: str, email: str, password: str):
        # 1. Public attributes
        self.customer_id = customer_id
        self.name = name
        
        # 2. Protected attribute (Quy ước nội bộ/kế thừa)
        self._email = email
        
        # 3. Private attributes (Bảo vệ nghiêm ngặt)
        self.__password = password  
        self.__credit_balance = Decimal('0')   # Luôn khởi tạo số dư mặc định là 0 bằng chuỗi '0'

    # --- ENCAPSULATION CHO CREDIT BALANCE ---

    @property 
    def credit_balance(self) -> Decimal:
        """Getter: Trả về số dư tài khoản hiện tại."""
        return self.__credit_balance

    @credit_balance.setter
    def credit_balance(self, value: Decimal):
        """Setter: Cập nhật số dư tài khoản. Chặn gán sai kiểu và gán số âm."""
        # Type Guard: Bảo vệ kiểu dữ liệu
        if not isinstance(value, Decimal):
            raise TypeError(f"Lỗi: Số dư phải là kiểu Decimal. Bạn đang truyền {type(value).__name__}.")
            
        # Value Guard: Bảo vệ logic nghiệp vụ
        if value < Decimal('0'):
            raise ValueError("Lỗi: Số dư tài khoản không được nhỏ hơn 0.")
            
        self.__credit_balance = value

    # --- BEHAVIORS (HÀNH VI NGHIỆP VỤ) ---

    def add_credit(self, amount: Decimal):
        """Nạp tiền vào tài khoản."""
        # Thêm Type Guard để hàm không bị crash khi user truyền int/float
        if not isinstance(amount, Decimal):
            raise TypeError("Lỗi: Số tiền nạp phải là định dạng Decimal.")
            
        if amount <= Decimal('0'):
            raise ValueError("Lỗi: Số tiền nạp phải lớn hơn 0.")
        
        self.credit_balance += amount # Tự động gọi gián tiếp qua setter
        print(f"[Thành công] {self.name} nạp {amount}. Số dư mới: {self.credit_balance}")

    def use_credit(self, amount: Decimal):
        """Sử dụng tiền từ tài khoản."""
        # Thêm Type Guard
        if not isinstance(amount, Decimal):
            raise TypeError("Lỗi: Số tiền sử dụng phải là định dạng Decimal.")
            
        if amount <= Decimal('0'):
            raise ValueError("Lỗi: Số tiền sử dụng phải lớn hơn 0.")
            
        if amount > self.credit_balance:
            raise ValueError(f"Lỗi: Giao dịch thất bại. {self.name} không đủ số dư (Hiện có: {self.credit_balance}).")
            
        self.credit_balance -= amount
        print(f"[Thành công] {self.name} tiêu {amount}. Số dư mới: {self.credit_balance}")


# ==========================================
# PHẦN TEST SỬA LỖI ĐỂ TRÁNH CRASH 
# ==========================================
if __name__ == "__main__":
    print("--- 1. KHỞI TẠO KHÁCH HÀNG ---")
    cus1 = Customer(customer_id="C001", name="Nguyen Van A", email="a@gmail.com", password="super_secret_pw")
    print(f"Khách hàng: {cus1.name}, ID: {cus1.customer_id}")
    print(f"Email (Protected): {cus1._email}")
    
    print("\n--- 2. TEST LOGIC TÀI KHOẢN (HAPPY PATH) ---")
    # LƯU Ý: Phải truyền Decimal thay vì int như code cũ
    cus1.add_credit(Decimal('500.00'))   
    cus1.use_credit(Decimal('200.00'))   
    
    print("\n--- 3. TEST LOGIC TÀI KHOẢN (EDGE CASES) ---")
    try:
        cus1.use_credit(Decimal('1000.00'))  # Cố tình tiêu quá số dư
    except ValueError as e:
        print(f"-> [THÀNH CÔNG] Chặn tiêu lố: {e}")
        
    try:
        cus1.add_credit(Decimal('-50.00'))   # Cố tình nạp số âm
    except ValueError as e:
        print(f"-> [THÀNH CÔNG] Chặn nạp số âm: {e}")
        
    print("\n--- 4. TEST ACCESS CONTROL (ENCAPSULATION) ---")
    
    # Test 4.1: Cố tình gán sai kiểu dữ liệu (Truyền int thay vì Decimal)
    try:
        cus1.credit_balance = -100  
    except TypeError as e:
        print(f"-> [THÀNH CÔNG] Chặn gán sai kiểu (TypeError): {e}")
        
    # Test 4.2: Cố tình gán số dư âm thông qua setter (Truyền đúng kiểu Decimal nhưng sai logic)
    try:
        cus1.credit_balance = Decimal('-100.00')
    except ValueError as e:
        print(f"-> [THÀNH CÔNG] Chặn gán số âm (ValueError): {e}")
        
    # Test 4.3: Truy cập biến Private __password
    print("\nThử truy cập __password từ bên ngoài:")
    try:
        print(cus1.__password)
    except AttributeError:
        print("-> [BẢO MẬT] AttributeError: Class 'Customer' object has no attribute '__password'")
        print("-> Biến __password đã được ẩn giấu thành công (Name Mangling)!")