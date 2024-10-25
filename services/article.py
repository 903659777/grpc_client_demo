# -*- coding = utf-8 -*-
# @Time :2024/10/25 14:46
import grpc
from services.protos import article_pb2, article_pb2_grpc
from utils.single import SingletonMeta
from services.decorators import grpc_error_handler


class ArticleStub:
    """ 创建一个异步上下文管理器，创建gRPC服务的连接通道 """

    def __init__(self):
        self.article_service_addr = "127.0.0.1:5000"

    async def __aenter__(self):
        self.channel = grpc.aio.insecure_channel(self.article_service_addr)
        stub = article_pb2_grpc.ArticleServiceStub(self.channel)
        return stub

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.channel.close()


class ArticleServiceClient(metaclass=SingletonMeta):
    """ 发送gRPC请求的方法，在调用这些方法的时候就会想服务端发送请求 """

    @grpc_error_handler
    async def get_article_list(self, page, size):
        """ 获取文章列表 """
        async with ArticleStub() as stub:
            request = article_pb2.ArticleListRequest()
            request.page = page
            request.page_size = size
            response = await stub.ArticleList(request)
        return response.articles

    @grpc_error_handler
    async def get_article_detail(self, article_id):
        """ 获取单个文章 """
        async with ArticleStub() as stub:
            request = article_pb2.ArticleDetailRequest()
            request.pk = article_id
            response = await stub.ArticleDetail(request)
        return response.article

    @grpc_error_handler
    async def create_article(self, name, content, create_time):
        """ 添加一个文章 """
        async with ArticleStub() as stub:
            request = article_pb2.CreateArticleRequest(name=name, content=content, create_time=create_time)
            response = await stub.CreateArticle(request)
        return response.article

    @grpc_error_handler
    async def update_article(self, article_id, name, content, create_time):
        """ 更新文章 """
        async with ArticleStub() as stub:
            request = article_pb2.UpdateArticleRequest(id=article_id, name=name, content=content,
                                                       create_time=create_time)
            return await stub.UpdateArticle(request)

    @grpc_error_handler
    async def delete_article(self, article_id):
        """ 删除文章 """
        async with ArticleStub() as stub:
            request = article_pb2.DeleteArticleRequest(id=article_id)
            return await stub.DeleteArticle(request)
