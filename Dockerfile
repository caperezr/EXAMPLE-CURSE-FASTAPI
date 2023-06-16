FROM python:3.10

WORKDIR /app/example-curse-fastapi

COPY src/ .
COPY requirement_local.txt .

RUN python -m pip install --upgrade pip
RUN python -m pip install uvicorn

RUN pip install -r ./requirement_local.txt

WORKDIR /app/example-curse-fastapi

CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]


