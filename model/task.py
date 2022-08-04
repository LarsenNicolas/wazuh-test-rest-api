from pydantic import BaseModel

class Task(BaseModel):
    """Task model."""
    user_id: int
    id: int
    title: str
    completed: bool
