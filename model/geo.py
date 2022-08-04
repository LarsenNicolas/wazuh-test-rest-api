from pydantic import BaseModel

class Geo(BaseModel):
    """Geo model."""
    lat: str
    lng: str
