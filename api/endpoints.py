# api/ (Tiền sảnh - Presentation Layer): Nơi tiếp khách, nhận order và trả món.

# endpoints.py (Lễ tân/Bồi bàn): nhận HTTP Request

# schemas.py (Menu/Quy định): Ép kiểu dữ liệu trước khi truyền (Data Validation).
from fastapi import APIRouter
from typing import List
from core.easy_services import filter_available, cart_total, order_message, classify_customer , active_users
from api.schemas import ProductInput, CartItem, OrderStatusInput, TotalSpentInput, UserInput

router = APIRouter()

# API Câu 1 
@router.post("/api/products/available")
def api_filter_available(products: List[ProductInput]):
    # Chuyển đổi list các Pydantic model thành list các dict
    products_dict = [p.dict() for p in products]
    
    # Gọi hàm nghiệp vụ và trả kết quả
    filtered = filter_available(products_dict)
    return filtered

# API Câu 2 
@router.post("/api/cart/total")
def api_cart_total(cart: List[CartItem]):
    cart_dict = [item.dict() for item in cart]
    
    total = cart_total(cart_dict)
    # Trả về dạng JSON 
    return {"total": total}

# API Câu 4
@router.post("/api/orders/message")
def api_order_message(payload: OrderStatusInput):
    # Gọi hàm nghiệp vụ và lấy kết quả
    message = order_message(payload.status)
    
    # JSON
    return {"message": message}

# API Câu 13
@router.post("/api/customer/classify")
def api_customer_classify(payload: TotalSpentInput):
    # Gọi hàm nghiệp vụ từ layer core và truyền dữ liệu đầu vào
    customer_tier = classify_customer(payload.total_spent)
    # Trả về kết quả dưới dạng JSON 
    return {"tier": customer_tier}

# API câu 15
@router.post("/api/admin/users/active")
def api_get_active_users(users: List[UserInput]):
    # Chuyển đổi dữ liệu Pydantic thành List of Dictionaries thuần
    users_dict = [u.model_dump() for u in users]
    
    # Gọi hàm nghiệp vụ cốt lõi
    filtered_users = active_users(users_dict)
    
    # Trả về kết quả
    return {"active_users": filtered_users}
