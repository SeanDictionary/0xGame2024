FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制要求的文件
#COPY requirements.txt .
COPY  main.py main.py
# 安装依赖
RUN pip install --no-cache-dir flask lxml
#RUN apt update
#RUN apt install curl -y


# 设置环境变量
RUN echo 0xGame{114514_XXE_114514_XXE} > /flag
EXPOSE 8000

CMD ["python3","main.py"]
