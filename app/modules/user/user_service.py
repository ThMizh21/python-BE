import json
from typing import List
from app.modules.user.user_model import User

json_file = 'app/data/user/user.json'

def load_users() -> List[User]:
    with open(json_file, "r") as file:
        user_data = json.load(file)
    return [User(**user) for user in user_data]

def save_users(users: List[User]) -> None:
    with open(json_file, 'w') as file:
        json.dump([user.dict() for user in users], file, indent=4)

def create_user(user: User):
    users = load_users()
    user.user_id = max([u.user_id for u in users], default=0) + 1
    users.append(user)
    save_users(users) 
    return {"status": 200, "message": "User created successfully"}

def update_user_by_id(user_id: int, user_data: User):
    users = load_users()
    for i, user in enumerate(users):
        if user.user_id == user_id:
            users[i] = user_data  
            save_users(users)  
            return {"status": 200, "message": "User updated successfully"}
    return {"status": 404, "message": "User not found"}

def delete_user(user_id: int):
    users = load_users()
    for i, user in enumerate(users):
        if user.user_id == user_id:
            del users[i]
            save_users(users) 
            return {"status": 200, "message": "User deleted successfully"}
    return {"status": 404, "message": "User not found"}
