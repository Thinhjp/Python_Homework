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

cart = [
{"name": "Áo thun", "price": 120000, "quantity": 2},
{"name": "Quần dài", "price": 350000, "quantity": 1},
{"name": "Tất", "price": 25000, "quantity": 3},
]

def cart_total(cart, discount=0.1):
    customer = []
    final_total = 0
    for pro in cart:
        cus = list(pro.values())
        total = int (pro["price"] * pro["quantity"] * 0.9)
        final_total += total
        customer.append(cus)
    return f"{customer} final price is: {final_total}"

print(cart_total(cart), "VND")
    
# 03. Gợi ý sản phẩm liên quan [LIST]

products = [
{"id": 1, "name": "Áo polo", "category": "ao", "rating": 4.5},
{"id": 2, "name": "Áo thun", "category": "ao", "rating": 4.8},
{"id": 3, "name": "Áo khoác", "category": "ao", "rating": 4.2},
{"id": 4, "name": "Quần jeans","category": "quan","rating": 4.7},
{"id": 5, "name": "Áo sơ mi", "category": "ao", "rating": 4.6},
]

def related_products(product_id = 1, products=products, limit = 3):
    sort_pro = []
    for pro in products:
        if pro["id"] == 1 and pro["category"] == "ao" and :
            
