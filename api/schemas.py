# api/ (Tiền sảnh - Presentation Layer): Nơi tiếp khách, nhận order và trả món.

# endpoints.py (Lễ tân/Bồi bàn): nhận HTTP Request

# schemas.py (Menu/Quy định): Ép kiểu dữ liệu trước khi truyền (Data Validation).
from pydantic import BaseModel

# Input cho Câu 1 
class ProductInput(BaseModel):
    id: int
    name: str
    stock: int
    is_active: bool

# Input cho Câu 2 
class CartItem(BaseModel):
    name: str
    price: int
    quantity: int

# Input cho Câu 4
class OrderStatusInput(BaseModel):
    status: str

# Input cho Câu 13
class TotalSpentInput(BaseModel):
    total_spent: int

# Input cho Câu 15
class UserInput(BaseModel):
    id: int
    name: str
    is_active: bool
