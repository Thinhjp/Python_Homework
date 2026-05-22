# main.py (Entry Point): Nơi khởi chạy ứng dụng. 
# Nó khởi tạo FastAPI app và dùng app.include_router(router) để gắn các API từ nơi khác vào. 
# Nhiệm vụ của nó rất mỏng, chỉ để "cắm điện" cho hệ thống chạy.
from fastapi import FastAPI
from api.endpoints import router

app = FastAPI(title="50 Bài Tập Python Backend - Logic Nghiệp Vụ")

# Gắn các route từ file endpoints vào app chính
app.include_router(router)