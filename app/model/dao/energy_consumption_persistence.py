"""
from app.model.dao.database_access import DatabasAccess
from app.controller.dojot_api_access import DojotApiAccess

from app.model.dao.database_access import DatabasAccess

import threading
import time


class EnergyConsumptionPersistence:

    def __init__(self, device_id):
        self.device_id = device_id

    def persist(self):
        database_access = DatabasAccess(
            '127.0.0.1', 27017, 'octogon', 'consumo_kWh')
        dojot_api_access = DojotApiAccess('127.0.0.1', 8000, 'admin', 'admin')

        while True:
            database_access.insert_one({
                'device_id': f'{self.device_id}',
                'ts': f'{time_stamp}',
                'value': f'{acumula_kW()}',
                'attr': 'kilowatt_hora'
            })

    def acumula_kW(self):
        somatorio_kilowatt_hora = 0
        while True:
            print('chegou no loop')

            response_data_dict = dojot_api_access.get_lastN_attribute_device_data(
                self.device_id, i, 'AmpsRMS,Consumo')
            ampere = response_data_dict['AmpsRMS']
            volt = response_data_dict['Consumo']
            watt = volt * ampere
            tempo_hora = 5 / 3600
            kilowatt_hora = (watt * tempo_hora) / 1000

            somatorio_kilowatt_hora += kilowatt_hora
            time_stamp = response_data_dict['ts']
            time.sleep(120)
            return somatorio_kilowatt_hora

    def calcular_consumo_energia(volt, ampere, tempo, tarifa):
        return calcular_kWh(volt, ampere, tempo) * tarifa

    def calcular_kWh(volt, ampere, tempo):
        watt = volt * ampere
        tempo_hora = tempo / 3600
        kilowatt_hora = (watt * tempo_hora) / 1000
        return kilowatt_hora

    def calcular_intervalo_tempo(data_inicial, data_final):
        formato = '%Y/%m/%d %H:%M:%S.%f'

        return (datetime.strptime(data_inicial, f) - datetime.strptime(t, data_final)).total_seconds()
"""

# Armazenar no banco de dados o consumo em kWh conforme os dados já armazenados no Dojot
# Armazenar os dados que o consumo em kWh conforme os dados que forem sendo adicionados após a inicialização do servidor
# Para armazenar o consumo em ambas as situações, deve-ser calcular e acumular o consumo em kWh a cada 5 e, de 10 em 10 minutos, armazenar este consumo

from pymongo import MongoClient


from app.controller.dojot_api_access import DojotApiAccess
from app.model.dao.database_access import DatabasAccess


"""
Modelo de armazenamento no banco de dados:
{
    ts: {ts},
    consumo_kWh: {consumo}
}
"""


class EnergyConsumptionPersistence:
    def __init__(self, host, port, data_base_name, device_id):
        self.device_id = device_id
        self.client = MongoClient(f'{host}', port)
        self.database_acess = DatabasAccess(
            f'{host}', port, f'{data_base_name}', f'consumo_kWh_{device_id}')

    def persist(self):
        dojot_api_access = DojotApiAccess('192.168.0.101', 8000, 'admin', 'admin')
        consumo_kWh_acumulado = 0
        while True:
            data_from_dojot = dojot_api_access.get_all_device_data(
                self.device_id)
            ampere = data_from_dojot['AmpsRMS']
            volt = data_from_dojot['Consumo']

    def calcular_consumo_energia_em_dinheiro(volt, ampere, tempo, tarifa):
        return calcular_kWh(volt, ampere, tempo) * tarifa

    def calcular_kWh(volt, ampere, tempo):
        watt = volt * ampere
        tempo_hora = tempo / 3600
        kilowatt_hora = (watt * tempo_hora) / 1000
        return kilowatt_hora
