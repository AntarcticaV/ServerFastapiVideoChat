from core.prisma import prismaBD

from app.models.model_user import UserAuth, UserOut, UserReg
from app.repasitories.base_user_repasitories import BaseUserRepasitories


class UserTemRepasitories(BaseUserRepasitories):

    async def registration_user(self, user_reg: UserReg):
        await prismaBD.user.create(data={'name': user_reg.name, 'surname': user_reg.surname,
                                         'email': user_reg.email, 'nickname': user_reg.nickname,
                                         'password': user_reg.password, 'id_image': 1})

    async def authenticate_user(self, user_auth: UserAuth) -> UserOut:
        user_auth_out = prismaBD.user.find_first(
            where={'nickname': user_auth.nickname, 'password': user_auth.password})
        print(user_auth_out)
        return await UserOut.convert(user_auth_out)
