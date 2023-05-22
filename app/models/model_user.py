from pydantic import BaseModel
from core.prisma import prismaBD
from prisma.models import User


class BaseUser(BaseModel):
    name: str
    email: str
    surname: str
    nickname: str


class UserAuth(BaseModel):
    nickname: str
    password: str


class UserReg(BaseUser):
    password: str


class UserPutPassword(BaseUser):
    password: str
    new_password: str


class UserOut(BaseUser):
    id_image: int
    status: bool

    @staticmethod
    async def convert(orig: User|None, stat:bool):
        # print(orig)
        ret = UserOut(
            name=orig.name,
            surname=orig.surname,
            email=orig.email,
            id_image=orig.id_image,
            nickname=orig.nickname,
            status=stat
        )
        return ret


class UserPutImage(BaseUser):
    new_image: str


class UserPutNickname(BaseUser):
    new_nickname: str
