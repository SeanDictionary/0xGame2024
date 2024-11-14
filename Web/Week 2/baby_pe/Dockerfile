# 使用官方的 Python 镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

#COPY requirements.txt .
COPY main.py main.py
COPY requirements.txt requirements.txt
#COPY whoami.sh whoami.sh
# 安装依赖
RUN #apt update && apt install dc -y
RUN chmod +s $(which find)
RUN useradd -ms /bin/bash app
RUN pip install --no-cache-dir -r requirements.txt
RUN echo "flag要root用户才可以看到,听说flask可以算pin" > /flag && chmod a+r /flag

# 设置环境变量
RUN echo 0xGame{You_Are_The_Privilege_Escalation_Master!} > /root/flag
EXPOSE 8000
# 运行 Flask 应用
USER app

CMD ["python3", "main.py"]
