from fastapi_users import FastAPIUsers

from api.auth.auth import auth_backend
from api.auth.db import User
from api.auth.manager import get_user_manager
from api.auth.schemas import UserRead, UserCreate

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


fastapi_users_routers = [
    fastapi_users.get_auth_router(auth_backend),
    fastapi_users.get_register_router(UserRead, UserCreate),
    ]
