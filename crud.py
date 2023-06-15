from sqlalchemy.orm import Session
from models import Post
from schemas import PostSchema


def get_posts(db: Session, skip: int = 0):
    return db.query(Post).offset(skip).all()

def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def remove_post(db: Session, post_id: int):
    _post = get_post_by_id(db=db, post_id=post_id)
    db.delete(_post)
    db.commit()


    db.commit()
    db.refresh(_post)
    return _post