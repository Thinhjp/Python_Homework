from decimal import Decimal

class Product:
    def __init__(self, product_id: int, name: str, price: float, quantity: int, category: str):
        # Kiểm tra dữ liệu đầu vào hợp lệ
        if price < 0 or quantity < 0: # Giá và số lượng không thể là số âm
            raise ValueError("Giá và Số lượng tồn kho không được là số âm.")
            
        self.product_id = product_id
        self.name = name
        # Sử dụng Decimal để tránh lỗi làm tròn khi tính toán với float, 
        # đặc biệt là khi áp dụng giảm giá
        self.price = Decimal(str(price)) 
        self.quantity = quantity
        self.category = category

    def apply_discount(self, discount_percent: float) -> float:
        # Kiểm tra phần trăm giảm giá hợp lệ
        if not (0 <= discount_percent <= 100):
            raise ValueError("Phần trăm giảm giá phải nằm trong khoảng 0-100.")
            
        # Tính giá sau khi áp dụng giảm giá
        discount_amount = self.price * (Decimal(str(discount_percent)) / Decimal('100'))
        discounted_price = self.price - discount_amount
        
        return float(discounted_price) # Ép lại float để dễ hiển thị nếu cần

    def is_in_stock(self) -> bool:
        """
        Kiểm tra sản phẩm còn trong kho không.
        """
        return self.quantity > 0

    # Hàm magic __str__ giúp in object ra console đẹp mắt, dễ debug
    def __str__(self):
        stock_status = "Còn hàng" if self.is_in_stock() else "Hết hàng"
        return f"[{self.product_id}] {self.name} - Giá: {self.price:,.0f}đ - Tình trạng: {stock_status}"


# ==========================================
# CHẠY THỬ VỚI 2-3 SẢN PHẨM KHÁC NHAU
# ==========================================

if __name__ == "__main__":
    # 1. Khởi tạo sản phẩm
    p1 = Product(product_id=101, name="Bàn phím cơ Keychron", price=1500000, quantity=10, category="Electronics")
    p2 = Product(product_id=102, name="Chuột Logitech G102", price=450000, quantity=0, category="Electronics")
    p3 = Product(product_id=103, name="Balo Laptop", price=600000, quantity=5, category="Fashion")

    products = [p1, p2, p3]

    print("--- TRẠNG THÁI BAN ĐẦU ---")
    for p in products:
        print(p)

    print("\n--- KIỂM TRA LOGIC NGHIỆP VỤ ---")
    
    # Kiểm tra tồn kho và áp dụng giảm giá
    for p in products:
        if p.is_in_stock():
            # Chạy campaign: Giảm 20% cho tất cả hàng còn trong kho
            new_price = p.apply_discount(20)
            print(f"Khuyến mãi! {p.name} giảm 20% chỉ còn: {new_price:,.0f}đ")
        else:
            print(f"Rất tiếc! {p.name} đã hết hàng, không thể áp dụng khuyến mãi.")