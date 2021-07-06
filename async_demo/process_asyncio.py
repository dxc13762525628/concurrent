#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/1 17:18 
# @Author : dxc
# @File : process_asyncio.py
"""
多进程+协程  python 3.6.8
"""
import asyncio
from multiprocessing import Process


async def do_something(i, pip_index):
    """
    协程做的io逻辑处理
    :param i:
    :param pip_index:
    :return:
    """
    await asyncio.sleep(i/2)
    print(str(pip_index) + '做事情' + str(i))
    return i/2


async def main(pip_index):
    """
    多进程里面跑多个协程
    :return:
    """
    tasks = [asyncio.ensure_future(do_something(i, pip_index)) for i in range(10)]
    results = await asyncio.gather(*tasks)
    for res in results:
        """
        获取协程的放回结果
        """
        print(res)
        pass


def run(i):
    """
    一个协程任务
    :return:
    """
    print("我是第{}个进程".format(i))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(i))
    loop.close()


def run_process():
    """
    开启多个进程
    :return:
    """
    p_list = []
    for i in range(1, 5):
        p = Process(target=run, args=(i,))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()


if __name__ == '__main__':
    run_process()
