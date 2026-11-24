from datetime import date
from enum import Enum

from pydantic import BaseModel, field_validator


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Status(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"


class Ticket(BaseModel):
    ticket_id: int
    customer_name: str
    priority: Priority
    status: Status
    created_date: date

    @field_validator("customer_name")
    @classmethod
    def name_not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("customer_name must not be blank")
        return v.strip()