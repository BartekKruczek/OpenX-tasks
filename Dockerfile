# zmienić na swoją wersję pythona
FROM python:3.9

WORKDIR /app

COPY . /app

# na razie nie ma pliku requirements.txt, tak na przyszłość
# RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]

