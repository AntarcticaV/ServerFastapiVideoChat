from fastapi import FastAPI
import uvicorn
from core.prisma import prismaBD
from core import setting
from app.routers import routers

app = FastAPI(title="Learn FastAPI")


@app.on_event("startup")
async def startup():
    await prismaBD.connect()
    routers(app)


@app.on_event("shutdown")
async def shutdown():
    await prismaBD.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=setting.POST, host=setting.HOST, reload=True)
