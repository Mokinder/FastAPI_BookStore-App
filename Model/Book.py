from pydantic import BaseModel
from typing  import Optional,Literal
from uuid import uuid4


class Book(BaseModel):
    book_id : Optional[int] = uuid4().int
    name: str
    price : float
    author : str
    genre : Literal["Fiction","Non-Fiction","Culture"]


