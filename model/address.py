from pydantic import BaseModel
from model.company import Company
from model.geo import Geo

class Address(BaseModel):
    """Address model."""
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo
    phone: str
    website: str
    company: Company