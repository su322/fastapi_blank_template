from fastapi import FastAPI
from app.api.v1 import router as api_v1_router

# 创建 FastAPI 应用
app = FastAPI(
    title="FastAPI Project",
    version="0.1.0"
)

# 基本路由
@app.get("/")
async def root():
    return {"message": "Hello World"}

# 注册 API 路由
app.include_router(api_v1_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
