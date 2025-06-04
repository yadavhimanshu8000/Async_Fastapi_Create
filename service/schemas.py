from pydantic import BaseModel ,EmailStr ,constr


class Usercreate(BaseModel):
    User_name: constr()
    Mobile: constr(min_length=10, max_length=15)
    Email : EmailStr
   
    class Config:
        from_attributes=True
    
    
    