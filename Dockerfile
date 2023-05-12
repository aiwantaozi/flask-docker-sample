FROM python:3.9.13

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# 指定端口 --port=8080，不指定的话默认为5000
CMD ["flask", "--app", "flask-server", "run", "--port=5000", "--host=0.0.0.0"]

