from fastapi_users import FastAPIUsers

from src.api.auth.auth import auth_backend
from src.api.auth.db import User
from src.api.auth.manager import get_user_manager
from src.api.auth.schemas import UserRead, UserCreate

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


fastapi_users_routers = [
    fastapi_users.get_auth_router(auth_backend),
    fastapi_users.get_register_router(UserRead, UserCreate),
    ]
