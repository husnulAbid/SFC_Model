FROM python:3.10


ENV PYTHONBUFFERED=1

WORKDIR /code

COPY sfc_model/requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

COPY sfc_model/datasets/ datasets/

EXPOSE 5100