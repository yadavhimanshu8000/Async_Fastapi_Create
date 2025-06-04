from fastapi import APIRouter,Depends,Request
from service.schemas import Usercreate
from database.db import get_db
from service.controller import *
from service.controller import Createuser
from fastapi import FastAPI, HTTPException
from typing import List


router = APIRouter(prefix="/v1/user")


@router.post("/usercreate/")
async def create_user_api(user: Usercreate , db: AsyncSession = Depends(get_db)):
    await Createuser(user,db)
    return {"message": "User created successfully"}


@router.get("/getuser/{user_id}",response_model=Usercreate)
async def get_user_api(user_id: int, db: AsyncSession = Depends(get_db)):
    store = await Getuser(db, user_id)
    return store

@router.get("/getuserall/",response_model=List[Usercreate])
async def get_user_all_api(db: AsyncSession = Depends(get_db)):
    store = await Getallusers(db)
    return store
    
    

# @router.put('/updateuser/',response_model=Usercreate)
# async def update_user_api(user_id: int,user: Usercreate, db: AsyncSession = Depends(get_db)):
#     await Updateuser(user,user_id,db)
#     return{"message": "User Updated Successfully"}


@router.put('/updateuser/{user_id}', response_model=Usercreate)
async def update_user_api(user_id: int, user: Usercreate, db: AsyncSession = Depends(get_db)):
    updated_user = await Updateuser(db, user_id, user)
    return updated_user

@router.delete('/delete/{user_id}',response_model=Usercreate)
async def delete_user_api(user_id: int, db: AsyncSession = Depends(get_db)):
    delete_user = await Deleteuser(db,user_id)
    return delete_user
    
    
   


    
    
    

    






