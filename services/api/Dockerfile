FROM python:3.10

WORKDIR /src

COPY . .

RUN pip install fastapi
RUN pip install requests
RUN pip install uvicorn
RUN pip install sqlalchemy
RUN pip install psycopg2

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]