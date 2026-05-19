# Câu 1: Lọc sản phẩm còn hàng [Dễ]
def filter_available(products):
    # Lọc sản phẩm có stock > 0 và is_active == True [cite: 17]
    return [p for p in products if p.get("stock", 0) > 0 and p.get("is_active") is True]

# Câu 2: Tính tổng tiền giỏ hàng [Dễ]
def cart_total(cart):
    # Tính tổng tiền = price * quantity cho từng item [cite: 23]
    return sum(item.get("price", 0) * item.get("quantity", 0) for item in cart)

# Câu 3: Áp dụng giảm giá phần trăm [Dễ] (Không tạo API)
def apply_discount(total, discount_percent):
    # Nếu discount_percent bằng 0 thì giữ nguyên total [cite: 28]
    if discount_percent == 0:
        return total
    
    # Tính số tiền sau giảm giá [cite: 27]
    return int(total * (1 - discount_percent / 100))