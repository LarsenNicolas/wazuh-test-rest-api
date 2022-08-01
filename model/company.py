from pydantic import BaseModel;

class Company(BaseModel):
    name: str;
    catchPhrase: int;
    bs: str;
