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

# 02. Tính tổng giá trị giỏ hàng [LIST]

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
    
# 03. Gợi ý sản phẩm liên quan [LIST]

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
            
#04. Phát hiện đơn hàng bất thường [LIST]
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

# 05. Xếp hạng sản phẩm bán chạy theo tuần [LIST]
items = [
{"product_id": 1, "name": "Áo thun", "qty": 5, "price": 120000},
{"product_id": 2, "name": "Quần jean", "qty": 3, "price": 350000},
{"product_id": 1, "name": "Áo thun", "qty": 8, "price": 120000},
{"product_id": 3, "name": "Giày", "qty": 2, "price": 450000},
{"product_id": 2, "name": "Quần jean", "qty": 4, "price": 350000},
]
def get_qty(item):
    return item["total_qty"] #tạo hàm để lấy số lượng tổng của sản phẩm, để dùng làm key khi sort
def top_selling(items, top_n): #tạo hàm để lấy top sản phẩm bán chạy, truyền vào list items và số lượng top cần lấy
    grouped_items = {} #tạo dict để gom các sản phẩm cùng id lại với nhau, tránh bị lặp khi có nhiều đơn hàng cùng sản phẩm
    for item in items: 
        product_id = item["product_id"]
        if product_id not in grouped_items: #nếu id sản phẩm chưa có trong dict thì tạo mới, nếu đã có thì cộng dồn số lượng và doanh thu
            grouped_items[product_id] = {
                "name": item["name"],
                "total_qty": 0,
                "revenue": 0
            }
        grouped_items[product_id]["total_qty"] += item["qty"] #cộng dồn số lượng bán ra của sản phẩm
        grouped_items[product_id]["revenue"] += item["qty"] * item["price"] #cộng dồn doanh thu của sản phẩm
    result = [] #tạo list để lưu kết quả 
    for product_id, data in grouped_items.items(): #tạo vòng lặp từ dữ liệu đã gom
        formatted_data = { #định dạng lại dữ liệu bao gồm id sản phẩm, tên, tổng số lượng bán ra và doanh thu
            "product_id": product_id,  
            "name": data["name"],
            "total_qty": data["total_qty"],
            "revenue": data["revenue"]
        }
        result.append(formatted_data)
    result.sort(key=get_qty, reverse=True) #sắp xếp theo key lấy từ hàm def get_qty đã tạo ở trên
    return result[:top_n] #slice để lấy top n sản phẩm bán chạy nhất
print(top_selling(items, top_n=2))



