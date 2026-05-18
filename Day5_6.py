# Bài tập 1: Xây dựng class Product
# Xây dựng một class Product với các yêu cầu sau:
# • Thuộc tính: product_id, name, price, quantity (tồn kho), category
# • Hàm __init__() khởi tạo các thuộc tính trên
# • Phương thức apply_discount(discount_percent): giảm giá sản phẩm (trả về giá sau giảm)
# • Phương thức is_in_stock(): kiểm tra xem sản phẩm còn trong kho hay không
# Yêu cầu: Viết code và chạy với 2-3 sản phẩm khác nhau.

from decimal import Decimal 
# Sử dụng Decimal để xử lý giá tiền chính xác hơn, tránh lỗi làm tròn khi dùng float

class Product:
    def __init__(self, product_id: int, name: str, price: float, quantity: int, category: str):
        # Kiểm tra dữ liệu đầu vào hợp lệ
        if price < 0 or quantity < 0: # Giá và số lượng không thể là số âm
            raise ValueError("Giá và Số lượng tồn kho không được là số âm.") 
        # raise là Control Flow Interruption (Ngắt luồng) báo lỗi ngay khi dữ liệu âm
        
            
        self.product_id = product_id
        self.name = name
        self.price = Decimal(str(price)) # Ép chuỗi rồi đưa cho Decimal tính
        self.quantity = quantity
        self.category = category

    def apply_discount(self, discount_percent: float) -> float:
        # Kiểm tra phần trăm giảm giá hợp lệ
        if not (0 <= discount_percent <= 100):
            raise ValueError("Phần trăm giảm giá phải nằm trong khoảng 0-100.")
            
        # Tính giá sau khi áp dụng giảm giá
        discount_amount = self.price * (Decimal(str(discount_percent)) / Decimal('100'))
        # ép float discount_percent thành String rồi tính bằng Decimal
        # '100' định nghĩa chuỗi thay cho str, không cần cũng được vì là số nguyên.
        discounted_price = self.price - discount_amount

        return discounted_price 

    def is_in_stock(self) -> bool:
        """
        Kiểm tra sản phẩm còn trong kho không.
        """ 
        # """ """ Docstring giải thích chức năng của hàm.
        return self.quantity > 0

    def __str__(self):
        """ Phiên dịch viên String để hiển thị thông tin sản phẩm một cách dễ đọc. """
        stock_status = "Còn hàng" if self.is_in_stock() else "Hết hàng"
        return f"[{self.product_id}] {self.name} - Giá: {self.price:,.0f}đ - Tình trạng: {stock_status}"
        # f"" format chuỗi. :,.0f có dấu phẩy ngăn cách hàng nghìn và không thập phân.No float.

# Test case.

if __name__ == "__main__":
    # 1. Khởi tạo sản phẩm
    p1 = Product(product_id=101, name="Bàn phím cơ Keychron", price=1500000, quantity=10, category="Electronics")
    p2 = Product(product_id=102, name="Chuột Logitech G102", price=450000, quantity=0, category="Electronics")
    p3 = Product(product_id=103, name="Balo Laptop", price=600000, quantity=5, category="Fashion")

    products = [p1, p2, p3]

    print("--- LIST THUỘC TÍNH ---")
    for p in products:
        print(p)

    print("\n--- TEST FUNCTION ---")
    
    # Kiểm tra tồn kho và áp dụng giảm giá
    for p in products:
        if p.is_in_stock():
            # Chạy campaign: Giảm 20% cho tất cả hàng còn trong kho
            new_price = p.apply_discount(20)
            print(f"Khuyến mãi! {p.name} giảm 20% chỉ còn: {new_price:,.0f}đ")
        else:
            print(f"Rất tiếc! {p.name} đã hết hàng, không thể áp dụng khuyến mãi.")

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
        self.__credit_balance = Decimal('0')   # khởi tạo số dư mặc định là 0 bằng chuỗi '0'

    # ĐÓNG GÓI CHO CREDIT BALANCE 

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

    # Method add và use

    def add_credit(self, amount: Decimal):
        """Nạp tiền vào tài khoản."""
        # Check type để hàm không bị crash khi user truyền int/float
        if not isinstance(amount, Decimal):
            raise TypeError("Lỗi: Số tiền nạp phải là định dạng Decimal.")
            
        if amount <= Decimal('0'):
            raise ValueError("Lỗi: Số tiền nạp phải lớn hơn 0.")
        
        self.credit_balance += amount # Tự động gọi gián tiếp qua setter
        print(f"[Thành công] {self.name} nạp {amount}. Số dư mới: {self.credit_balance}")

    def use_credit(self, amount: Decimal):
        """Sử dụng tiền từ tài khoản."""
        # check type
        if not isinstance(amount, Decimal):
            raise TypeError("Lỗi: Số tiền sử dụng phải là định dạng Decimal.")
            
        if amount <= Decimal('0'):
            raise ValueError("Lỗi: Số tiền sử dụng phải lớn hơn 0.")
            
        if amount > self.credit_balance:
            raise ValueError(f"Lỗi: Giao dịch thất bại. {self.name} không đủ số dư (Hiện có: {self.credit_balance}).")
            
        self.credit_balance -= amount
        print(f"[Thành công] {self.name} tiêu {amount}. Số dư mới: {self.credit_balance}")


