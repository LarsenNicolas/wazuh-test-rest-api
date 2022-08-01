from pydantic import BaseModel;

class Task(BaseModel):
    user_id: int;
    id: int;
    title: str;
    completed: bool;
