#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/30 14:28 
# @Author : dxc
# @File : aiofile_demo.py
import asyncio
import aiofiles


class AiofilesDemo:
    """
    aiofile的简单使用
    python 3.6.8
    """

    def __init__(self, filename='demo.txt'):
        self.filename = filename

    async def write(self, data):
        """
        写数据
        :param data:
        :return:
        """
        async with aiofiles.open(self.filename, 'w', encoding='utf-8')as fp:
            await fp.write(data)

    async def read(self):
        """
        异步读取数据
        :return:
        """
        async with aiofiles.open(self.filename, 'r', encoding='utf-8') as fp:
            content = await fp.read()
            return content


if __name__ == '__main__':
    aiofile_demo = AiofilesDemo()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aiofile_demo.write('111111'))
    print(loop.run_until_complete(aiofile_demo.read()))

