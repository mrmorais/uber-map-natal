# coding=utf-8
import time
import datetime as dt
import pandas as pd
import numpy as np

from uber_rides.session import Session
from uber_rides.client import UberRidesClient

from config.uber_config import UberToken, ProductId
from config.neighborhoods import Neighborhoods

session = Session(server_token=UberToken) # Fazer autenticação do APP
client = UberRidesClient(session) # Criar sessão

#dataFrame = pd.read_csv('uber-map.csv')

while True:
    time_before = dt.datetime.now() # Datetime inicial
    nbhoods_data = {}
    for nbhood in Neighborhoods: # Loop pelos bairros
        estimates = []
        for point in nbhood['points']: # Loop pelos pontos do bairro
            # Executar requisição ao Uber API
            response = client.get_pickup_time_estimates(
                start_latitude=point['latitude'],
                start_longitude=point['longitude'],
                product_id=ProductId
            )
            # print response.json.get('times')
            if (response.json.get('times')):
                estimate = response.json.get('times')[0]['estimate']
                #dataFrame[nbhood['name']].append(estimate)
                estimates.append(estimate)
            else:
                #dataFrame[nbhood['name']].append(estimate)
                estimates.append(0)
        avg_estimate = np.mean(estimates)
        nbhoods_data[nbhood['name']] = pd.Series([avg_estimate], index=[time_before])
    dataFrame = pd.DataFrame(nbhoods_data)
    dataFrame.to_csv('data/uber_map.csv', mode='a', header=False)

    time_after = dt.datetime.now() # Datetime final
    delta = time_after - time_before # Tempo levado para fazer as requisições
    interval = dt.timedelta(0, 180) - delta # Define o intervalo baseado no delta
    time.sleep(interval.seconds) # Espera interval segundos até a próxima onda de requests