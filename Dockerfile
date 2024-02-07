FROM python:3.12-alpine3.19
WORKDIR /bot

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . . 

CMD ["python","main.py"]


