FROM python:3.9-slim

WORKDIR /app

COPY app/ /app/
COPY train.py /app/
COPY Housing.csv /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9000

CMD ["sh", "-c", "python train.py && python app.py"]
