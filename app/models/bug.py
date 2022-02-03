from app.schemas import BugType
from enum import Enum
from app.db.base import Base
from sqlalchemy import Column, String, Integer, Float


class Bug(Base):
    __tablename__ = "bugs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    classification = Column(String, nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    primary_type = Column(Enum(BugType), nullable=False)
    secondary_type = Column(nullable=True)
    primary_ability = Column(String, nullable=True)
    primary_ability_desc = Column(String, nullable=True)
    male_ratio = Column(Float, nullable=False)
    female_ratio = Column(Float, nullable=False)
    region_of_origin = Column(String, nullable=False)
