FROM python:3-alpine

WORKDIR /opt/app

COPY kekw/ .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "kekw.py"]
