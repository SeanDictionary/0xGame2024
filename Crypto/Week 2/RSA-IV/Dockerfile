FROM python:slim AS app
RUN pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple pycryptodome

FROM pwn.red/jail
COPY --from=app / /srv
COPY task.py /srv/app/run
RUN chmod 777 /srv/app/run
COPY challenge.py /srv/app
COPY secret.py /srv/app
ENV JAIL_MEM=30M JAIL_ENV_NUM=5  JAIL_TIME=60
