# # 01. Lọc sản phẩm còn hàng [LIST]
# products = [
# {"id": 1, "name": "Áo thun", "stock": 10, "is_active": True},
# {"id": 2, "name": "Quần jean", "stock": 0, "is_active": True},
# {"id": 3, "name": "Giày sneaker","stock": 5, "is_active": False},
# {"id": 4, "name": "Nón baseball","stock": 3, "is_active": True},
# ]
# def filter_available(products):
#     product = []
#     for i in products:
#         if i["stock"] > 0 and i["is_active"] == True:
#             product.append(i)
#     return product

# in_test = filter_available(products)
# print(in_test)

# # 02. Tính tổng giá trị giỏ hàng [LIST]

# cart = [
# {"name": "Áo thun", "price": 120000, "quantity": 2},
# {"name": "Quần dài", "price": 350000, "quantity": 1},
# {"name": "Tất", "price": 25000, "quantity": 3},
# ]

# def cart_total(cart, discount=0.1):
#     customer = []
#     final_total = 0
#     for pro in cart:
#         cus = list(pro.values())
#         total = int (pro["price"] * pro["quantity"] * 0.9)
#         final_total += total
#         customer.append(cus)
#     return f"{customer} final price is: {final_total}"

# print(cart_total(cart), "VND")
    
# # 03. Gợi ý sản phẩm liên quan [LIST]

# products = [
# {"id": 1, "name": "Áo polo", "category": "ao", "rating": 4.5},
# {"id": 2, "name": "Áo thun", "category": "ao", "rating": 4.8},
# {"id": 3, "name": "Áo khoác", "category": "ao", "rating": 4.2},
# {"id": 4, "name": "Quần jeans","category": "quan","rating": 4.7},
# {"id": 5, "name": "Áo sơ mi", "category": "ao", "rating": 4.6},
# ]

# def related_products(product_id, products, limit):
#     # tạo vòng lặp để lấy category từ id được truyền vào. VD: truyền id = 1 thì lấy "ao"
#     get_category = None
#     for pro in products:
#         if pro["id"] == product_id:
#             get_category = pro["category"]
#             break
#     if get_category == None: #nếu key truyền vào không xuất hiện thì end sớm về chuỗi rỗng
#         return []
#     # Gom các sản phẩm chung category nhưng khác id, để không bị lặp sản phẩm hiện tại đang input vào.
#     filtered_list = []
#     for pro in products:
#         if pro["category"] == get_category and pro["id"] != product_id:
#             filtered_list.append(pro)
#     def rate(item):
#         return item["rating"]
#     sorted_list = sorted(filtered_list, key = rate, reverse=True)
#     return sorted_list[:limit]

# test = related_products(product_id=1, products=products, limit=3)
# print(test)
            
# # 04. Phát hiện đơn hàng bất thường [LIST]
# orders = [
# {"id": 101, "total": 250000},
# {"id": 102, "total": 180000},
# {"id": 103, "total": 920000},
# {"id": 104, "total": 210000},
# {"id": 105, "total": 195000},
# ]
# def detect_anomalies(orders, threshold=2.5):
#     if orders == None:
#         return[]
#     total = 0
#     for order in orders:
#         total += order["total"]
#     # Trung bình
#     avg = total / len(orders)
#     #Tạo giới hạn
#     limit = avg * threshold
#     anomalies = []
#     for ord in orders:
#         if ord["total"] > limit:
#             anomalies.append(ord)
#     return anomalies
# print(detect_anomalies(orders))

