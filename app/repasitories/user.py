from fastapi import UploadFile
from core.prisma import prismaBD
from prisma.models import Image
# import aiofiles
from app.models.model_user import UserAuth, UserOut, UserPutImage, UserPutNickname, UserPutPassword, UserReg
from app.repasitories.base_user_repasitories import BaseUserRepasitories


class UserTemRepasitories(BaseUserRepasitories):

    async def registration_user(self, user_reg: UserReg) -> UserOut:
        status:bool
        user_out = await prismaBD.user.find_first(where={'nickname':user_reg.nickname})
        if user_out != None:
            status = False
        else:
            user_out = await prismaBD.user.create(data={'name': user_reg.name, 'surname': user_reg.surname,
                                         'email': user_reg.email, 'nickname': user_reg.nickname,
                                         'password': user_reg.password, 'id_image': 1})
            status = True
        return await UserOut.convert(user_out,status)


    async def authenticate_user(self, user_auth: UserAuth) -> UserOut:
        user_auth_out = await prismaBD.user.find_first(
            where={'nickname':user_auth.nickname, 'password':user_auth.password})
        return await UserOut.convert(user_auth_out, True)
    
    async def chench_nickname(self, user_chanch_nick: UserPutNickname) -> UserOut:
        status:bool
        user_out = await prismaBD.user.find_first( where={'nickname':user_chanch_nick.new_nickname})
        if user_out != None:
            status=False
        else:
            user_out = await prismaBD.user.update(where={'nickname':user_chanch_nick.nickname}, data={'nickname':user_chanch_nick.new_nickname})
            status = True
            pass
        return await UserOut.convert(user_out,status)
    
    async def chench_password(self, user_chench_password: UserPutPassword) -> UserOut:
        status:bool = True
        user_out = await prismaBD.user.update(where={'nickname':user_chench_password.nickname}, data={'password':user_chench_password.new_password})
        return await UserOut.convert(user_out,status)
    
    # async def chench_image(self, user_chench_image: UserPutImage) -> UserOut:
    #     status:bool = True
    #     image:Image = await prismaBD.image.fain_first(where={'name': user_chench_image.new_image})
    #     user_out = await prismaBD.user.update(where={'nickname':user_chench_image.nickname}, data={'id_image':image.id})
        
    # async def download_image(swlf, file: UploadFile) -> bool:
    #     status:bool
    #     try:
    #         async with aiofiles.open("Image/"+file.filename, mode='wb')as file_save:
    #             contex = await file.read()
    #             await file_save.write(contex)
    #         await prismaBD.image.create(data={'name':file.filename})
    #         status = True
    #     except:
    #         status = False
    #     return status