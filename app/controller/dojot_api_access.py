import requests
import json


class DojotApiAccess():

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.base_url = f'http://{self.host}:{self.port}/'
        self.authentication_header = {'Content-Type': 'application/json '}
        self.default_header = {
            'Authorization': f'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJKMThIZmhmaG9TVHlVSzZsRXQySmVHV3JoREt1UXExTCIsImlhdCI6MTU1OTkzMTA0MywiZXhwIjoxNTU5OTMxNDYzLCJuYW1lIjoiQWRtaW4gKHN1cGVydXNlcikiLCJlbWFpbCI6ImFkbWluQG5vZW1haWwuY29tIiwicHJvZmlsZSI6ImFkbWluIiwiZ3JvdXBzIjpbMV0sInVzZXJpZCI6MSwianRpIjoiMWE5ZjExMTg5MGYyYTRlNWY1NDI3NWMwMDRlZjE4NTciLCJzZXJ2aWNlIjoiYWRtaW4iLCJ1c2VybmFtZSI6ImFkbWluIn0.WEHfyj9KvvW8q48G1lmunMjsLuedwpWNe-aLQrNETSU'
        }

    def get_access_token(self):
        url = f'{self.base_url}auth'
        payload = {
            'username': f'{self.username}',
            'passwd': f'{self.password}'
        }
        response = requests.get(
            url, headers=self.authentication_header, data=payload)

        return response.json()

    def get_data_by_n_values_attribute(self, device_id, lastN, attr):
        url = f'{self.base_url}history/device/{device_id}/history?lastN='
        url += f'{lastN}&attr={attr}'
        response = requests.get(url, headers=self.default_header)

        return response.json()

    def get_all_devices(self):
        url = f'{self.base_url}device'
        response = requests.get(url, headers=self.default_header)

        return response.json()

    def get_all_device_data(self, device_id):
        url = f'{self.base_url}history/device/{device_id}/history'

        response = requests.get(url, headers=self.default_header)

        return response.json()

    def get_lastN_attribute_device_data(self, device_id, lastN, attr):
        # url = f'/device/{device_id}/history?lastN={lastN}&attr={attr}'
        url = f'{self.base_url}history/device/{device_id}/history?lastN='
        url += f'{lastN}&attr={attr}'

        response = requests.get(url, headers=self.default_header)

        return response.json()

    def get_lastN_attribute_device_dated_data(self, device_id, lastN, attr,
                                              dateFrom, dateTo):
        url = f'/device/{device_id}/history?lastN={lastN}&attr={attr}&'
        +'dateFrom={dateFrom}&dateTo={dateTo}'

        response = requests.get(url, headers=self.default_header)

        return response.json()

    def get_total_consumption(self):
        pass
