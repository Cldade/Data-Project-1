from dataclasses import dataclass
from requests.models import Response
import requests
import json
import threading
import time
import csv
from faker import Faker
import random


precio_lista = [4,15,19,29,30,39,45,69,89,129,149,169,199,699]
productos_lista = ['Landskrona', 'Brimnes', 'Ekedalen', 'Evedal', 'Ulriksberg', 'Idanäs', 'Starkvind', 'Eket', 'Odger', 'Bleckberget', 'Skurup', 'Dejsa', 'Nymane', 'Raskog', 'Bergpalm', 'Elloven', 'Torared', 'Kermsund', 'Ikea 365+', 'Mala']
faker = Faker()


def pedirFrase():

 while True:
  print(f'Name: {faker.first_name()}')
  First_name = {faker.first_name()}

  print(f'Last name: {faker.last_name()}')
  Last_name = {faker.last_name()}

  print(f'Address: {faker.address()}')
  Address = {faker.address()}
  result = random.choice(precio_lista)
  result2 = random.choice(productos_lista)
  print(result)
  data =  [First_name, Last_name, Address, result, result2]
  with open('Clientes.csv', 'a') as file:

        writer = csv.writer(file)

        writer.writerow(data) 



  time.sleep(3)



pedirFrase()