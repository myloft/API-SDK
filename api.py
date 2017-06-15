"""API Script"""
# coding:utf-8

import requests

AUTH = ('api', 'api123')
URL = 'https://api.iloft.xyz/'
HEADERS = {'content-type': 'application/json'}


def get_status(type_id, device_id):
    """Get Device Status"""
    if type_id == 0:
        g_emitter = requests.get(
            url=URL + 'emitter/' + str(device_id), auth=AUTH)
        emitter_data = g_emitter.json()
        return emitter_data['status']
    elif type_id == 1:
        g_relay = requests.get(url=URL + 'relay/' + str(device_id), auth=AUTH)
        relay_data = g_relay.json()
        return relay_data['status']
    elif type_id == 2:
        g_sensor = requests.get(url=URL + 'sensor/' +
                                str(device_id), auth=AUTH)
        sensor_data = g_sensor.json()
        return sensor_data['status']


def patch_status(type_id, device_id, data):
    """edit Device Status"""
    if type_id == 0:
        p_emitter = requests.patch(url=URL + 'emitter/' + str(device_id),
                                   data='{"status": ' + str(data) + '}', headers=HEADERS, auth=AUTH)
        return p_emitter.status_code
    elif type_id == 1:
        p_relay = requests.patch(url=URL + 'relay/' + str(device_id),
                                 data='{"status": ' + str(data) + '}', headers=HEADERS, auth=AUTH)
        return p_relay.status_code
    elif type_id == 2:
        p_sensor = requests.patch(url=URL + 'sensor/' + str(device_id),
                                  data='{"status": ' + str(data) + '}', headers=HEADERS, auth=AUTH)
        return p_sensor.status_code
