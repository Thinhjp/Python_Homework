from fastapi import FastAPI
from api.endpoints import router

app = FastAPI(title="50 Bài Tập Python Backend - Logic Nghiệp Vụ")

# Gắn các route từ file endpoints vào app chính
app.include_router(router)