# -*- coding = utf-8 -*-
# @Time :2024/10/25 14:44
from fastapi import APIRouter

from services.article import ArticleServiceClient
from schemas.request import ArticleModel
from schemas.response import ArticleResponse, ArticleListResponse

router = APIRouter(prefix="/api", tags=["article"])
# 实例化发送gRPC请求类
article_service_client = ArticleServiceClient()


@router.get("/articles", response_model=ArticleListResponse)
async def get_articles(page: int = 1, size: int = 10):
    articles = await article_service_client.get_article_list(page=page, size=size)
    return {"code": 200, "msg": "数据获取成功", "data": articles}


@router.get("/article/{article_id}", response_model=ArticleResponse)
async def get_article(article_id: int):
    article = await article_service_client.get_article_detail(article_id)
    return {"code": 200, "msg": "数据获取成功", "data": article}


@router.post("/article", response_model=ArticleResponse)
async def create_article(data: ArticleModel):
    name = data.name
    content = data.content
    create_time = str(data.create_time)
    article = await article_service_client.create_article(name=name, content=content, create_time=create_time)
    return {"code": 200, "msg": "数据添加成功", "data": article}


@router.put("/article/{article_id}", response_model=ArticleResponse)
async def update_article(article_id: int, data: ArticleModel):
    name = data.name
    content = data.content
    create_time = str(data.create_time)
    await article_service_client.update_article(article_id=article_id, name=name, content=content,
                                                create_time=create_time)
    return {"code": 200, "msg": "更新成功"}


@router.delete("/article/{article_id}", response_model=ArticleResponse)
async def delete_article(article_id: int):
    await article_service_client.delete_article(article_id=article_id)
    return {"code": 200, "msg": "删除成功"}
