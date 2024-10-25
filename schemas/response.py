# -*- coding = utf-8 -*-
# @Time :2024/10/25 15:13
from datetime import datetime
from typing import List

from schemas.ResponseSchema import ResponseSchema
from pydantic import BaseModel

class ArticleModel(BaseModel):
    id: int
    name: str
    content: str
    create_time: datetime

ArticleListResponse = ResponseSchema[List[ArticleModel]]
ArticleResponse = ResponseSchema[ArticleModel]