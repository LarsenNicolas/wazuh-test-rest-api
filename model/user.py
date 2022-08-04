from pydantic import BaseModel

from model.address import Address
from model.company import Company

class User(BaseModel):
    """User model."""
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company
