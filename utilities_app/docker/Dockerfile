FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY ./app /app
