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
    """Edit Device Status"""
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


def create_emitter(function, data):
    """Create New Emitter"""
    c_emitter = requests.post(url=URL + 'emitter/', data='{"function":' + '"' + str(
        function) + '"' + ',' + '"status":' + str(data) + '}', headers=HEADERS, auth=AUTH)
    if c_emitter.status_code == 201:
        emitter_data = c_emitter.json()
        return emitter_data['id']
    else:
        print("创建失败,请检查是否又重复设备")


def create_relay(data):
    """Create New Relay"""
    c_relay = requests.post(
        url=URL + 'relay/', data='{"status": ' + str(data) + '}', headers=HEADERS, auth=AUTH)
    if c_relay.status_code == 201:
        relay_data = c_relay.json()
        return relay_data['id']
    else:
        print("创建失败,请检查是否又重复设备")


def create_sensor(name, data):
    """Create New Sensor"""
    c_sensor = requests.post(url=URL + 'sensor/', data='{"name":' + '"' + str(
        name) + '"' + ',' + '"status":' + str(data) + '}', headers=HEADERS, auth=AUTH)
    if c_sensor.status_code == 201:
        sensor_data = c_sensor.json()
        return sensor_data['id']
    else:
        print("创建失败,请检查是否又重复设备")


def delete_device(type_id, device_id):
    """Delete Device"""
    if type_id == 0:
        d_device = requests.delete(
            url=URL + 'emitter/' + str(device_id), headers=HEADERS, auth=AUTH)
        return d_device.status_code
    if type_id == 1:
        d_device = requests.delete(
            url=URL + 'relay/' + str(device_id), headers=HEADERS, auth=AUTH)
        return d_device.status_code
    if type_id == 2:
        d_device = requests.delete(
            url=URL + 'sensor/' + str(device_id), headers=HEADERS, auth=AUTH)
        return d_device.status_code
