# -*- coding = utf-8 -*-
# @Time :2024/10/26 19:36
from typing import Tuple, List, Dict, Union, Optional
import socket
import consul
import uuid
from .single import SingletonMeta
from dns import asyncresolver, rdatatype
from settings import settings


def get_current_ip() -> Tuple[str, int]:
    # 获取ip地址
    sock_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_ip.connect(("8.8.8.8", 80))
    ip = sock_ip.getsockname()[0]
    sock_ip.close()
    return ip


class ServiceAddress:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.count = 0

    def increment(self):
        # 访问一次count+1
        self.count += 1


class LoadBalancer:
    """ 负载均衡器 """

    def __init__(self, addresses: List[Dict[str, Union[str, int]]] = None):
        self.addresses: List[ServiceAddress] = []
        if addresses:
            self.init_addresses(addresses)

    def init_addresses(self, addresses: List[Dict[str, Union[str, int]]]):
        self.addresses.clear()
        for address in addresses:
            self.addresses.append(ServiceAddress(address['ip'], address['port']))

    def get_address(self) -> Tuple[Optional[str], Optional[int]]:
        """获取地址"""
        # 根据访问次数从小到大排序
        if len(self.addresses) > 0:
            self.addresses.sort(key=lambda address: address.count)
            address = self.addresses[0]  # 获取访问次数最少的地址
            address.increment()  # 访问次数+1
            return address.host, address.port
        else:
            return None, None


class DemoConsul(metaclass=SingletonMeta):
    def __init__(self):
        self.consul_host = settings.CONSUL_HOST
        self.consul_http_port = settings.CONSUL_HTTP_PORT
        self.consul_dns_port = settings.CONSUL_DNS_PORT
        self.client = consul.Consul(self.consul_host, self.consul_http_port)  # consul所在的ip，默认是localhost
        self.service_id = uuid.uuid4().hex
        self.service_lb = LoadBalancer()

    def register(self):
        ip = get_current_ip()
        port = settings.SERVER_PORT
        self.client.agent.service.register(
            name="grpc_client_demo",  # 名字
            service_id=self.service_id,  # 注册的服务id
            address=ip,  # ip地址
            port=port,  # 端口
            tags=["servic_demo", "http"],  # 标签
            check=consul.Check.http(url=f"http://{ip}:{port}/health", interval="10s")  # 健康检查
        )

    def deregister(self):
        self.client.agent.service.deregister(self.service_id)

    async def fetch_grpc_servic_demo_addresses(self):
        """ 获取服务地址端口 """
        resolver = asyncresolver.Resolver()
        resolver.nameservers = [self.consul_host]  # consul dns服务器地址
        resolver.port = self.consul_dns_port  # consul dnsf服务器端口号
        # 获取grpc_servic_demo这个名字下的所有服务的ip
        answer_ip = await resolver.resolve(f'grpc_servic_demo.service.consul', rdatatype.A)
        ips = []
        for info in answer_ip:
            ips.append(info.address)
        # 获取grpc_servic_demo这个名字下的所有服务的端口
        answer_port = await resolver.resolve(f'grpc_servic_demo.service.consul', rdatatype.SRV)
        ports = []
        for info in answer_port:
            ports.append(info.port)

        address = []
        for index, port in enumerate(ports):
            if len(ips) == 1:
                address.append({"ip": ips[0], "port": port})
            else:
                address.append({"ip": ips[index], "port": port})
        # 将获取到的地址放入负载均衡器中
        self.service_lb.init_addresses(address)

    def get_one_grpc_servic_demo_service_address(self) -> Tuple[Optional[str], Optional[int]]:
        return self.service_lb.get_address()