# # 05. Xếp hạng sản phẩm bán chạy theo tuần [LIST]
# items = [
# {"product_id": 1, "name": "Áo thun", "qty": 5, "price": 120000},
# {"product_id": 2, "name": "Quần jean", "qty": 3, "price": 350000},
# {"product_id": 1, "name": "Áo thun", "qty": 8, "price": 120000},
# {"product_id": 3, "name": "Giày", "qty": 2, "price": 450000},
# {"product_id": 2, "name": "Quần jean", "qty": 4, "price": 350000},
# ]
# def get_qty(item):
#     return item["total_qty"] #tạo hàm để lấy số lượng tổng của sản phẩm, để dùng làm key khi sort
# def top_selling(items, top_n): #tạo hàm để lấy top sản phẩm bán chạy, truyền vào list items và số lượng top cần lấy
#     grouped_items = {} #tạo dict để gom các sản phẩm cùng id lại với nhau, tránh bị lặp khi có nhiều đơn hàng cùng sản phẩm
#     for item in items: 
#         product_id = item["product_id"]
#         if product_id not in grouped_items: #nếu id sản phẩm chưa có trong dict thì tạo mới, nếu đã có thì cộng dồn số lượng và doanh thu
#             grouped_items[product_id] = {
#                 "name": item["name"],
#                 "total_qty": 0,
#                 "revenue": 0
#             }
#         grouped_items[product_id]["total_qty"] += item["qty"] #cộng dồn số lượng bán ra của sản phẩm
#         grouped_items[product_id]["revenue"] += item["qty"] * item["price"] #cộng dồn doanh thu của sản phẩm
#     result = [] #tạo list để lưu kết quả 
#     for product_id, data in grouped_items.items(): #tạo vòng lặp từ dữ liệu đã gom
#         formatted_data = { #định dạng lại dữ liệu bao gồm id sản phẩm, tên, tổng số lượng bán ra và doanh thu
#             "product_id": product_id,  
#             "name": data["name"],
#             "total_qty": data["total_qty"],
#             "revenue": data["revenue"]
#         }
#         result.append(formatted_data)
#     result.sort(key=get_qty, reverse=True) #sắp xếp theo key lấy từ hàm def get_qty đã tạo ở trên
#     return result[:top_n] #slice để lấy top n sản phẩm bán chạy nhất
# print(top_selling(items, top_n=2))


# # 06. Xây dựng catalog sản phẩm [DICT]
# products = [
# {"id": "SP001", "name": "Áo thun basic", "price": 120000,
# "category": "ao"},
# {"id": "SP002", "name": "Quần jogger", "price": 280000,
# "category": "quan"},
# {"id": "SP003", "name": "Nón bucket", "price": 95000,
# "category": "phu_kien"},
# ]
# def build_catalog(products):
#     # 1. Khởi tạo một dictionary rỗng để chứa kết quả
#     catalog = {} 
    
#     # 2. Bắt đầu duyệt qua từng sản phẩm trong danh sách
#     for product in products:
        
#         # 3. Lấy ra mã ID của sản phẩm hiện tại để làm Key
#         product_id = product["id"] 
        
#         # 4. Lưu vào dictionary: Gán Key (product_id) = Value (toàn bộ data của product)
#         catalog[product_id] = product 
        
#     # 5. Trả về kết quả cuối cùng Dict lồng
#     return catalog
# print(build_catalog(products))
# #Test ngoài bài 6
# #Cách lấy dữ liệu bên trong dict lồng
# catalog = build_catalog(products)
# print(catalog["SP002"]["price"]) #Lấy price của SP002

# # 07. Thống kê đơn hàng theo trạng thái [DICT]

# statuses = ["confirmed", "pending", "shipped", "confirmed", "delivered",
# "pending", "cancelled", "confirmed", "shipped", "delivered"]

# def count_by_status(statuses):
#     counts = {}
#     for status in statuses:
#         counts[status] = counts.get(status,0) + 1 
#         #hàm get xét giá trị dict mới counts, counts[status] 
#         # tạo giá trị mới nếu chưa có hoặc cập nhật value nếu trùng key.
#     return counts
# print(count_by_status(statuses))

# # 08. Áp dụng mã giảm giá [DICT]
# coupon_db = {
# "SALE20": {"type": "percent", "value": 20, "min_order": 200000},
# "SHIP50K": {"type": "fixed", "value": 50000, "min_order":
# 150000},
# "VIP30": {"type": "percent", "value": 30, "min_order": 500000},
# }
# def apply_coupon(cart_total: int, code: str, coupon_db: dict) -> dict:
#     # 1. Early Return: Mã không tồn tại
#     coupon = coupon_db.get(code)
#     if not coupon:
#         return {"valid": False, "message": "Mã không tồn tại"}

#     # 2. Early Return: Không đủ điều kiện tối thiểu
#     if cart_total < coupon["min_order"]:
#         return {
#             "valid": False, 
#             "message": f"Đơn hàng tối thiểu để áp dụng mã là {coupon['min_order']}đ"
#         }

#     # 3. Xử lý Logic cốt lõi
#     discount_amount = 0
#     if coupon["type"] == "percent":
#         discount_amount = int(cart_total * (coupon["value"] / 100))
#     elif coupon["type"] == "fixed":
#         discount_amount = coupon["value"]
#     # đảm bảo nếu kết quả < 0 thì lấy số 0
#     final_price = cart_total - discount_amount
#     if final_price < 0:
#         final_price = 0

