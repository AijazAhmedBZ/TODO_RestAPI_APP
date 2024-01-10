from sqlalchemy.orm import Session
from models import Todo

def create_todo(db: Session, title: str, description: str, owner_id: int):
    db_todo = Todo(title=title, description=description, owner_id=owner_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
