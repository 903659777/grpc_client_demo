# -*- coding = utf-8 -*-
# @Time :2024/9/20 19:29
from functools import wraps
from fastapi.exceptions import HTTPException
from utils.status_code import get_http_code

import grpc


def grpc_error_handler(func):
    """ 捕获出现grpc服务端的异常 """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except grpc.RpcError as e:
            raise HTTPException(status_code=get_http_code(e.code()), detail=e.details())
    return wrapper