#     # 5. Trả về kết quả
#     return {
#         "valid": True,
#         "discount_amount": discount_amount,
#         "final_price": final_price,
#         "message": f"Áp dụng thành công {code} (-{coupon['value']}{'%' if coupon['type'] == 'percent' else 'đ'})"
#     }
# print(apply_coupon(cart_total=350000, code="SHIP50K", coupon_db=coupon_db))

# # 09. Tổng hợp báo cáo doanh thu theo ngày [DICT]
# transactions = [
# {"date": "2024-01-15", "amount": 320000},
# {"date": "2024-01-15", "amount": 185000},
# {"date": "2024-01-16", "amount": 450000},
# {"date": "2024-01-15", "amount": 270000},
# {"date": "2024-01-16", "amount": 390000},
# ]

# def daily_report(transactions):
#     report = {}

#     # Duyệt qua từng giao dịch để gom nhóm
#     for item in transactions:
#         date = item["date"]
#         amount = item["amount"]

#         # Date chưa có trong dict thì tạo mới
#         if date not in report:
#             report[date] = {
#                 "total": 0,
#                 "count": 0
#             }

#         # Cộng dồn total và đếm nếu Date trong Dict
#         report[date]["total"] += amount
#         report[date]["count"] += 1

#     # BƯỚC 2: Tính toán giá trị trung bình sau khi đã có tổng số
#     for date in report:
#         total = report[date]["total"]
#         count = report[date]["count"]
        
#         # Thêm key 'avg' vào dict của ngày đó, hàm trung bình cộng
#         report[date]["avg"] = round(total / count, 2)

#     return report
# print(daily_report(transactions))

# # 10. Quản lý phiên đăng nhập [DICT]

# import time

# class SessionStore:
#     def __init__(self, timeout=1800):
#         # Dictionary lưu trữ toàn bộ session
#         self.sessions = {}
#         # Thời gian sống mặc định của 1 session (tính bằng giây)
#         self.timeout = timeout

#     def create(self, user_id, data):
#         # Lấy mốc thời gian hiện tại (giây)
#         current_time = int(time.time())
        
#         # Tạo bản ghi lưu vào dictionary
#         self.sessions[user_id] = {
#             "user_id": user_id,
#             "data": data,
#             "created_at": current_time,
#             "expires_at": current_time + self.timeout
#         }

#     def get(self, user_id):
#         # 1. Kiểm tra xem user có trong hệ thống không
#         if user_id not in self.sessions:
#             return None
        
#         # 2. Lấy session ra để kiểm tra
#         session = self.sessions[user_id]
#         current_time = int(time.time())

#         # 3. Kiểm tra hạn sử dụng (Lazy Expiration)
#         if current_time > session["expires_at"]:
#             # Đã quá hạn -> Xóa rác và báo không tìm thấy
#             self.delete(user_id)
#             return None
        
#         # 4. Hợp lệ -> Trả về dữ liệu
#         return session

#     def delete(self, user_id):
#         # Kiểm tra trước khi xóa để tránh lỗi KeyError
#         if user_id in self.sessions:
#             del self.sessions[user_id]


# if __name__ == "__main__":
#     #tạo vật thật store từ class(bản vẽ)
#     store = SessionStore(timeout=1800) # 30 phút
    
#     # gọi hàm từ class ra
#     store.create("user_123", {"name": "An", "role": "customer"})
    
#     # Lấy session
#     session = store.get("user_123")
#     print(session)
    
#     # Xóa session
#     store.delete("user_123")
    
#     # Lấy lại sau khi xóa
#     print(store.get("user_123"))

# # 11. Hệ thống phân quyền RBAC [DICT]
# rbac = {
# "admin": {"products": ["read","create","update","delete"],

# "orders": ["read","update","delete"]},
# "seller": {"products": ["read","create","update"],

# "orders": ["read"]},

# "customer": {"orders": ["read","create"]},
# }

# def check_permission(role, resource, action, rbac):
#     return action in rbac.get(role, {}).get(resource, []) 
#     # Sử dụng phương thức get để truy cập vào role và resource,
#     # nếu role tồn tại sẽ trả về dict chứa resource, 
#     #dict resource sẽ trả về list quyền của resource đó.
#     # nếu không tồn tại sẽ trả về dict rỗng, tránh lỗi KeyError.
#     # Kiểm tra xem action có trong list quyền của resource đó hay không, 
#     # trả về True hoặc False.

