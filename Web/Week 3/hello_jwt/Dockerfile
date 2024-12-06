FROM python:3.11

COPY ./src /app

WORKDIR /app

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask && \
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyjwt

CMD python3 app.py