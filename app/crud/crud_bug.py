from .crud_base import CRUDBase
from app.models import Bug
from app.schemas import BugCreate, BugUpdate

bug = CRUDBase[Bug, BugCreate, BugUpdate](Bug)