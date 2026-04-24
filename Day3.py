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
orders = [
{"id": 101, "total": 250000},
{"id": 102, "total": 180000},
{"id": 103, "total": 920000},
{"id": 104, "total": 210000},
{"id": 105, "total": 195000},
]
def detect_anomalies(orders, threshold=2.5):
    if orders == None:
        return[]
    
    total = sum(order["total"] for order in orders)
    # Trung bình
    avg = total / len(orders)
    #Tạo giới hạn
    limit = avg * threshold
    anomalies = []
    for ord in orders:
        if ord["total"] > limit:
            anomalies.append(ord)
    return anomalies
print(detect_anomalies(orders))

    