# Test code

if __name__ == "__main__":
    print("--- 1. KHỞI TẠO KHÁCH HÀNG ---")
    cus1 = Customer(customer_id="C001", name="Nguyen Van A", email="a@gmail.com", password="secret123")
    print(f"Khách hàng: {cus1.name}, ID: {cus1.customer_id}")
    print(f"Email (Protected): {cus1._email}")
    
    print("\n--- 2. TEST LOGIC TÀI KHOẢN (HAPPY PATH) ---")
    
    cus1.add_credit(Decimal('500.00'))   
    cus1.use_credit(Decimal('200.00'))   
    
    print("\n--- 3. TEST LOGIC TÀI KHOẢN (EDGE CASES) ---")
    try:
        cus1.use_credit(Decimal('1000.00'))  # Cố tình tiêu quá số dư
    except ValueError as e:
        print(e)
        
    try:
        cus1.add_credit(Decimal('-50.00'))   # Cố tình nạp số âm
    except ValueError as e:
        print(e)
        
    print("\n--- 4. TEST ACCESS CONTROL (ENCAPSULATION) ---")
    
    # Test 4.1: Cố tình gán sai kiểu dữ liệu (Truyền int thay vì Decimal)
    try:
        cus1.credit_balance = -100  
    except TypeError as e:
        print(e)
        
    # Test 4.2: Cố tình gán số dư âm thông qua setter (Truyền đúng kiểu Decimal nhưng sai logic)
    try:
        cus1.credit_balance = Decimal('-100.00')
    except ValueError as e:
        print(e)
        
    # Test 4.3: Truy cập biến Private __password
    print("\nThử truy cập __password từ bên ngoài:")
    print(cus1._Customer__password) # bypass qua AttributeError
    try:
        print(cus1.__password)
    except AttributeError:
        print("-> Biến __password đã được ẩn giấu thành công (Name Mangling)!")

# Bài tập 3: Xây dựng class Order và tính tổng tiền
# Xây dựng class Order (đơn hàng) với:
# • Thuộc tính: order_id, customer (đối tượng Customer), order_date, items (danh sách các sản phẩm đã mua), quantities (danh sách số lượng)
# • Phương thức add_item(product, quantity): thêm sản phẩm vào đơn hàng
# • Phương thức calculate_total(): tính tổng tiền đơn hàng
# • Phương thức apply_discount(discount_percent): áp dụng mã giảm giá cho toàn bộ đơn
# Yêu cầu: Tạo 2-3 đơn hàng với sản phẩm khác nhau và kiểm tra tính tổng tiền.

from decimal import Decimal
from datetime import datetime

# Composition - Mối quan hệ "Có một" / HAS-A
# --- CLASS PRODUCT VÀ CUSTOMER ---
class Product:
    def __init__(self, product_id: str, name: str, price: str):
        self.product_id = product_id
        self.name = name
        self.price = Decimal(price) # dùng Decimal cho tiền

class Customer:
    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name

