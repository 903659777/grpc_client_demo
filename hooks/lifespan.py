# -*- coding = utf-8 -*-
# @Time :2024/10/26 18:34
from contextlib import asynccontextmanager
from fastapi import FastAPI
from utils.demo_consul import DemoConsul


demo_consul = DemoConsul()


@asynccontextmanager
async def lifespan(app: FastAPI):
    demo_consul.register()  # 注册
    await demo_consul.fetch_grpc_servic_demo_addresses()
    yield
    demo_consul.deregister()  # 注销
