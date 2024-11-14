# 使用官方的 Python 镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制要求的文件
#COPY requirements.txt .
COPY main.py .
# 安装依赖
RUN pip install --no-cache-dir flask


# 设置环境变量
ENV flag=0xGame{Pickle_Unserliaze_Without_Any_Limit_Is_Not_Safe!}
EXPOSE 8000

# 运行 Flask 应用
CMD ["python3", "main.py"]