# --- ORDER ---
class Order: # Lúc khởi tạo Object VD: order1 = Order("ORD-001", cus1)
    """
    Class quản lý Đơn hàng.
    Bảo vệ tính toàn vẹn của danh sách sản phẩm và nghiệp vụ tính tiền.
    """
    def __init__(self, order_id: str, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        self.order_date = datetime.now()
        self.items = []
        self.quantities = []

        # Biến trạng thái để lưu discount
        self.discount_percent = Decimal('0')

    def add_item(self, product: Product, quantity: int):
        """Thêm sản phẩm vào giỏ hàng."""
        # Validation đầu vào
        if quantity <= 0:
            raise ValueError(f"Lỗi: Số lượng của {product.name} phải > 0.")

        # Kiểm tra xem sản phẩm đã có trong giỏ chưa (tránh trùng lặp logic)
        if product in self.items:
            index = self.items.index(product)
            # Hàm list.index(value) của Python có nhiệm vụ: Duyệt qua danh sách từ trái sang phải,
            # tìm xem value nằm ở vị trí số mấy (bắt đầu từ 0) và trả về con số đó.
            self.quantities[index] += quantity
            print(f"-> Đã cộng dồn thêm {quantity} {product.name}. Tổng: {self.quantities[index]}")
        else:
            # Thêm mới: Bắt buộc append cùng lúc để giữ đồng bộ index
            self.items.append(product)
            self.quantities.append(quantity)
            print(f"-> Thêm mới {quantity} x {product.name} vào đơn hàng.")

    def apply_discount(self, discount_percent: str):
        """Áp dụng mã giảm giá cho toàn bộ đơn hàng (0 - 100%)."""
        dec_discount = Decimal(discount_percent)
        if dec_discount < Decimal('0') or dec_discount > Decimal('100'):
            raise ValueError("Lỗi: Phần trăm giảm giá phải từ 0 đến 100.")

        self.discount_percent = dec_discount
        print(f"*** Đã áp dụng mã giảm giá {self.discount_percent}% cho toàn bộ đơn hàng! ***")

    def calculate_total(self) -> Decimal:
        """Tính tổng tiền đơn hàng (Đã bao gồm giảm giá)."""
        # Kiểm tra an toàn: Đảm bảo 2 list không bị lệch nhau trước khi dùng zip
        if len(self.items) != len(self.quantities):
            raise RuntimeError("Lỗi Hệ Thống (Data Corruption): Danh sách sản phẩm và số lượng không khớp nhau!")

        sub_total = Decimal('0')

        # Dùng zip để lặp 2 mảng song song
        for product, qty in zip(self.items, self.quantities):
            item_total = product.price * Decimal(qty)
            sub_total += item_total

        # Áp dụng giảm giá
        discount_amount = sub_total * (self.discount_percent / Decimal('100'))
        final_total = sub_total - discount_amount

        # Chuẩn hóa tiền (Làm tròn 2 chữ số thập phân chuẩn tài chính)
        # Nếu dùng VND thì không cần số lẻ, nhưng USD thì cần 2 số
        return final_total.quantize(Decimal('0.01'))

    def print_receipt(self):
        """Hàm helper để in biên lai đẹp mắt."""
        print(f"\n{'='*40}")
        print(f"HÓA ĐƠN: {self.order_id} | KHÁCH HÀNG: {self.customer.name}")
        print(f"NGÀY MUA: {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 40)
        for p, q in zip(self.items, self.quantities):
            print(f"{p.name:<20} x {q:<3} = ${(p.price * Decimal(q)):.2f}")
        print("-" * 40)
        print(f"GIẢM GIÁ: {self.discount_percent}%")
        print(f"TỔNG THANH TOÁN: ${self.calculate_total():.2f}")
        print(f"{'='*40}\n")

# TEST CODE
if __name__ == "__main__":
    # 1. Chuẩn bị Data
    cus1 = Customer("C01", "Alice")
    cus2 = Customer("C02", "Bob")

    p_laptop = Product("P1", "MacBook Pro", "2000")
    p_mouse = Product("P2", "Logitech Mouse", "50.50")
    p_keyboard = Product("P3", "Mechanical KB", "120")

    # 2. Tạo Đơn hàng 1 (Không giảm giá)
    print("--- TẠO ĐƠN HÀNG 1 ---")
    order1 = Order("ORD-001", cus1)
    order1.add_item(p_laptop, 1)
    order1.add_item(p_mouse, 2) # Cộng dồn item
    order1.print_receipt()

    # 3. Tạo Đơn hàng 2 (Có giảm giá)
    print("--- TẠO ĐƠN HÀNG 2 ---")
    order2 = Order("ORD-002", cus2)
    order2.add_item(p_mouse, 1)
    order2.add_item(p_keyboard, 2)

    order2.apply_discount('15') # Giảm giá 15%
    order2.print_receipt()

    # 4. Test validation (Bảo vệ hệ thống)
    print("--- TEST BẢO VỆ LỖI ---")
    try:
        order2.apply_discount('150') # Lỗi > 100%
    except ValueError as e:
        print(e)

    try:
        order2.add_item(p_keyboard, -5) # Lỗi âm số lượng
    except ValueError as e:
        print(e)

# Bài tập 4: Kế thừa - Tạo class SpecialCustomer từ Customer
# Xây dựng class SpecialCustomer kế thừa từ Customer với:
# • Thêm thuộc tính: loyalty_points (điểm thành viên), loyalty_level (mức VIP: Bronze, Silver, Gold)
# • Override phương thức __init__() sử dụng super()
# • Phương thức add_loyalty_points(points): tích lũy điểm từ mỗi mua hàng
# • Phương thức get_discount(): trả về mức giảm giá dựa trên loyalty_level (Bronze: 5%, Silver: 10%, Gold: 15%)
# • Phương thức __str__(): in thông tin khác với Customer thường
# Yêu cầu: Tạo một SpecialCustomer, mua hàng, tích lũy điểm và xem mức giảm giá tương ứng.

# --- CLASS CHA (Base Class) ---
class Customer:
    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name

    def __str__(self):
        return f"[Customer] ID: {self.customer_id} | Name: {self.name}"

# --- CLASS CON (Derived Class) ---
class SpecialCustomer(Customer):
    """
    Class quản lý Khách hàng VIP. Kế thừa từ Customer.
    """
    def __init__(self, customer_id: str, name: str, loyalty_points: int = 0):
        # 1. Gọi hàm __init__ của class Cha để setup ID và Name
        super().__init__(customer_id, name)
        
        # 2. Khởi tạo các thuộc tính riêng của class Con
        self.loyalty_points = loyalty_points
        self.loyalty_level = self._calculate_level() # Tự động tính level

    def _calculate_level(self) -> str:
        """Hàm nội bộ (private) để đánh giá hạng dựa trên điểm."""
        if self.loyalty_points >= 500:
            return "Gold"
        elif self.loyalty_points >= 200:
            return "Silver"
        else:
            return "Bronze"

    def add_loyalty_points(self, points: int):
        """Tích điểm sau khi mua hàng và tự động cập nhật hạng."""
        if points < 0:
            raise ValueError("Điểm tích lũy không được âm!")
        
        self.loyalty_points += points
        old_level = self.loyalty_level # So sánh để tạo hiệu ứng thưởng
        self.loyalty_level = self._calculate_level()
        
        print(f"-> {self.name} vừa được cộng {points} điểm. (Tổng: {self.loyalty_points})")
        
        # Thưởng hiệu ứng thăng hạng
        if old_level != self.loyalty_level:
            print(f"*** CHÚC MỪNG! {self.name} đã thăng hạng lên {self.loyalty_level.upper()}! ***")

    def get_discount(self) -> float:
        """Trả về phần trăm giảm giá dựa trên hạng."""
        # Dùng Dictionary mô phỏng Switch/Case, dễ bảo trì hơn if/else dài dòng
        discount_map = {
            "Bronze": 0.05, # 5%
            "Silver": 0.10, # 10%
            "Gold": 0.15    # 15%
        }
        # Nếu không tìm thấy, mặc định 0%
        return discount_map.get(self.loyalty_level, 0.0)

    # Ghi đè (Override) phương thức in thông tin của class Cha
    def __str__(self):
        return (f"[SpecialCustomer] ID: {self.customer_id} | Name: {self.name} "
                f"| Level: {self.loyalty_level} | Points: {self.loyalty_points}")

# ==========================================
# TEST CODE (DRY RUN)
# ==========================================
if __name__ == "__main__":
    print("1. KHỞI TẠO KHÁCH HÀNG VIP")
    # Alice bắt đầu với 100 điểm
    vip_cus = SpecialCustomer("V01", "Alice", loyalty_points=100)
    print(vip_cus) # Test __str__
    
    print("\n2. KIỂM TRA GIẢM GIÁ HIỆN TẠI")
    current_discount = vip_cus.get_discount()
    print(f"Mức giảm giá của {vip_cus.loyalty_level}: {current_discount * 100}%")

    print("\n3. MUA HÀNG VÀ TÍCH ĐIỂM (LẦN 1)")
    # Giả sử Alice mua đơn hàng lớn, được cộng 150 điểm
    vip_cus.add_loyalty_points(150) 
    print(vip_cus)
    
    print("\n4. MUA HÀNG VÀ TÍCH ĐIỂM (LẦN 2)")
    # Alice mua thêm, cộng 300 điểm
    vip_cus.add_loyalty_points(300)
    print(vip_cus)
    print(f"Mức giảm giá mới của {vip_cus.loyalty_level}: {vip_cus.get_discount() * 100}%")


# Bài tập 5: Polymorphism - Tạo class cho các loại sản phẩm khác nhau
# Xây dựng 3 class kế thừa từ Product:

# 1. PhysicalProduct (sản phẩm vật lý): thêm thuộc tính weight (cân nặng), shipping_fee (phí vận chuyển)
# 2. DigitalProduct (sản phẩm số): thêm thuộc tính file_size (MB), license_type (một lần / vĩnh viễn)
# 3. ServiceProduct (dịch vụ): thêm thuộc tính duration_days (ngày dùng), renewal_fee (phí gia hạn)
# Mỗi class phải override phương thức calculate_final_price():
# - PhysicalProduct: giá + phí vận chuyển
# - DigitalProduct: nếu license_type = 'one-time' thì giảm 20%, không thì giá gốc
# - ServiceProduct: tính giá cho duration_days, có phí gia hạn
# Yêu cầu: Tạo danh sách sản phẩm hỗn hợp, duyệt qua và in giá cuối cùng của mỗi sản phẩm.

from decimal import Decimal
from abc import ABC, abstractmethod

# 1. CLASS CHA (ABSTRACT BASE CLASS)
class Product(ABC): # Class trừu tượng, không thể tạo object trực tiếp 
    # và hợp đồng với các class sau phải có hàm để tính tiền.
    def __init__(self, product_id: str, name: str, base_price: str):
        self.product_id = product_id
        self.name = name
        self.base_price = Decimal(base_price)

    # Decorator này ép TẤT CẢ các class con bắt buộc phải có hàm này
    # Nếu class con không viết lại hàm này, Python sẽ báo lỗi ngay khi chạy!
    @abstractmethod
    def calculate_final_price(self) -> Decimal:
        pass

# 2. CÁC CLASS CON OVERRIDE LẠI LOGIC
class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, base_price: str, weight: float, shipping_fee: str):
        super().__init__(product_id, name, base_price)
        self.weight = weight
        self.shipping_fee = Decimal(shipping_fee)

    def calculate_final_price(self) -> Decimal:
        return self.base_price + self.shipping_fee

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, base_price: str, file_size: float, license_type: str):
        super().__init__(product_id, name, base_price)
        self.file_size = file_size
        self.license_type = license_type

    def calculate_final_price(self) -> Decimal:
        if self.license_type == 'one-time':
            # Giảm 20%
            return self.base_price * Decimal('0.8')
        return self.base_price

