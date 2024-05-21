from typing import List

from fastapi import FastAPI, Depends

from routes import routes_list

app = FastAPI(
    title="Blog API",
    description="",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)
for route in routes_list:
    app.include_router(route)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
