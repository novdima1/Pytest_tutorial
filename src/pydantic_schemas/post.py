from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int = Field(le=2)
    title: str
    # name: str = Field(alias="_name")

    # @validator("id")
    # def check_id(cls, v):
    #     if v > 100:
    #         raise ValueError("Id should be less than 2")
    #     else:
    #         return v
