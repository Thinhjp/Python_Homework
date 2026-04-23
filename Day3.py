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
    