# # Test cases
# print(check_permission("seller", "products", "delete", rbac)) # False
# print(check_permission("admin", "orders", "delete", rbac)) # True
# print(check_permission("customer", "products", "read", rbac)) # False

# # 12. Tính phí vận chuyển theo vùng [DICT]
# shipping_zones = {
# "HN": {"zone_rate": 15000, "free_threshold": 300000, "min_fee":
# 15000},
# "HCM": {"zone_rate": 15000, "free_threshold": 300000, "min_fee":
# 15000},
# "DN": {"zone_rate": 20000, "free_threshold": 350000, "min_fee":
# 20000},
# "other": {"zone_rate": 30000, "free_threshold": 500000, "min_fee":
# 30000},
# }
# def calc_shipping(city, weight_kg, order_total, zones):
#     zone = zones.get(city, zones["other"]) 
#     # Lấy thông tin vùng dựa trên thành phố, 
#     #nếu không tìm thấy thì lấy vùng "other"
#     if order_total >= zone["free_threshold"]: 
#         # Nếu tổng đơn hàng vượt ngưỡng miễn phí, trả về 0
#         return {"fee": 0, 
#                 "free_shipping": True, 
#                 "message": f"Đơn hàng đủ điều kiện miễn phí ship đến {city}!"}
#     else:
#         return {"fee": max(int(zone["zone_rate"] * weight_kg), zone["min_fee"]), 
#                 "free_shipping": False,
#                 "message": f"Phí ship đến {city}: {max(int(zone['zone_rate'] * weight_kg), zone['min_fee']):,}đ"} 
#         # Tính phí dựa trên trọng lượng và so sánh với phí tối thiểu, 
#         #trả về giá cao hơn


# # Test cases
# print(calc_shipping(city="DN", weight_kg=1.5, order_total=200000, zones=shipping_zones))
# print(calc_shipping(city="HaiPhong", weight_kg=1.5, order_total=100000, zones=shipping_zones))
# print(calc_shipping(city="HN", weight_kg=1.5, order_total=500000, zones=shipping_zones))

# # 14. Tìm sản phẩm chưa được xem [SET]
# all_products = {"SP001","SP002","SP003","SP004","SP005","SP006"}
# viewed_products = {"SP001","SP003","SP005"}
# def get_unviewed(all_products, viewed_products):
#     return all_products - viewed_products 
#     # Sử dụng phép trừ tập hợp để tìm các sản phẩm chưa được xem, 
#     #trả về một set mới chứa các phần tử thuộc all_products nhưng không thuộc viewed_products   

# # Test case
# print(get_unviewed(all_products, viewed_products))

# # 15. Lấy danh sách danh mục duy nhất [SET]
# products = [
# {"name": "Áo thun", "category": "ao"},
# {"name": "Quần jean", "category": "quan"},
# {"name": "Áo khoác", "category": "ao"},
# {"name": "Giày", "category": "giay"},
# {"name": "Áo polo", "category": "ao"},
# ]
# def unique_categories(products):
#     categories = set() #tạo một set rỗng để lưu trữ các danh mục duy nhất
#     for product in products: #duyệt qua từng sản phẩm trong danh sách
#         categories.add(product["category"]) #thêm category của sản phẩm vào set, nếu đã tồn tại thì sẽ không bị thêm vào nữa
#     return categories #trả về set chứa các danh mục duy nhất
# # Test case
# print(unique_categories(products))

# # 16. Gợi ý sản phẩm cùng mua (cross-sell) [SET]
# order_history = [
# {"items": ["SP001","SP002","SP005"]},
# {"items": ["SP001","SP003"]},
# {"items": ["SP001","SP002","SP004"]},
# {"items": ["SP006","SP002"]},
# ]
# current_cart = {"SP001", "SP003"}

