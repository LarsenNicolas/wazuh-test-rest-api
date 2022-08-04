from pydantic import BaseModel

class Company(BaseModel):
    """Company model."""
    name: str
    catchPhrase: int
    bs: str
