FROM python:3.9

RUN mkdir /ikea
WORKDIR /ikea

COPY . /ikea

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]