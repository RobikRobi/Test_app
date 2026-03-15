from pydantic import BaseModel, Field
from uuid import uuid4, UUID

class User(BaseModel):
    id: int
    name: str
    age: int