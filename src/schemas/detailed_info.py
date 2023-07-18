from pydantic import BaseModel
from pydantic.types import List

from src.schemas.owners import Owners
from src.schemas.physical import Physical


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]