# def cross_sell(product_id, order_history, current_cart):
#     co_purchased = set() 
#     #tạo một set rỗng. Set sẽ tự động loại bỏ các giá trị trùng lặp.
#         #duyệt qua từng đơn hàng trong lịch sử mua hàng
#         items = set(order["items"]) 
#         #tạo set có giá trị duy nhất từ Dict. Không bị lặp.
#         if product_id in items: 
#             #kiểm tra nếu sản phẩm hiện tại có trong items.
#             co_purchased.update(items) 
#             #thêm tất cả sản phẩm trong đơn hàng đó vào set co_purchased
#     co_purchased.discard(product_id) 
#     #loại bỏ sản phẩm hiện tại khỏi set co_purchased để không gợi ý lại chính nó
#     recommendations = co_purchased - current_cart 
#     # loại bỏ những sản phẩm đã có trong giỏ hàng hiện tại
#     return recommendations 
# print(cross_sell("SP001", order_history, current_cart))

# # 17. Phát hiện sản phẩm bị xóa khỏi flash sale [SET]

# old_sale = {"SP001","SP002","SP003","SP004","SP005"}
# new_sale = {"SP002","SP004","SP005","SP006","SP007"}
# def sale_diff(old_sale, new_sale):
#     removed = old_sale - new_sale 
#     # Sản phẩm bị xóa khỏi flash sale.
#     added = new_sale - old_sale 
#     # Sản phẩm được thêm vào flash sale. 
#     kept = old_sale & new_sale 
#     # Sản phẩm giữ nguyên trong flash sale.
#     return {
#         "removed": removed,
#         "added": added,
#         "kept": kept
#     }
# # Test case
# print(sale_diff(old_sale, new_sale))

# # 18. Lọc review hợp lệ theo người dùng đã mua [SET]

# verified_buyers = {"U001", "U003", "U005", "U007"}
# reviews = [
# {"user_id": "U001", "rating": 5, "comment": "Rất tốt!"},
# {"user_id": "U002", "rating": 1, "comment": "Kém chất lượng"},
# {"user_id": "U003", "rating": 4, "comment": "Ưng ý"},
# {"user_id": "U004", "rating": 5, "comment": "Tuyệt vời"},
# ]
# def filter_verified_reviews(reviews, verified_buyers):
#     valid_reviews = [] 
#     #tạo một list rỗng để lưu trữ các review hợp lệ
#     for review in reviews:
#         if review["user_id"] in verified_buyers: 
#             # Kiểm tra nếu user_id của review có trong set verified_buyers
#             valid_reviews.append(review) 
#             # Nếu có thì thêm review đó vào danh sách valid_reviews
#     return valid_reviews

# # Test case
# print(filter_verified_reviews(reviews, verified_buyers))

# # 19. Phân tích hành vi mua hàng theo segment [SET]

# order_counts = {
# "U001": 1, "U002": 7, "U003": 3, "U004": 1,
# "U005": 5, "U006": 2, "U007": 9, "U008": 4,
# }
# def segment_users(order_counts):
#     segments = {
#         "one_time": set(),
#         "repeat": set(),
#         "vip": set()
#     }
#     for user_id, count in order_counts.items():
#         if count == 1:
#             segments["one_time"].add(user_id) 
#             # Thêm user_id vào segment one_time nếu chỉ mua 1 lần
#         elif 2 <= count < 5:
#             segments["repeat"].add(user_id) 
#             # Thêm user_id vào segment repeat nếu mua từ 2 đến 5 lần
#         elif count >= 5:
#             segments["vip"].add(user_id) 
#             # Thêm user_id vào segment vip nếu mua hơn 5 lần
#     return segments

# # Test case
# print(segment_users(order_counts))

# 20. Kiểm tra xung đột kho hàng trong flash sale [SET]

active_campaigns = {
"clearance": {"SP001","SP005","SP009"},
"bundle_deal": {"SP003","SP007","SP011"},
"new_arrival": {"SP013","SP015"},
}
flash_sale_items = {"SP001","SP003","SP007","SP020","SP025"}

def check_conflicts(flash_sale_items, active_campaigns):
    conflicts = []
    safe_items = []
    has_conflict = False
    for item in flash_sale_items:
        print(item)
        for key, value in active_campaigns.items():
            if item in value:
                conflicts.append(item) 
                # Nếu item có trong bất kỳ chiến dịch nào, thêm vào list conflicts
                has_conflict = True 
                # Đánh dấu có xung đột
                break 
                # Dừng vòng lặp kiểm tra các chiến dịch khác nếu đã phát hiện xung đột
    safe_items = flash_sale_items - set(conflicts)

    return{"has_conflict": has_conflict,
            "conflicts": conflicts,
            "safe_items": safe_items
}
# Test case
print(check_conflicts(flash_sale_items, active_campaigns))