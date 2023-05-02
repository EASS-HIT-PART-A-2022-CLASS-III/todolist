from pydantic import BaseModel
import datetime
from enum import Enum

class Status(str,Enum):
    complete = "complete"
    in_progress = "in progress"
    
    

class Todo(BaseModel):
    title: str
    description: str