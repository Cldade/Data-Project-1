FROM python

COPY ./python/main.py /app/python/
COPY ./python/genera_clientes.py /app/python/
COPY ./python/genera_ventas.py /app/python/
COPY ./python/insertar_influencers.py /app/python/
COPY ./python/insertar_productos.py /app/python/
COPY ./requirements.txt /app/python/
COPY ./csv/Influencers.csv /app/csv/
COPY ./csv/Productos.csv /app/csv/

WORKDIR /app/
RUN pip install -r python/requirements.txt

ENTRYPOINT ["python3", "python/main.py"]