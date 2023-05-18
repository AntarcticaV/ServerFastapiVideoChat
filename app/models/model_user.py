from pydantic import BaseModel
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
    image: str
    
    @staticmethod
    async def convert()


class UserPutImage(BaseUser):
    new_image: str


class UserPutNickname(BaseUser):
    new_nickname: str
