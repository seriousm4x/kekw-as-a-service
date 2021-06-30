FROM python:3-alpine

WORKDIR /opt/app

COPY kekw/ .

RUN pip install -U pip && pip install -r requirements.txt

CMD ["python", "kekw.py"]
