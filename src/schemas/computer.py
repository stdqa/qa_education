from pydantic import BaseModel
from pydantic.types import PastDate, FutureDate
from pydantic.networks import IPv4Address, IPv6Address


from src.schemas.detailed_info import DetailedInfo
from src.enums.user_enums import Statuses
from example import computer


class Computer(BaseModel):
    id: int
    status: Statuses
    started_at: PastDate
    exparation_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo


comp = Computer.model_validate(computer)
print(comp.model_json_schema)
