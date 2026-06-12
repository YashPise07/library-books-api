from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    is_borrowed: bool = False

    class Config:
        from_attributes = True