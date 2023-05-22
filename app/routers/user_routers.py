from fastapi import APIRouter, Depends, UploadFile, WebSocket
from app.dependencies import get_user_repo
from app.models.model_user import UserAuth, UserOut, UserReg, UserPutNickname, UserPutPassword,UserPutImage
from app.repasitories.base_user_repasitories import BaseUserRepasitories

router = APIRouter()


@router.post("/registration_user", response_model=UserOut)
async def registration_user(user: UserReg, user_repo: BaseUserRepasitories = Depends(get_user_repo)):
    return await user_repo.registration_user(user)


@router.post("/authenticate_user", response_model=UserOut)
async def authenticate_user(user: UserAuth, user_repo: BaseUserRepasitories = Depends(get_user_repo)):
    return await user_repo.authenticate_user(user)

@router.put("/chench_nickname", response_model=UserOut)
async def chench_nickname(user: UserPutNickname, user_repo: BaseUserRepasitories =Depends(get_user_repo)):
    return await user_repo.chench_nickname(user)

@router.put("/chench_password", response_model=UserOut)
async def chench_password(user:UserPutPassword, user_repo:BaseUserRepasitories=Depends(get_user_repo)):
    return await user_repo.chench_password(user)

# @router.put("/chench_image", response_model=UserOut)
# async def chench_image(user:UserPutImage, user_repo:BaseUserRepasitories=Depends(get_user_repo)):
#     return await user_repo.chench_image(user)

# @router.post("/download_file", response_model=bool)
# async def download_file(file: UploadFile, user_repo:BaseUserRepasitories=Depends(get_user_repo)):
#     return user_repo.download_image(file)

@router.websocket("/ws_video")
async def websocket_video(websocket: WebSocket, ws_repo:BaseUserRepasitories=Depends(get_user_repo)):
    await ws_repo.websocket_video(websocket)