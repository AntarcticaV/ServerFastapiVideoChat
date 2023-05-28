from fastapi import UploadFile, WebSocket, WebSocketDisconnect
from core.prisma import prismaBD
from prisma.models import Image
# import aiofiles
from app.models.model_user import UserAuth, UserOut, UserPutImage, UserPutNickname, UserPutPassword, UserReg
from app.repasitories.base_user_repasitories import BaseUserRepasitories


class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        await websocket.close()
        self.active_connections.remove(websocket)

    async def broadcast_video(self, video_frame: bytes, sender: WebSocket):
        for connection in self.active_connections:
            if connection != sender:
                await connection.send_bytes(video_frame)


class UserTemRepasitories(BaseUserRepasitories):
    manager = ConnectionManager()
    manager_audio = ConnectionManager()

    # проверка уникальных полей пользователя и запись его в базу данных
    async def registration_user(self, user_reg: UserReg) -> UserOut:
        status: bool = False
        user_out = await prismaBD.user.find_first(where={'nickname': user_reg.nickname})
        if user_out != None:
            status = False
        else:
            user_out = await prismaBD.user.create(data={'name': user_reg.name, 'surname': user_reg.surname,
                                                        'email': user_reg.email, 'nickname': user_reg.nickname,
                                                        'password': user_reg.password, 'id_image': 1})
            status = True
        return await UserOut.convert(user_out, status)

    # запрос в базу данных с помощью prisma
    async def authenticate_user(self, user_auth: UserAuth) -> UserOut:
        user_auth_out = await prismaBD.user.find_first(
            where={'nickname': user_auth.nickname, 'password': user_auth.password})
        return await UserOut.convert(user_auth_out, True)

    # проверка уникальности псевдонима и внесения изменене в базу данных
    async def chench_nickname(self, user_chanch_nick: UserPutNickname) -> UserOut:
        status: bool
        user_out = await prismaBD.user.find_first(where={'nickname': user_chanch_nick.new_nickname})
        if user_out != None:
            status = False
        else:
            user_out = await prismaBD.user.update(where={'nickname': user_chanch_nick.nickname}, data={'nickname': user_chanch_nick.new_nickname})
            status = True
        return await UserOut.convert(user_out, status)

    # поиск пользователя по псевдониму и изменение его пороля
    async def chench_password(self, user_chench_password: UserPutPassword) -> UserOut:
        status: bool = True
        user_out = await prismaBD.user.update(where={'nickname': user_chench_password.nickname}, data={'password': user_chench_password.new_password})
        return await UserOut.convert(user_out, status)

    # подключение пользователя по websocket и предача на сервер кадра видео и отправка другим подключённым пользователям этого кадра
    async def websocket_video(self, websocket: WebSocket):
        await self.manager.connect(websocket)
        try:
            while True:
                data = await websocket.receive_text()
                await self.manager.broadcast_video(data, websocket)
        except WebSocketDisconnect:
            self.manager.disconnect(websocket)

    # подключение пользователя по websocket и предача на сервер фрагмента аудио потока и отправка другим подключённым пользователям этого фрагмента
    async def websocket_audio(self, websocket: WebSocket):
        print(self.manager_audio.active_connections)
        await self.manager_audio.connect(websocket)
        try:
            while True:
                data = await websocket.receive_bytes()
                for connection in self.manager_audio.active_connections:
                    if connection != websocket:
                        await connection.send_bytes(data)
        except :
            await self.manager_audio.disconnect(websocket)
            print(self.manager_audio.active_connections)
        
        if (WebSocketDisconnect):
            await self.manager_audio.disconnect(websocket)

    async def broadcast(self, data: bytes, sender: WebSocket):
        for client in self.connected_clients:
            if client != sender:
                await client.send_bytes(data)
