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
def count_status(statuses):
    counted_status = {}
    for status in statuses:
        


        



