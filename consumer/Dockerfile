FROM python:3-alpine

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD consumer.py /opt/consumer.py

CMD python /opt/consumer.py
