from pydantic import BaseModel
from typing import Optional

class CourseCreate(BaseModel):

    name: str
    code: str
    credits: int
    department_id: int


class CourseResponse(CourseCreate):

    id: int

    class Config:
        from_attributes = True
        
class CourseUpdate(BaseModel):

    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None