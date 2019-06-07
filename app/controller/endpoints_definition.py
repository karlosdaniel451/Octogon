from flask import jsonify
from app.controller.dojot_api_access import DojotApiAccess
import json
import requests
import time
from datetime import datetime

dojot_api_access = DojotApiAccess('192.168.0.101', '8000', 'admin', 'admin')


def define_endpoints(app):

    @app.route('/')
    def hello_world():
        return jsonify({
            'about': 'Hello world'
        })

    @app.route('/device/<device_id>/history/')
    def get_device_all_data(device_id):
        return jsonify(dojot_api_access.get_all_device_data(device_id))

    @app.route('/device/<device_id>/history/<lastN>/<attr>/')
    def get_lastN_attribute_device_data(device_id, lastN, attr):
 
        return jsonify(dojot_api_access.get_data_by_n_values_attribute(
            device_id, lastN, attr))


    @app.route('/device/<device_id>/history/<lastN>/<attr>/<dateFrom>/<dateTo>/')
    def get_lastN_attribute_device_dated_data(device_id, lastN, attr, dateFrom,
                                              dateTo):
        return jsonify(dojot_api_access.get_lastN_attribute_device_dated_data(
            device_id, lastN, attr, dateFrom, dateTo))
