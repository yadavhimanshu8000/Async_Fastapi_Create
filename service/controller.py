from service.models import User
from service.schemas import Usercreate
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, HTTPException
from sqlalchemy.future import select

async def Createuser(user: Usercreate, db: AsyncSession):
    new_user = User(
        User_name = user.User_name,
        Mobile = user.Mobile,
        Email = user.Email,   
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user




async def Getuser(db: AsyncSession, user_id : int):
    result=  await db.execute(select(User).where(User.User_id == user_id))
    user = result.scalar_one_or_none()
    
    if user is None:
        raise HTTPException(status_code=404, detail='User Not Found')
    return user




async def Getallusers(db: AsyncSession):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users





async def Updateuser(db: AsyncSession, user_id: int,user: Usercreate):
    result = await db.execute(select(User).where(User.User_id == user_id))
    db_user = result.scalar_one_or_none()
    
    db_user.User_name = user.User_name
    db_user.Mobile = user.Mobile
    db_user.Email =user.Email
   
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user




async def Deleteuser(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.User_id == user_id))
    db_user = result.scalar_one_or_none()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User Not Found')
    await db.delete(db_user)
    await db.commit()
    # await db.refresh(db_user)
    return db_user


# async def create_user(user: Usercreate, db: AsyncSession):
#     user_details = insert(User).values(
#         User_name=user.User_name,
#         Mobile=user.Mobile,
#         Email=user.Email
#     )
#     await db.execute(user_details)
#     await db.commit()  
    

