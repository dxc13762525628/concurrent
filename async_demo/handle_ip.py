#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/29 11:32 
# @Author : dxc
# @File : handle_ip.py
"""
使用协程处理ip  python3.7 linux环境
关于ping操作
"""
import asyncio

# 设置并发度
sem = asyncio.Semaphore(500)


class PingIp:
    """
    ping ip异步处理
    """
    def __init__(self):
        self.ips = ['75.240.51.10', '75.240.51.10', '75.240.51.10', '75.240.51.10', '75.240.51.10', '75.240.51.10']

    @staticmethod
    async def ping_ip(ip):
        """
        ping ip 异步获取评价延时和丢包率
        :param ip:
        :return:
        """
        async with sem:
            cmd = 'ping -n 4 {}'.format(ip)
            proc = await asyncio.create_subprocess_exec(
                cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                stdin=asyncio.subprocess.PIPE)

            stdout, stderr = await proc.communicate()
            res = stdout.decode('gbk')
            return res

    async def main(self):
        """
        主函数
        :return:
        """
        for ip in self.ips:
            tasks = []
            data = []
            # 将一个一个的ip放到协程队列中去
            tasks.append(asyncio.ensure_future(self.ping_ip(ip)))
            # 获取异步的返回结果进行操作
            results = await asyncio.gather(*tasks)
            for result in results:
                # 获取执行结果
                data.append(result)


if __name__ == '__main__':
    ping_ip = PingIp()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ping_ip.main())
    loop.close()
