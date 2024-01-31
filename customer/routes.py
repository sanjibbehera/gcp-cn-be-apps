from fastapi import APIRouter,Depends,status,Response
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate
from config import database
import customer.schemas as schemas
from sqlalchemy.orm import Session
import customer.dao as dao
from typing import List

router=APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/list/", response_model=List[schemas.ShowUser])
def all_users(db: Session = Depends(database.get_db)):    
    return dao.get_all(db)

@router.post("/create/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(database.get_db)) :
   return dao.create(request,db)

@router.get("/view/{id}")
def show_user(id:int, db:Session=Depends(database.get_db)) :   
    return dao.show(id,db)    

@router.put("/update/{id}",status_code=202)
def update(id,response: Response,request: schemas.User, db : Session= Depends(database.get_db)):
    return dao.update(id,response,request,db)

@router.delete("/delete/{id}",status_code=204)
def destory(id,response: Response,db : Session= Depends(database.get_db)):
    return dao.destroy(id,response,db)