FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirement.txt

ENTRYPOINT ["python", "evaluate.py"]
CMD ["all"]