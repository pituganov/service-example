FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -U --no-cache-dir -r requirements.txt

CMD [ "python", "./api.py"]
