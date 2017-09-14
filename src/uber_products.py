# coding=utf-8
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

from config.uber_config import UberToken

session = Session(server_token=UberToken) # Fazer autenticação do APP
client = UberRidesClient(session) # Criar sessão

response = client.get_products(-5.8368171,-35.2065031)
products = response.json.get('products')
for product in products:
    print product['short_description'],':', product['product_id']