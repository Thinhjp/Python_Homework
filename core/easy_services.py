# core : Business Logic Layer nơi chứa logic chính để tính toán (Nhà bếp làm món)

# Câu 1: Lọc sản phẩm còn hàng [Dễ]
def filter_available(products):
    # Lọc sản phẩm có stock > 0 và is_active == True 
    return [p for p in products if p.get("stock", 0) > 0 and p.get("is_active") is True]

# Câu 2: Tính tổng tiền giỏ hàng [Dễ]
def cart_total(cart):
    # Tính tổng tiền = price * quantity cho từng item 
    return sum(item.get("price", 0) * item.get("quantity", 0) for item in cart)

# Câu 3: Áp dụng giảm giá phần trăm [Dễ] (Không tạo API)
def apply_discount(total, discount_percent):
    # Nếu discount_percent bằng 0 thì giữ nguyên total 
    if discount_percent == 0:
        return total
    
    # Tính số tiền sau giảm giá 
    return int(total * (1 - discount_percent / 100))

# Câu 4: Kiểm tra trạng thái đơn hàng [Dễ] (Tạo API)
def order_message(status: str) -> str:
    # Sử dụng Dictionary làm "Từ điển" mapping
    status_map = {
        "pending": "Chờ xử lý",
        "confirmed": "Đã xác nhận",
        "shipping": "Đang giao",
        "completed": "Hoàn thành",
        "cancelled": "Đã hủy"
    }
    
    # .get() nếu không tìm thấy key sẽ trả về giá trị mặc định
    return status_map.get(status.lower(), "Không hợp lệ")

# Câu 5: Tính phí vận chuyển theo khoảng cách [Dễ] (Không tạo API)
def shipping_fee(distance_km):
    ship_fee = 0
    if distance_km <= 5:
        ship_fee = 15000
    elif distance_km <= 10:
        ship_fee = 25000
    else:
        ship_fee = 40000
    return ship_fee

# Câu 6: Kiểm tra đăng nhập đơn giản [Dễ]
def login(username, password): 
    log = False
    if username == "admin" and password == "123456":
        log = True
    return log

# Câu 7: Đếm số đơn theo trạng thái [Dễ]
def count_status(statuses: list) -> dict:
    counted_status = {}
    for status in statuses:
        counted_status[status] = counted_status.get(status, 0) + 1
    return counted_status
    
# Câu 8: Tìm sản phẩm theo id [Dễ]
def find_product(products: list, product_id: str) -> dict | None:
    for product in products:
        if product.get("id") == product_id:
            return product
    return None

# Câu 9: Lọc đơn hàng có giá trị cao [Dễ]
def high_value_orders(orders: list, min_total: int) -> list:
    result = [] #tạo list chứa kết quả sau lọc
    for order in orders:
        if order.get("total", 0) >= min_total:
            result.append(order)
    return result

# Câu 10: Kiểm tra số dư trước khi thanh toán [Dễ]
def can_pay(balance: int, order_total:int) -> True:
    check = False
    if balance >= order_total:
        check = True
    return check

# Câu 11: Cập nhật tồn kho sau khi bán [Dễ]
def update_stock(stock: int, sold_quantity: int) -> int:
    stock =- sold_quantity
    return stock

# Câu 12: Tính điểm tích lũy khách hàng [Dễ]
def loyalty_points(order_total: int) -> int:
    point = order_total // 10000
    return point

# Câu 13: Phân loại khách hàng theo tổng chi tiêu [Dễ] (Tạo API)
def classify_customer(total_spent:int) -> str:
    customer_class = "Normal"
    if 1000000 <= total_spent < 5000000:
        customer_class = "Silver"
    elif total_spent >= 5000000:
        customer_class = "Gold"
 
# Câu 14: Kiểm tra email hợp lệ cơ bản [Dễ]
def is_valid_email(email: str) -> True:
    check = False
    if "@" and ".com" in email:
        check = True
    return check

# Câu 15: Lọc người dùng đang hoạt động [Dễ] (Tạo API)
def active_users(users: list) -> list:
    """
    Lọc ra những user có trạng thái đang hoạt động.
    """
    # return [user for user in users if user.get("is_active")] - List Comprehension
    active = []
    for user in users:
        if user.get("is_active"):
            active.append(user)
    return active 




        



