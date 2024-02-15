from fastapi import FastAPI

from src.api.auth.controller import fastapi_users_routers

ROUTERS = []
AUTH_ROUTERS = fastapi_users_routers


app = FastAPI(title="example",
              version="1.0.0",
              )

for auth_router in AUTH_ROUTERS:
    app.include_router(auth_router,
                       prefix="/auth",
                       tags=["auth"],
                       )


for router in ROUTERS:
    app.include_router(router)
