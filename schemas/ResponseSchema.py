# -*- coding = utf-8 -*-
# @Time :2024/10/18 09:28
from pydantic import BaseModel
from typing import Optional, Generic, TypeVar

T = TypeVar('T')


class ResponseSchema(BaseModel, Generic[T]):
    """ 基础模型 """
    code: int
    msg: str
    data: Optional[T] = None

    class Config:
        arbitrary_types_allowed = True