class ServiceProduct(Product):
    def __init__(self, product_id: str, name: str, base_price: str, duration_days: int, renewal_fee: str):
        super().__init__(product_id, name, base_price)
        self.duration_days = duration_days
        self.renewal_fee = Decimal(renewal_fee)

    def calculate_final_price(self) -> Decimal:
        # Giả sử base_price là giá mỗi ngày
        total = self.base_price * Decimal(self.duration_days)
        # Cộng thêm phí gia hạn nếu có
        return total + self.renewal_fee

# ==========================================
# 3. TEST KHẢ NĂNG CỦA ĐA HÌNH (POLYMORPHISM)
# ==========================================
if __name__ == "__main__":
    # Khởi tạo các sản phẩm khác biệt hoàn toàn
    iphone = PhysicalProduct("P01", "iPhone 15", "1000", weight=0.5, shipping_fee="20")
    win11 = DigitalProduct("D01", "Windows 11", "200", file_size=5000, license_type="one-time")
    adobe = DigitalProduct("D02", "Adobe CC", "50", file_size=2000, license_type="subscription")
    cleaning = ServiceProduct("S01", "Dọn dẹp nhà", "15", duration_days=3, renewal_fee="0")

    # Bỏ tất cả vào một giỏ hàng (Danh sách hỗn hợp)
    cart: list[Product] = [iphone, win11, adobe, cleaning] # Danh sách có luật của Product

    print(f"{'SẢN PHẨM':<20} | {'LOẠI':<15} | {'GIÁ CUỐI CÙNG'}")
    print("-" * 55)
    
    total_cart_value = Decimal('0')
    
    # MAGIC HAPPENS HERE: Vòng lặp không hề có lệnh IF/ELSE nào!
    for item in cart:
        # Hệ thống tự biết item nào gọi logic tính toán của class đó
        final_price = item.calculate_final_price()
        total_cart_value += final_price
        
        # item.__class__.__name__ để in ra tên Class cho dễ nhìn
        print(f"{item.name:<20} | {item.__class__.__name__:<15} | ${final_price:.2f}")
        
    print("-" * 55)
    print(f"TỔNG CỘNG GIỎ HÀNG: ${total_cart_value:.2f}")