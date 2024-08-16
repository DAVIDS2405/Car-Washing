from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from routers import customers
from utils.constans import routers
from config.middlewares.rate_limit import add_slowapi_middleware, limiter, rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
app = FastAPI(
    title="Lavadora de autos api",
    description="Api para el control de una lavadora de autos",
    version="0.1",
    docs_url="/api/v1/docs",
    openapi_url="/api/v1/openapi.json",
    redoc_url=None,
)

add_slowapi_middleware(app)
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)
app.include_router(customers.router, prefix=routers.PREFIX)


@app.get("/", include_in_schema=False)
async def read_root():
    return RedirectResponse(url="/api/v1/docs")


@app.get("/health")
@limiter.limit('5/minute')
async def read_check_healt(request: Request):
    return "Ok"
