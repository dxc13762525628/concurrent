# debain

## python3.7.3

```python
# 首先安装构建Python源代码所需的软件包
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
# 下载最新的 Python下载页面使用以下 curl命令发布了该发行版的源代码
curl -O https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
# 下载完成后，提取压缩包：
tar -xf Python-3.7.3.tar.xz
# 导航到Python源目录并运行configure脚本，该脚本将执行许多检查以确保所有依赖性您系统上的
cd Python-3.7.3
# --enable-optimizations选项将通过运行多个测试来优化Python二进制文件，这会使构建过程变慢
./configure --enable-optimizations
#运行make以开始构建过程
make -j 8 # 8表示核数pytohhn
# 查看核数
nproc
# 安装构建 请勿使用标准make install，因为它将覆盖默认系统python3二进制文件 
make altinstall
# 验证
python3.7 --version

# 有报错
"""
generate-posix-vars failed
make[3]: *** [Makefile:604: pybuilddir.txt] Error 1
make[3]: Leaving directory '/home/wb.duanxingcai/Python-3.7.3'
make[2]: *** [Makefile:519: build_all_generate_profile] Error 2
make[2]: Leaving directory '/home/wb.duanxingcai/Python-3.7.3'
make[1]: *** [Makefile:495: profile-gen-stamp] Error 2
make[1]: Leaving directory '/home/wb.duanxingcai/Python-3.7.3'
make: *** [Makefile:507: profile-run-stamp] Error 2
"""
# lsb_release -a
# gcc --version
# apt upgrade gcc
# echo $PYTHONPATH

```

## 安装虚拟环境

```python
# 安装pip
apt install python3-pip
# 安装virtualenv
pip3 install virtualenv
# 安装指定版本的python环境
virtualenv -p /usr/bin/python py2(虚拟环境的名字)
virtualenv -p /usr/bin/python3 py3
# 激活虚拟环境
cd py2/ (进入自己创建的虚拟环境目录)
source bin/activate
python -V
# 退出虚拟环境
deactivate
```

## 安装docker

### 使用存储库安装

```python
# 更新apt包索引并安装包以允许apt通过 HTTPS 使用存储库
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
# 添加Docker官方的GPG密钥：
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# 使用以下命令设置稳定存储库
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### 安装docker引擎

```python
# 更新apt包索引，安装最新版本的Docker Engine和containerd，或者到下一步安装特定版本
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
# 要安装特定版本的 Docker Engine，请在 repo 中列出可用版本，然后选择并安装：
apt-cache madison docker-ce # 获取版本号
sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io # 安装指定版本
# 测试
sudo docker run hello-world
```

### docker 报错

```python
# 错误方式
docker run -itd mtl_fit_remind -p 0.0.0.0:8005:8001 /bin/bash
a6606f50a2624d5c5cda40ad8988f06196c02128a4d3757277fd9caba972e774
docker: Error response from daemon: invalid header field value "oci runtime error: container_linux.go:247: starting container process caused \"exec: \\\"-p\\\": executable file not found in $PATH\"\n".
# 解决办法
docker run --name mtl_fit_server -p 0.0.0.0:8005:8001 -itd mtl_fit_remind /bin/bash
41114ab618e9c85a3cbe67ee1957e45ab4bf3e57ea5a48660fe9c650e2a81532
```

### docker网卡配置

```python
# 关于docker 网卡
:~$ cat /etc/docker/daemon.json
{
"mtu": 1400
}
```



## docker里面安装软件

### vim

```python
# 同步 /etc/apt/sources.list 和 /etc/apt/sources.list.d 中列出的源的索引，这样才能获取到最新的软件包
apt-get update
# 安装vim
apt-get install vim
```

### cron

```python
# 安装
apt-get install cron
# 启动
service cron start
# 检查状态
service cron status
# 查询cron可用的命令：
service cron
```

### 时区配置

```python
# 1查看时区是否正确为
date -R
# 2. 如果与当前时区不符合
cp -i /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# 可能会报错 看报错原因无法将上海时区写入到localtime
cp: not writing through dangling symlink '/etc/localtime'
# 2.1 解决报错
rm -rf /etc/localtime
# 3. 重新执行
cp -i /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# 校验
date-R
```

## linux主机时区同步

```python
# 1. 修改配置文件
vim /etc/default/rcS
# 写入配置
UTC=no
# 安装软件
apt-get install ntpdate
# 执行
ntpdate-debian
```

## 数据备份与恢复

```python
# 备份 不成功用 ./mongodump 去运行
/user/local/mongodb/bin/mongodump -d net_work -c global_ip_0 -o /home/wb.duanxingcai/mongo_global/
# 数据恢复
/user/local/mongodb/bin/mongorestore -d net_work -c global_ip /home/wb.duanxingcai/mongo_data/net_work/global_ip_0.bson

# 数据导出
./mongoexport -d net_work -c global_ip -o /home/xuwei01/global_ip.csv
# 数据导入
./mongoimport -d net_work -c global_ip --file /home/xuwei01/global_ip.csv

