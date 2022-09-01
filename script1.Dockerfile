FROM python:3

COPY ./IoT_scripts/script-1-producer.py ./main.py
COPY ./requirements.txt ./

RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
CMD ["python", "./main.py"]