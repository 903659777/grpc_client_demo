# -*- coding = utf-8 -*-
# @Time :2024/10/25 15:13
from datetime import datetime

from pydantic import BaseModel


class ArticleModel(BaseModel):
    name: str
    content: str
    create_time: datetime
