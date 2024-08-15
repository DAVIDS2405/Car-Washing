from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI(
    title="Lavadora de autos api",
    description="Api para el control de una lavadora de autos",
    version="0.1",
    docs_url="/api/v1/docs",
    openapi_url="/api/v1/openapi.json",
    redoc_url=None
)


@app.get("/", include_in_schema=False)
async def read_root():
    return RedirectResponse(url="/api/v1/docs")
