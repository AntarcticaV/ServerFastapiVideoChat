from app.models.model_user import UserReg, UserOut, UserAuth


class BaseUserRepasitories:

    async def registration_user(self, user_reg: UserReg):
        raise NotImplementedError

    async def authenticate_user(self, user_auth: UserAuth) -> UserOut:
        raise NotImplementedError
