from pydantic import BaseModel

# Input mẫu cho Câu 1 
class ProductInput(BaseModel):
    id: int
    name: str
    stock: int
    is_active: bool

# Input mẫu cho Câu 2 
class CartItem(BaseModel):
    name: str
    price: int
    quantity: int