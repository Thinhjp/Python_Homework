# Bài 1: In danh sách sản phẩm (có index)
# products = ["Áo", "Quần", "Giày", "Mũ"]
# i = 1
# for product in products:
#     print(f"{i}. {product}")
#     i += 1

# Bài 2: Tính tổng tiền giỏ hàng
# prices = [100000, 200000, 500000]
# tong_tien = 0
# # Sử dụng loop để tính tổng
# for price in prices:
#     tong_tien += price
# # In kết quả theo format yêu cầu
# print(f"Tổng tiền: {tong_tien} VND")


# Bài 3: Đếm sản phẩm giá cao
# prices = [100000, 500000, 700000, 200000]
# i = 0
# for price in prices:
#     if price > 300000:
#         i += 1
# print(f"Số sản phẩm có giá trên 300000 VND: {i}")


# Bài 4: Tìm giá lớn nhất
# prices = [100000, 500000, 700000, 200000]
# max_price = prices[0]
# for price in prices:
#     if price > max_price:
#         max_price = price
# print(f"Giá sản phẩm cao nhất: {max_price} VND")

# Bài 5: Tính tổng các số chẵn
# numbers = [1,2,3,4,5,6]
# tong_chan = 0
# for number in numbers:
#     if number % 2 == 0:
#         tong_chan += number
# print(f"Tổng các số chẵn: {tong_chan}")

# Bài 6: Bảng cửu chương mini
# for i in range(1, 6):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print()  
    
# Bài 7: Kiểm tra số nguyên tố
# n = 17
# so_nguyen_to = True
# if n < 2:
#     so_nguyen_to = False
# else:
#     for i in range(2, int(n**0.5) + 1):  # n**0.5 là căn bậc hai của 17
#         if n % i == 0:    
#             so_nguyen_to = False
#             break

# if so_nguyen_to:
#     print(f"{n} là số nguyên tố")
# else:
#     print(f"{n} không phải là số nguyên tố")

# Bài 8: Đếm số lần xuất hiện
# orders = ["A", "B", "A", "C", "A"]
# count = 0
# for order in orders:
#     if order == "A":
#         count += 1
# print(f"Số lần xuất hiện của 'A': {count}")

# Bài 9: Hàm tính tổng tiền
# def calculate_total(price, quantity):
#     total = price * quantity
#     return total

# Tong_tien = calculate_total(100000, 3)
# print(f"Tổng tiền: {Tong_tien} VND")

# Bài 10: Hàm kiểm tra đăng nhập
# def check_login(is_logged_in):
#     if is_logged_in:
#         return "Đã đăng nhập"
#     else:
#         return "Chưa đăng nhập"
# check = check_login(True)
# print(f"Trạng thái đăng nhập: {check}")

# Bài 11: Hàm giảm giá
# def apply_discount(price, percent):
#     giam_gia = int(price * (percent / 100))
#     gia_moi = price - giam_gia
#     return gia_moi

# gia_hien_tai = 200000
# gia_sau_giam = apply_discount(gia_hien_tai, 20)
# print(f"Giá hiện tại: {gia_hien_tai} VND")
# print(f"Giá sau khi giảm: {gia_sau_giam} VND")

# Bài 12: Hàm free ship
# def is_free_shipping(order_value):
#     if order_value >= 500000:
#         return True
#     else:
#         return False
# free_ship = is_free_shipping(600000)
# if free_ship:
#     print("Đơn hàng được miễn phí vận chuyển")
# else:
#     print("Đơn hàng không được miễn phí vận chuyển")

# Bài 13: Phân loại khách hàng
# def classify_customer(total_spent):
#     if total_spent >= 100000:
#         return "VIP"
#     elif total_spent >= 50000:
#         return "Gold"
#     else:
#         return "Normal"
# i1 = 1000000
# khach_hang1 = classify_customer(i1)
# print(f"Điểm thưởng hiện tại: {i1} USD")
# print(f"Hạng hiện tại: {khach_hang1}")

# # Bài 14: Validate email
# def is_valid_email(email):
#     if "@" and "." in email:
#         print ("Email hợp lệ")
#     else:
#         print("Email không hợp lệ")

# Bài 15: Tổng doanh thu
# def total_revenue(orders):
#     total = 0
#     for i in orders:
#         total += i
#     return total
# orders = [100000, 200000, 300000]
# tong_tien = total_revenue(orders)
# print(f"Tổng doanh thu là: {tong_tien}")

# Bài 16: Lọc giá cao
# def filter_prices(prices):
#     high = []
#     for i in prices:
#         if i > 300000:
#             high.append(i)
#     return high
# prices = [100000, 500000, 700000, 200000]
# gia_cao = filter_prices(prices)
# print(gia_cao)

# Bài 17: Đếm đơn hợp lệ

# def check_orders(orders):
#     n = 0
#     for i in orders:
#         if i > 0:
#             n += 1
#     return n
# orders = [100000, 0, 200000, -50000]
# Real_order = check_orders(orders)
# print("Số lượng đơn đặt hợp lệ:", Real_order)

# Bài 18: Tổng sau giảm giá
# def apply_discount(prices):
#     total = 0
#     for price in prices:
#         total = int (total + price - (price * 0.1))
#     return total
# prices = [100000, 200000, 300000]
# thanh_toan_sau_discount = apply_discount(prices)
# print("Tổng số tiền cần thanh toán:", thanh_toan_sau_discount)

# Bài 19: Lọc khách VIP
# def vip_checker(cart):
#     vip = True
#     for i in cart:
#         if i < 3000000:
#             vip = False
#     return vip
# cart = [200000, 1500000, 800000]
# customer = vip_checker(cart)
# if customer == True:
#     print("Khách này VIP")
# else:
#     print("Khách chưa VIP")

# Bài 20: Hệ thống thanh toán (mini backend)

# balance = 500000
# cart = [100000, 200000, 150000]
# def checkout(cart, balance):
#     total = 0
#     for i in cart:
#         total += i
#     so_du = balance - total
#     if total <= balance:
#         return {"status": "Thanh toán thành công", "Số dư còn lại": so_du}
#     else:
#         return {"status": "Không đủ tiền", "Số dư còn lại": balance}

# khach1 = checkout(cart, balance)
# print(khach1)
