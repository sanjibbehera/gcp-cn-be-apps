from sqlalchemy.orm import Session
import customer.models as models
import customer.schemas as schemas
from utility.hashing import Hash
from fastapi import HTTPException, status

def get_all(db: Session):
    users = db.query(models.User).all()
    return users


def create(request, db: Session):
    new_user = models.User(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        user_name=request.user_name,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




def show(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        return {"detail": f"user with id {id} not found"}
    return {"user": user}


def destroy(id, response, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        response.status_code = 404
        return {"detail": f"user with id {id} not found"}
    else:
        try:
            # Soft delete by setting isDeleted to True
            user.isDeleted = True
            db.commit()
            response.status_code = 200
            return {'msg': 'deleted'}
        except Exception as e:
            response.status_code = status.HTTP_406_NOT_ACCEPTABLE
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=str(e))


def update(id, response, request: schemas, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        response.status_code = 404
        return {"detail": f"user with id {id} not found"}
    else:
        db.query(models.User).filter(models.User.id == id).update({
            'first_name': request.first_name,
            'last_name': request.last_name,
            'email': request.email,
            'user_name': request.user_name,
            'password': Hash.bcrypt(request.password)
        })
        db.commit()
        return {'msg': 'updated'}
