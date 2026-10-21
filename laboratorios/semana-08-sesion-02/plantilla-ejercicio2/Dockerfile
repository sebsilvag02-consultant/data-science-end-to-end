FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MPLBACKEND=Agg

WORKDIR /app/plantilla-ejercicio2

COPY plantilla-ejercicio2/requirements.txt ./requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY plantilla-ejercicio2/explorar_relaciones.py ./explorar_relaciones.py
COPY starter/viajes_taxi.csv /app/starter/viajes_taxi.csv

CMD ["python", "explorar_relaciones.py"]
