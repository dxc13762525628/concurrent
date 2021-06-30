#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/30 14:48 
# @Author : dxc
# @File : aiofile_exercise.py
"""
aiofiles的
应用场景
    可能向几个不同的文件写数据
    python 3.6.8
"""
import aiofiles
import asyncio


class AiofileExercise:
    """
    aiofiles的文件数据
    """

    def __init__(self):
        """
        对于如果有许多数据的，可以一边操作数据，构成字典 yield出来给协程去处理
        """
        self.res = {
            "./int.txt": 'data1',
            "./str.txt": 'data1',
            "./dict.txt": 'data1',
            "./list.txt": 'data1',
        }

    async def write(self, filename, data):
        """
        写数据
        :param data:
        :return:
        """
        async with aiofiles.open(filename, 'w', encoding='utf-8')as fp:
            await fp.write(data)

    async def main(self):
        """
        主函数
        :return:
        """
        tasks = [asyncio.ensure_future(self.write(path, value)) for path, value in self.res.items()]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    aio = AiofileExercise()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aio.main())
    loop.close()
