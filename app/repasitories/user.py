from core.prisma import prismaBD

from app.models.model_user import UserAuth, UserOut, UserReg
from app.repasitories.base_user_repasitories import BaseUserRepasitories


class UserTemRepasitories(BaseUserRepasitories):

    async def registration_user(self, user_reg: UserReg):
        await prismaBD.user.create(date={'name': user_reg.name, 'surname': user_reg.surname,
                                         'email': user_reg.email, 'nickname': user_reg.nickname,
                                         'password': user_reg.password, 'id_image': 1})

    async def authenticate_user(self, user_auth: UserAuth) -> UserOut:

        return await UserOut().user_auth
