from fastapi import APIRouter, Request
from config.middlewares.rate_limit import limiter


router = APIRouter(
    tags=["Customers"],
)


@router.post("/new_customer")
@limiter.limit('100/minute')
async def new_customer(request: Request):
    return "add new"


@router.get("/shearch_customer")
@limiter.limit('100/minute')
async def shearch_customer(request: Request):
    return "add new"


@router.put("/update_customer")
@limiter.limit('100/minute')
async def update_customer(request: Request):
    return "add new"


@router.delete("/delete_customer")
@limiter.limit('100/minute')
async def delete_customer(request: Request):
    return "delete customer"
