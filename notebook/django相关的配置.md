# Django相关的配置

## 定时任务篇

### celery

```python
# 安装
pip install celery
pip install django-celery
pip install redis==2.10.6
# setting.py 里面的配置
INSTALLED_APPS = [
	....
    'djcelery',
]
# celery配置
from fwzs.celery_config import *

# 消息中间件地址
# 测试环境redis配置
BROKER_URL = 'redis://host:port/0'
BROKER_TRANSPORT = 'redis'
# 结果存储用redis
BROKER_BACKEND = 'redis'
# 结果存储地址
CELERY_RESULT_BACKEND = 'redis://host:port/1'
```

#### celery的配置文件

```python
# -*- coding: utf-8 -*-
"""
celery的配置文件
"""
import djcelery
import os
import django
from celery.schedules import crontab
from celery import platforms

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fwzs.settings")
django.setup()
djcelery.setup_loader()

platforms.C_FORCE_ROOT = True

# celery执行任务的队列
CELERY_QUEUES = {
    # 定时任务队列
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    },
    # 其他队列
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_type': 'direct',
        'binding_key': 'work_queue'
    }
}

# celery默认配置队列
CELERY_DEFAULT_QUEUE = 'work_queue'

# celery任务模块
CELERY_IMPORTS = (
    'user.api.tasks',  # 
    'service.api.tasks',
)

# 有些情况可以防止死锁
CELERYD_FORCE_EXECV = True

# 设置并发的worker数量
CELERYD_CONCURRENCY = 4

# 允许重试
CELERY_ACKS_LATE = True

# 每个worker最多执行100个任务被销毁，可以防止内存泄露
CELERYD_MAX_TASKS_PER_CHILD = 100

# 单个任务的最大运行时间 软处理 不报异常
CELERYD_TASK_SOFT_TIME_LIMIT = 12 * 30

# 定时任务
CELERYBEAT_SCHEDULE = {
    # 定时获取关注用户列表
    'blank_openid-task': {
        'task': 'get_user_openid-task',
        'schedule': crontab(hour=20, minute=30),
        'options': {
            'queue': 'beat_tasks'
        }
    },
    # 定时获取关注用户列表
    'attention_openid-task': {
        'task': 'add_attention_user-task',
        'schedule': crontab(hour=20, minute=30),
        'options': {
            'queue': 'beat_tasks'
        }
    },
    # 定时更新超过10分钟没有沟通的客服
    'update_service_gt_ten_minute-task': {
        'task': 'update_service_status-task',
        'schedule': crontab(minute='*/5'),
        'options': {
            'queue': 'beat_tasks'
        }
    }
}

# user.api.tasks.py
from celery.task import Task

class AttentionUserTask(Task):
    """
    定时获取未关注用户的openid
    """
    name = 'get_user_openid-task'

    def run(self):
        # 业务逻辑
        ...

# service.api.tasks
from celery.task import Task

class UpdateServiceStatus(Task):
    """
    定时更新客服状态
    """
    name = "update_service_status-task"

    def run(self):
        # 业务逻辑 run函数是写死的 
        ...
        
# 启动celery worker
python manage.py celery worker -l info
# 启动celery beay 
python manage.py celery beat -l info
# 后台启动celery worker
python manage.py celery multi start  worker --loglevel=info --logfile=celery_worker.log
# 后台启动celery beat 
nohup python manage.py celery beat -l info >> celery_beat.log &
# 启动项目
python manage.py runserver 0.0.0.0:8001 
# 后台启动项目
nohup python manage.py runserver 0.0.0.0:8001 >> django.log &
    
# 杀死所有celery worker
pkill -9 -f 'celery worker'
# 杀死所有的celery beat
pkill -9 -f 'celery beat'
# 或者kill -9 pid01 pid02 pid03
# 查看进程
ps -aux|grep celery
```

### django-crontab

```python
# 安装
pip install django-crontab
# setting.py里面的配置
INSTALLED_APPS = (  
'django_crontab',  
...  
)  

CRONJOBS = [  
 # ('*/5 * * * *', 'book.scheduled_task.refresh_task','>>/home/book.log')   app.xxx.xxx.xx  到定时任务函数
]  
```

```python
# linux环境
# 安装
apt-get install cron
# 启动
service cron start
# 检查状态
service cron status
# 查询cron可用的命令：
service cron
```

```python
# 启动django项目
uwsgi uwsgi.ini
# 没有uwsgi
python manage.py runserver 0.0.0.0:8000
# 添加定时任务
python manage.py crontab add
# 显示当前定时任务
python manage.py crontab show
# 删除所有定时任务
python manage.py crontab remove
```

```python
# 常用命令
# 编辑定时任务
crontab -e
# 查看定时任务
crontab -l
```

## django配置session

```python
# mysql 直接默认就好不需要配置
# nosql 默认不支持session
pip install django-mongo-sessions

# 方式一
# setting.ps增加配置
SESSION_ENGINE = 'mongo_sessions.session'
MONGO_SESSIONS_COLLECTION = 'mongo_sessions'  # default option
MONGO_SESSIONS_TTL = 60 * 60  # one hour
MONGO_PORT = 27017
MONGO_HOST = '10.214.12.70'
MONGO_DB_NAME = 'co_test'
MONGO_DB_USER = False
MONGO_DB_PASSWORD = False

# 方式二
# 如果已经有数据库连接
from pymongo import MongoClient
connection = MongoClient()
MONGO_CLIENT = connection.your_database
MONGO_SESSIONS_COLLECTION = 'mongo_sessions
```

