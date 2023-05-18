from fastapi import APIRouter, Depends
from app.dependencies import get_user_repo
from app.models.model_user import UserAuth, UserOut, UserReg
from app.repasitories.base_user_repasitories import BaseUserRepasitories

router = APIRouter()


@router.post("/registration_user")
async def registration_user(user: UserReg, user_repo: BaseUserRepasitories = Depends(get_user_repo)):
    await user_repo.registration_user(user)


@router.post("/authenticate_user", response_model=UserOut)
async def authenticate_user(user: UserAuth, user_repo: BaseUserRepasitories = Depends(get_user_repo)):
    return await user_repo.authenticate_user(user)
