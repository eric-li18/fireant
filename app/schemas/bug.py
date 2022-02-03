from .types import BugType
from typing import Optional
from pydantic import BaseModel


class BugBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    classification: Optional[str]
    height: Optional[float]
    weight: Optional[float]
    primary_type: Optional[BugType]
    secondary_type: Optional[BugType]
    primary_ability: Optional[str]
    primary_ability_desc: Optional[str]
    male_ratio: Optional[float]
    female_ratio: Optional[float]
    region_of_origin: Optional[str]


# Read-only application
class BugCreate(BugBase):
    pass


# Read-only application
class BugUpdate(BugBase):
    pass


# Properties to return to client
class Bug(BugBase):
    id: int
    name: str
    classification: str
    height: float
    weight: float
    primary_type: BugType
    primary_ability: str
    primary_ability_desc: str
    male_ratio: float
    female_ratio: float
    region_of_origin: str

    # Tells the Pydantic model to read data in dict and ORM model:
    #
    # We can access id by:
    # id = data.id
    #     or
    # id = data["id"]
    class Config:
        orm_mode = True
