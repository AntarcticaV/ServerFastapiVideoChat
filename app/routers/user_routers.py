from fastapi import APIRouter, Depends, UploadFile, WebSocket
from app.dependencies import get_user_repo
from app.models.model_user import UserAuth, UserOut, UserReg, UserPutNickname, UserPutPassword, UserPutImage
from app.repasitories.base_user_repasitories import BaseUserRepasitories

router = APIRouter()

# позволяет зарегистрироваться новому пользователю


@router.post("/registration_user", response_model=UserOut)
async def registration_user(user: UserReg, user_repo: BaseUserRepasitories = Depends(get_user_repo)):
    return await user_repo.registration_user(user)


# позволяет пользователю авторизоваться
@router.post("/authenticate_user", response_model=UserOut)
async def authenticate_user(user: UserAuth, user_repo: BaseUserRepasitories = Depends(get_user_repo)):
    return await user_repo.authenticate_user(user)

# позволяет изменять псевдоним


@router.post("/chench_nickname", response_model=UserOut)
async def chench_nickname(user: UserPutNickname, user_repo: BaseUserRepasitories = Depends(get_user_repo)):
    return await user_repo.chench_nickname(user)

# позволяет изменить пароль


@router.post("/chench_password", response_model=UserOut)
async def chench_password(user: UserPutPassword, user_repo: BaseUserRepasitories = Depends(get_user_repo)):
    return await user_repo.chench_password(user)

# создает подключение между пользователями для передачи видео кадров


@router.websocket("/ws_video")
async def websocket_video(websocket: WebSocket, ws_repo: BaseUserRepasitories = Depends(get_user_repo)):
    await ws_repo.websocket_video(websocket)

# создает подключение между пользователями для передачи звука


@router.websocket("/ws_audio")
async def websocket_audio(websocket: WebSocket, ws_repo: BaseUserRepasitories = Depends(get_user_repo)):
    await ws_repo.websocket_audio(websocket)
