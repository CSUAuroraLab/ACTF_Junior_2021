FROM python:3.5

WORKDIR /app
ADD ./www /app
COPY ./requirements.txt /app/requirements.txt
COPY ./flag /app/flag
RUN pip install -r /app/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir
RUN chmod 711 app.py
EXPOSE 80
ENV FLAG flag{Th|s_1s_picKle_anD_F1ask!}
CMD ["python","app.py"]
