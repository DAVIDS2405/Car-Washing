from fastapi import Request, status
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)


def add_slowapi_middleware(app):
    app.state.limiter = limiter
    app.add_middleware(SlowAPIMiddleware)


async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    time = exc.limit.limit.get_expiry() / 60
    return JSONResponse(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={
            "detail": f"Realizaste muchas peticiones intentalo dentro de {time:.0f} minuto"
        },
    )
