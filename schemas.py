from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, examples=["Python Basics"])
    author: str = Field(..., min_length=1, examples=["Shreyash"])
    is_borrowed: bool = False

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "title": "Python Basics",
                "author": "Shreyash",
                "is_borrowed": False
            }
        }
    }