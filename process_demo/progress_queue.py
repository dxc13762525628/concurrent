#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/5 15:53 
# @Author : dxc
# @File : progress_queue.py
"""
多进程的queue
"""

import time
from multiprocessing import Queue, Process


class QueueDemo:
    """
    queue的简单使用
    """
    def __init__(self):
        self.queue = Queue()

    def producer(self):
        """
        生产者
        :return:
        """
        for i in range(10):
            self.queue.put(i)
        time.sleep(0.5)

    def consumer(self):
        """
        消费者
        :return:
        """
        time.sleep(0.5)
        datas=[]
        while not self.queue.empty():
            data = self.queue.get()
            datas.append(data)
        print(datas)
        print(self.queue.empty())

    def run(self):
        """
        主要运行的函数
        :return:
        """
        my_producer = Process(target=self.producer, )
        my_consumer = Process(target=self.consumer, )
        my_producer.start()
        my_consumer.start()
        my_producer.join()
        my_consumer.join()


if __name__ == '__main__':
    queue = QueueDemo()
    queue.run()
