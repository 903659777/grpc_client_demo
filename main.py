import uvicorn
from fastapi import FastAPI
from routers import article
from hooks.lifespan import lifespan

from settings import settings

app = FastAPI(lifespan=lifespan)
app.include_router(article.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/health")
async def health():
    return "ok"


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=settings.SERVER_PORT)