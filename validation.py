# from pydantic import BaseModel, field_validator

# class User(BaseModel):
#     name: str
#     password: str
#     age: int

#     @field_validator('password')
#     def password_must_be_strong(cls, value):
#         if len(value) < 8:
#             raise ValueError('Password must be at least 8 characters long.')
#         print(value)
#         return value
    
#     @field_validator('name')
#     def name_should_not_be_short(cls, value):
#         if len(value) < 3:
#             raise ValueError('username should not be less then 3 ')
#         print(value)
#         return value
    
    
            
# User(name = "tamil",password = "123456789" ,age = 23)




from datetime import datetime

from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    id: int  
    name: str = 'John Doe'  
    signup_ts: datetime | None  
    tastes: dict[str, PositiveInt]  


external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',  
    'tastes': {
        'wine': 9,
        b'cheese': 7,  
        'cabbage': '1',  
    },
}

user = User(**external_data)  

print(user.id)  
#> 123
print(user.model_dump())  
