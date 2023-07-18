FROM python:3.10

WORKDIR /src

COPY . .

RUN pip install fastapi

RUN pip install uvicorn

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]