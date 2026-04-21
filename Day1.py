# Bài 1: Tính tổng tiền đơn hàng
# price = 120000
# quantity = 3
# total = price * quantity
# print("Tổng tiền: ", total, "VND")

# Bài 2: Áp dụng giảm giá sản phẩm
# price = 500000
# discount_percent = 10 
# discount_amount = int(price * discount_percent / 100)
# final_price = price - discount_amount
# print("Giá gốc: ", price, "VND")
# print("Giảm giá: ", discount_amount, "VND")
# print("Giá sau khi giảm: ", final_price, "VND")

# Bài 3: Tính lương nhân viên
# name = "THINH"
# salary_per_day = 300000
# working_days = 22
# total_salary = salary_per_day * working_days
# print("Tên nhân viên: ", name)
# print("Tổng lương tháng: ", total_salary, "VND")

# Bài 4: Tính phí vận chuyển
# distance_km = 12
# cost_per_km = 5000
# total_cost = distance_km * cost_per_km
# print("Tổng chi phí vận chuyển: ", total_cost, "VND")

# Bài 5: Kiểm tra dung lượng lưu trữ
# total_storage = 256
# used_storage = 180 
# remaining_storage = total_storage - used_storage
# print("Dung lượng lưu trữ còn lại: ", remaining_storage, "GB")

# Bài 6: Kiểm tra khả năng thanh toán
# balance = 200000
# item_price = 150000
# if balance >= item_price:
#     balance -= item_price
#     print("Thanh toán thành công! Số dư còn lại: ", balance, "VND")
# else:
#     print("Bạn không đủ tiền trong tài khoản")

# Bài 7: Điều kiện miễn phí vận chuyển
# order_value = 250000
# if order_value >= 200000:
#     print("Bạn được miễn phí vận chuyển!")


# Bài 8: Phân quyền người dùng
# is_logged_in = True
# is_admin = False
# if is_logged_in and not is_admin:
#     print("Bạn đã đăng nhập nhưng không phải là quản trị viên.")


# Bài 9: Kiểm tra giờ làm việc
# hour = 14
# if 9 <= hour <= 18:
#     print("Đang trong giờ làm việc.")


# Bài 10: Kiểm tra email hợp lệ (cơ bản)
# email = "user@gmail.com"
# if "@" in email and "." in email:
#     print("Địa chỉ email hợp lệ.")
# else:
#     print("Địa chỉ email không hợp lệ.")

# Bài 11: Tính phí vận chuyển theo giá trị đơn
# order_value = 180000
# total = order_value 
# if order_value >= 200000:
#     total = order_value 
# else:
#     total = order_value + 30000
# print("Tổng giá trị đơn hàng: ", total, "VND")


# Bài 12: Tính thưởng nhân viên
# performance_score = 8.2
# if performance_score >= 9:  
#     print("Thưởng 5000000 VND")
# elif performance_score >= 7:
#     print("Thưởng 2000000 VND")
# else:
#     print("Không được thưởng")


# Bài 13: Mapping trạng thái đơn hàng
# status_code = 2
# if status_code == 1:
#     print("Pending")
# elif status_code == 2:
#     print("Shipping")
# elif status_code == 3:
#      print("Delivered")
# else:
#     print("Unknown")


# Bài 14: Tính giá vé theo độ tuổi
# age = 15
# if age < 12:
#     print("50000 VND")
# elif 12 <= age < 18:
#     print("70000 VND")
# elif age == 18:
#     print("100000 VND")


# Bài 15: Phân loại khách hàng
# total_spent = 1200000
# if total_spent >= 1000000:
#     print("VIP")
# elif total_spent >= 500000:
#     print("Gold")
# elif total_spent < 500000:
#     print("Normal")


# Bài 16: Tính tiền điện theo bậc
# kwh = 135
# if kwh <= 50:
#     print("Tiền điện mức 1: ", kwh * 1678, "VND")
# elif 50 < kwh <= 100:
#     print("Tiền điện mức 2: ", kwh * 1734, "VND")
# elif 100 < kwh <= 200:
#     print("Tiền điện mức 3: ", kwh * 2014, "VND")


# Bài 17: Tính lương có thưởng KPI
# base_salary = 10000000
# kpi = 0.85
# if kpi >= 0.9:
#     bonus = int(base_salary * 0.3)
# elif 0.8 <= kpi < 0.9:
#     bonus = int(base_salary * 0.1)
# else:
#     bonus = 0
# total_salary = base_salary + bonus
# print("Lương cơ bản: ", base_salary, "VND")
# print("Thưởng: ", bonus, "VND")
# print("Tổng lương: ", total_salary, "VND")

# Bài 18: Tính giá taxi
# distance = 12
# if distance < 1:
#     taxi_fee = 15000
# elif 2 <= distance < 10:
#     taxi_fee = 15000 + (distance - 1) * 12000 
# else:
#     taxi_fee = 15000 + 9* 12000 + (distance - 10) * 10000
# print("Số km: ", distance, "km")
# print("Tiền taxi: ", taxi_fee, "VND")

# Bài 19: Kiểm tra điều kiện vay
# income = 15000000
# debt = 3000000
# if income >= 10000000 and debt <= income * 0.5:
#     print("Bạn đủ điều kiện vay")
# else:
#     print("Bạn không đủ điều kiện vay") 


# Bài 20: Áp dụng nhiều điều kiện giảm giá
# price = 1000000
# is_member = True
# voucher = 100000
# if is_member:
#     membership_discount = int(price * 0.1)
# else:
#     membership_discount = 0
# final_price = price - membership_discount - voucher
# if final_price < 0:
#     final_price = 0
# print("Giá sau khi áp dụng mã giảm giá:", final_price)
