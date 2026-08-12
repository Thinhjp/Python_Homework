# Chuyển từ Code Thường sang API trong Python

Dự án này minh họa cách chuyển một ứng dụng Python xử lý nghiệp vụ theo kiểu hàm thuần sang dạng API bằng FastAPI. Mục tiêu không chỉ là "biến code thành endpoint", mà là tách rõ trách nhiệm theo kiến trúc:

- `api/`: nơi nhận request HTTP, validate dữ liệu và trả response
- `core/`: nơi chứa logic nghiệp vụ
- `main.py`: nơi khởi tạo ứng dụng và gắn router

---

## 1. Vấn đề cần giải quyết

Khi viết code theo kiểu thường, ta thường làm như sau:

```python
products = [
    {"id": 1, "name": "Laptop", "stock": 5, "is_active": True},
    {"id": 2, "name": "Mouse", "stock": 0, "is_active": True}
]

filtered = [p for p in products if p["stock"] > 0 and p["is_active"] is True]
print(filtered)
```

Đây là code chạy tốt trên console, nhưng có hạn chế:

- Không có giao diện để bên ngoài gọi
- Không thể dùng từ web/mobile app
- Không có kiểm tra dữ liệu đầu vào
- Không có chuẩn response JSON
- Khó tích hợp, deploy và bảo trì

Để mở rộng, ta cần biến logic thành API để hệ thống có thể giao tiếp qua HTTP.

---

## 2. Ý tưởng chuyển đổi

Ta giữ nguyên logic nghiệp vụ ở layer `core`, nhưng thêm một lớp `api` để nhận request và trả response.

### Cách tiếp cận

1. Viết logic nghiệp vụ ở dạng function Python thuần
2. Định nghĩa schema dữ liệu đầu vào bằng Pydantic
3. Tạo route trong `api/endpoints.py`
4. Gọi function nghiệp vụ từ `core`
5. Trả về JSON qua FastAPI

---

## 3. Kiến trúc trong repo

```text
Python_Homework/
├── main.py
├── README.md
├── requirements.txt
├── api/
│   ├── __init__.py
│   ├── endpoints.py
│   └── schemas.py
├── core/
│   ├── __init__.py
│   ├── easy_services.py
│   └── hard_services.py
```

### `main.py`

Nơi bắt đầu ứng dụng, khởi tạo FastAPI và gắn router:

```python
from fastapi import FastAPI
from api.endpoints import router

app = FastAPI(title="50 Bài Tập Python Backend - Logic Nghiệp Vụ")
app.include_router(router)
```

### `api/schemas.py`

Định nghĩa cấu trúc dữ liệu đầu vào để FastAPI tự validate:

```python
from pydantic import BaseModel

class ProductInput(BaseModel):
    id: int
    name: str
    stock: int
    is_active: bool
```

### `core/easy_services.py`

Chứa logic nghiệp vụ:

```python
def filter_available(products):
    return [p for p in products if p.get("stock", 0) > 0 and p.get("is_active") is True]
```

### `api/endpoints.py`

Nơi chuyển request HTTP thành gọi logic nghiệp vụ và trả JSON:

```python
@router.post("/api/products/available")
def api_filter_available(products: List[ProductInput]):
    products_dict = [p.dict() for p in products]
    filtered = filter_available(products_dict)
    return filtered
```

---

## 4. Ví dụ chuyển đổi từ code thường sang API

### Bước 1: Code thuần

```python
def filter_available(products):
    return [p for p in products if p["stock"] > 0 and p["is_active"] is True]
```

### Bước 2: Tạo schema validation

```python
class ProductInput(BaseModel):
    id: int
    name: str
    stock: int
    is_active: bool
```

### Bước 3: Tạo endpoint API

```python
@router.post("/api/products/available")
def api_filter_available(products: List[ProductInput]):
    products_dict = [p.dict() for p in products]
    filtered = filter_available(products_dict)
    return filtered
```

### Bước 4: Gửi request bằng JSON

```json
[
  {"id": 1, "name": "Laptop", "stock": 5, "is_active": true},
  {"id": 2, "name": "Mouse", "stock": 0, "is_active": true}
]
```

### Bước 5: Response trả về

```json
[
  {"id": 1, "name": "Laptop", "stock": 5, "is_active": true}
]
```

Như vậy, logic vẫn nguyên, nhưng giờ có thể được gọi từ web, app mobile hoặc hệ thống khác qua HTTP.

---

## 5. Vì sao nên tách layer như vậy?

### 1) Dễ bảo trì
Logic nghiệp vụ không bị lẫn với HTTP request và response.

### 2) Dễ test
Ta có thể test hàm trong `core` mà không cần khởi động server.

### 3) Dễ mở rộng
Có thể thêm nhiều API mới mà không làm hỏng logic cũ.

### 4) Dễ validate dữ liệu
Schema Pydantic giúp lọt dữ liệu sai trước khi vào business logic.

### 5) Dễ tích hợp
Frontend, mobile app hoặc service khác chỉ cần gọi API, không cần biết logic bên trong.

---

## 6. Các API đã triển khai trong repo

Repo hiện có các endpoint mẫu tương ứng với các bài tập nghiệp vụ:

- `POST /api/products/available` — lọc sản phẩm còn hàng
- `POST /api/cart/total` — tính tổng tiền giỏ hàng
- `POST /api/orders/message` — trả lời trạng thái đơn hàng
- `POST /api/customer/classify` — phân loại khách hàng
- `POST /api/admin/users/active` — lọc user đang hoạt động

---

## 7. Cách chạy project

Cài đặt dependency:

```bash
pip install -r requirements.txt
```

Khởi động server:

```bash
uvicorn main:app --reload
```

Mở Swagger UI:

```text
http://localhost:8000/docs
```

---

## 8. Kết luận

Việc chuyển từ code thường sang API không phải là thay đổi logic, mà là thay đổi cách tiếp cận: từ chạy trực tiếp trên console sang giao tiếp qua HTTP theo chuẩn hiện đại.

Với FastAPI, quy trình này rất rõ ràng:

- `Schema` kiểm soát dữ liệu đầu vào
- `Endpoint` nhận request
- `Core` xử lý nghiệp vụ
- `JSON` trả về cho client

Đây cũng là cách triển khai phổ biến trong backend thực tế, giúp code dễ phát triển, dễ bảo trì và dễ tích hợp với hệ thống khác.

---

## 9. Gợi ý mở rộng

Bạn có thể tiếp tục phát triển repo theo hướng:

- Thêm database và ORM
- Chuyển logic cũ thành service layer chuyên biệt
- Thêm authentication và authorization
- Tạo unit test cho core functions
- Tạo thêm API cho các bài tập còn lại

---

> Tư duy kiến trúc: Endpoint nhận lệnh -> Schema kiểm duyệt -> Core xử lý logic.
