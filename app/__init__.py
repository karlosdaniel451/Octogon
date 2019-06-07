from app.controller.endpoints_definition import define_endpoints
from flask import Flask
# from model.dao.energy_consumption_persistence import EnergyConsumptionPersistence
from app.model.dao.energy_consumption_persistence import EnergyConsumptionPersistence
import threading
# import config

#energy_consumption_persistence = EnergyConsumptionPersistence(12345)


def create_app():
    app = Flask(__name__)

    # app.config.from_object(config)

    define_endpoints(app)

    #t = threading.Thread(target=worker)

    #thread = threading.Thread(target=energy_consumption_persistence.persist())

    #thread.start()

    #host_dojot, host_mongodb = get_env_data()

    #energy_consumption_persistence = EnergyConsumptionPersistence(
    #    host_mongodb, 27017, 'octogon', 'bOfca5')

    #print(host_dojot, host_mongodb)

    return app


"""
def get_env_data():
    host_dojot = input('IP do host do Dojot: ')
    host_mongodb = input('IP do host IP do MongoDB: ')

    return {
        'host_dojot': host_dojot,
        'host_mongodb': host_mongodb
    }
"""