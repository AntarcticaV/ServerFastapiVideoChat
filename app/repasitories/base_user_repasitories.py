from app.models.model_user import UserReg, UserOut, UserAuth, UserPutNickname, UserPutPassword,UserPutImage
from fastapi import UploadFile, WebSocket


class BaseUserRepasitories:

    async def registration_user(self, user_reg: UserReg)-> UserOut:
        raise NotImplementedError

    async def authenticate_user(self, user_auth: UserAuth) -> UserOut:
        raise NotImplementedError
    
    async def chench_nickname(self, user_chench_nick: UserPutNickname)->UserOut:
        raise NotImplementedError
    
    async def chench_password(self, user_chench_password:UserPutPassword)->UserOut:
        raise NotImplementedError
    
    async def chench_image(self, user_chench_image:UserPutImage)->UserOut:
        raise NotImplementedError
    
    async def download_image(self,file:UploadFile)->bool:
        raise NotImplementedError
    
    async def websocket_video(self, websocket: WebSocket):
        raise NotImplementedError
    
    async def websocket_audio(self, websocket:WebSocket):
        raise NotImplementedError
