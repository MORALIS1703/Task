from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import PostSchema, Request, Response, RequestPost
import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/get")
async def get_posts(text: int = 0, db: Session = Depends(get_db)):
    _posts = crud.get_posts(db, text)
    return Response(status="Ok", code="200", message="Success", result=_posts)

@router.delete("/delete")
async def delete_posts(delete_id: RequestPost,  db: Session = Depends(get_db)):
    crud.remove_post(db, post_id=delete_id.parameter.id)
    return Response(status="Ok", code="200", message="Success").dict(exclude_none=True)
