FROM python:3.6.8-slim-stretch

#===========================================================
#更换apt源安装socat,并安装py3下的Crypto库(中途warning无影响可忽略)
#===========================================================

RUN sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/' /etc/apt/sources.list && \
    sed -i '/security/d' /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get install socat -y && \
    pip3 install pycryptodome -i https://mirrors.aliyun.com/pypi/simple/

COPY server.py \
     secret.py \
     /usr/src/app/

#=======================
#socat将py脚本挂载到9999端口
#=======================

ENTRYPOINT socat TCP4-LISTEN:9999,tcpwrap=script,reuseaddr,fork EXEC:"/usr/bin/env python3 -u /usr/src/app/server.py"