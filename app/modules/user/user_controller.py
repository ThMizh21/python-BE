from fastapi import APIRouter
from app.modules.user.user_model import User
from app.modules.user.user_service import load_users ,create_user , update_user_by_id, delete_user


router = APIRouter()

@router.get("/v1/users/")
def get_all_users():
    return load_users()

@router.post("/v1/users/")  
def create_new_user(user : User): 
     return create_user(user)
 
@router.put("/v1/users/{user_id}")
def update_user_info(user_id : int):
    return update_user_by_id()

@router.delete("/v1/users/{user_id}")
def delete_user_info(user_id: int):
    return delete_user()