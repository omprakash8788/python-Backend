from pydantic import BaseModel
from typing import Optional

class TaskV2(BaseModel):
    title:str
    description:str
    status:str
    priority:str | None ="lower"
class TaskV2WithID(TaskV2):
    id:int

class Task(BaseModel):
    title:str
    description:str
    status:str
class TaskWithID(Task):
    id:int

class UpdateTask(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None