```

## nginx

```python
user  nginx;
worker_processes     4;
worker_cpu_affinity 0001 0010 0100 1000;
#worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on 负载均衡;
    upstream cotest-server {
        server 10.215.0.116:8017 weight=5;
        server 10.215.0.117:8017 weight=4;
    }
    include /etc/nginx/conf.d/*.conf;
}

```



## mongodb

## mysql

## 部署Minio服务器

### 正常部署

```python
# 下载
wget https://dl.min.io/server/minio/release/linux-amd64/minio
# 加权限
chmod -x minio
# 启动
./minio server /usr/software/minio/data
# 或者 设置账号密码
MINIO_ACCESS_KEY=myminioadmin MINIO_SECRET_KEY=myminioadmin ./minio server /usr/software/minio/data
# 再或者
MINIO_ACCESS_KEY=myminioadmin MINIO_SECRET_KEY=myminioadmin ./minio server --config-dir /usr/software/minio/config /usr/software/minio/data

# 后台启动
nohup ./minio server /usr/software/minio/data  >  log.log &
# 或者

MINIO_ACCESS_KEY=myminioadmin MINIO_SECRET_KEY=myminioadmin nohup ./minio server --config-dir /usr/software/minio/config /usr/software/minio/data>  log.log &

# 启动成功 浏览器输入host:9000即可
```

### docker 部署

## 安装yapi

### docker安装

```python
1. 国内加速镜像
# vi /etc/docker/daemon.json
{
    'registry-mirrors':["http://hub-mirror.c.163.com"]
}
2. docker 重启
	systemctl restart docker.service
```

```python
# 下载monogo
docker run -d --name mongo-yapi mongo
# 拉镜像
2. docker pull registry.cn-hangzhou.aliyuncs.com/anoy/yapi
# 配置monog数据库及账号
docker run -d --name yapi --link mongo-yapi:mongo --entrypoint npm --workdir /api/vendors registry.cn-hangzhou.aliyuncs.com/anoy/yapi run install-server
# 启动yapi的docker
docker run -d \
  --name yapi \
  --link mongo-yapi:mongo \
  --workdir /api/vendors \
  -p 3000:3000 \
  registry.cn-hangzhou.aliyuncs.com/anoy/yapi \
  server/app.js
# 登录默认
user: 		admin@admin.com
password:   ymfe.org
```

```python
"""
如需重启
docker start mongo-yapi
docker start yapi
"""
```

### Win10环境安装

```python
1. 首先安装node.js环境 (注意别用14会冲突)
2. 安装mogodb数据库
# 3. 官网https://hellosean1025.github.io/yapi/devops/index.html#%e7%89%88%e6%9c%ac%e9%80%9a%e7%9f%a5
3. 进入cmd命令 执行
   npm install -g yapi-cli --registry https://registry.npm.taobao.org
4. 执行yapi server
5. 浏览器输入端口127.0.0.1:9090 即可以进入页面了
6. 简单的配置就可以部署了，注意不要关闭cmd命令窗口
7. 结束后会有
"""
初始化管理员账号成功,账号名："admin@admin.com"，密码："ymfe.org"
部署成功，请切换到部署目录，输入： "node vendors/server/app.js" 指令启动服务器, 然后在浏览器打开 http://127.0.0.1:3000 访问
"""
8. 进入my_yapi目录执行cmd命令
	node vendors/server/app.js
    浏览器打开访问就好啦
```

## 基本命令

```python
# 查看版本号
lsb_release -a
```

### 防火墙相关

```python
# 更新索引包
apt-get update
# 下载systemctl
apt-get install systemctl
# 开发防火墙
 systemctl start firewalld
# 重启防火墙
systemctl restart firewalld
# 关闭防火墙
systemcel stop firewalld
# 设置开机启动 
systemctl enable firewalld

# 重启nginx
systemctl restart nginx
```

## 部署服务相关

### 后端django服务

#### docker 安装数据库及获取映射ip

```python
# 获取redis
docker pull redis
# 启动redis 
docker run -p 6379:6379 --name myredis -v /usr/local/docker/redis.conf:/etc/redis/redis.conf -d redis redis-server /etc/redis/redis.conf --appendonly yes
# 进入redis
docker exec -it myredis /bin/bash
# 获取映射ip
cat /etc/host
172.0.0.3
# mysql也是一样的方式就可以了，如果其他容器也想获取的话，直接输入获取到的映射ip就可以了
```

#### mongodb

```python
# 拉取镜像
docker pull mongo
# 查看镜像
docker images
# 启动并创建容器
docker run -itd --name mongo -p 27017:27017 mongo
# 进入容器内部
docker exec -it mongo mongo admin
# 创建用户
db.createUser({ user:'admin',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'},"readWriteAnyDatabase"]});
# 测试连接
db.auth('admin', '123456')
```

#### 跨域问题解决

```python
# 安装django-cors-headers
pip install django-cors-headers
# 中间件
MIDDLEWARE_CLASSES = (
  ...
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware', # 注意顺序
  ...
)
# app注册
INSTALLED_APPS = [
  ...
  'corsheaders'，
  ...
 ] 
# 设置跨域
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
  '*'
)
CORS_ALLOW_METHODS = (
  'DELETE',
  'GET',
  'OPTIONS',
  'PATCH',
  'POST',
  'PUT',
  'VIEW',
)
  
CORS_ALLOW_HEADERS = (
  'XMLHttpRequest',
  'X_FILENAME',
  'accept-encoding',
  'authorization',
  'content-type',
  'dnt',
  'origin',
  'user-agent',
  'x-csrftoken',
  'x-requested-with',
)
```

#### mysql

```python
# 拉取镜像
docker pull mysql
# 启动容器
docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql

# mysql 
# root 123456

# mysql的配置文件
[mysqld]
default_authentication_plugin=mysql_native_password
```

#### redis

```python
# 拉取镜像
docker pull redis
# 启动容器
docker run -itd --name redis -p 6379:6379 redis
```

#### Dockerfile

```python
FROM python:3.6

MAINTAINER username <username@qq.com>

COPY .  /www/

WORKDIR /www/

RUN pip install -r /www/project/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
CMD ["/bin/bash"]
```

#### uwsgi

```python
[uwsgi]
# 通讯方式及端口
#socket=127.0.0.1:8000
http= :8001

# 项目当前工作目录
chdir=/www/co_test
# 项目中wsgi.py文件的目录，相对于shdir
#module=fwzs.wsgi
#env = DJANGO_SETTING_MODULE=fwzs.setting
wsgi-file=/www/co_test/co_test/wsgi.py
# 进程个数
processes=4
# 每个进程的线程个数
threads=2
# 服务的主进程pid记录文件
pidfile=pid.wsgi
daemonize = /var/log/uwsgi.log
# 服务的目志文件位置
#daemonize=uwsgi.log
# 开启主进程管理模式
# 一主多从，主接收外界通讯并fork子进程，子进程实现具体功能
master=true
# 退出，重启是清理日志文件
vacuum=true
listen=120
#socket-timeout = 10
logdate = true

#post-buffering = 8192
#logto = /var/log/uwsgi/uwsgi.log
#touch-logreopen = /var/log/uwsgi/.touchforlogrotat
#status=/tmp/uwsgistats.socket
# 通讯方式区别
# http
# 客户端主动发起请求,服务器响应,服务器不能主动发起响应.
# 一次请求完毕后则断开连接,以节省资源.

# Socket
# 双方都可以主动发送数据
# 客户端跟服务器直接使用Socket进行连接,可保持连接通道

# 安装uwsgi
pip install uwsgi
# 启动uwsgi
uwsgi uwsgi.ini
# 杀掉并重启重启uwsgi
pkill uwsgi
```

#### 部署

```python
# 部署
co_test项目目录打包-->co_test.zip  包含dockerfile文件
# 解压
unzip co_test
# 构建项目
docker build -f co_test/Dockerfile -t co_test_server .
# 启动容器
docker run -itd --name co_test_server -p 0.0.0.0:8001:8001 co_test_server
# 进入容器
docker exec -it co_test_server /bin/bash
# 进入项目目录
cd co_test
# 安装uwsgi
pip install uwsgi
# 启动项目
uwsgi uwsgi.ini
# 查看是否有输出的日志
cat /var/log/uwsgi.log


---------------------------------------------------celery相关----------------------------------------------------------------
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

#### 更新

```python
# 打包co_test.zip
co_test-->co_test.zip
# 解压
unzip co_test
# 更新
docker cp co_test co_test_server:/www/
# 进入容器
docker exec -it co_test_server /bin/bash
# 重启uwsgi
pkill uwsgi
```

#### 数据库连接超时

```python
# 关于数据库连接
"""
只有两种情况
1. 直接服务器地址连接
2. 服务器docker内部的映射连接
如果连接外部服务器的数据库
看防火墙是否关闭 
"""
```



### 前端相关

#### Dockerfile

```python
FROM nginx:latest

MAINTAINER dxc <dxc@163.com>

RUN rm /etc/nginx/conf.d/default.conf

ADD conf.d/default.conf /etc/nginx/conf.d/

COPY dist/  /usr/share/nginx/csm/
```

#### 部署

```python
# 服务器内部有个nginx解析域名，转发到docker80端口，docker 内部80转发到服务器后端
# 部署
npm run build
dist ->dist.zip 统计目录有conf.d下的default.conf文件 ,Dockerfile文件
docker build -t 镜像名字 .
docker run -itd -p 0.0.0.0:8001:80 --name 容器名字 镜像名字
-
# 更新
npm run build -> dist
dist -> dist.zip -> server
unzip dist.zip
cd dist
docker cp . cotest_client:/usr/share/nginx/csm
docker restart cotest_client

# 前端nginx配置文件位置
/etc/nginx/nginx.conf
```

