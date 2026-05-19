from fastapi import APIRouter
from typing import List
from core.easy_services import filter_available, cart_total
from api.schemas import ProductInput, CartItem

router = APIRouter()

# API Câu 1 [cite: 14]
@router.post("/api/products/available")
def api_filter_available(products: List[ProductInput]):
    # Chuyển đổi list các Pydantic model thành list các dict
    products_dict = [p.dict() for p in products]
    
    # Gọi hàm nghiệp vụ và trả kết quả
    filtered = filter_available(products_dict)
    return filtered

# API Câu 2 [cite: 21]
@router.post("/api/cart/total")
def api_cart_total(cart: List[CartItem]):
    cart_dict = [item.dict() for item in cart]
    
    total = cart_total(cart_dict)
    # Trả về dạng JSON {"total": giá_trị} cho chuẩn format API
    return {"total": total}