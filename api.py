"""API SDK"""
# coding:utf-8

import requests

AUTH = ('api', 'api123')
URL = 'https://api.iloft.xyz/'
HEADERS = {'content-type': 'application/json'}


def get_status(type_id, device_id):
    """Get Device Status"""
    if type_id == 0:
        g_controller = requests.get(
            url=URL + 'controller/' + str(device_id), auth=AUTH)
        controller_data = g_controller.json()
        return controller_data['status']
    elif type_id == 1:
        g_sensor = requests.get(url=URL + 'sensor/' +
                                str(device_id), auth=AUTH)
        sensor_data = g_sensor.json()
        return sensor_data['status']


def patch_status(type_id, device_id, status):
    """Edit Device Status"""
    if type_id == 0:
        p_status = requests.patch(url=URL + 'controller/' + str(device_id),
                                  data='{"status": ' + str(status) + '}', headers=HEADERS, auth=AUTH
                                 )
        return p_status.status_code
    elif type_id == 1:
        p_status = requests.patch(url=URL + 'sensor/' + str(device_id),
                                  data='{"status": ' + str(status) + '}', headers=HEADERS, auth=AUTH
                                 )
        return p_status.status_code


def create_device(type_id, name, status):
    """Create New device"""
    if type_id == 0:
        c_device = requests.post(url=URL + 'controller/', data='{"name":' + '"' + str(
            name) + '"' + ',' + '"status":' + str(status) + '}', headers=HEADERS, auth=AUTH)
        if c_device.status_code == 201:
            device_data = c_device.json()
            return device_data['id']
        else:
            print("创建失败,请检查是否有重名设备")
    if type_id == 1:
        c_device = requests.post(url=URL + 'sensor/', data='{"name":' + '"' + str(
            name) + '"' + ',' + '"status":' + str(status) + '}', headers=HEADERS, auth=AUTH)
        if c_device.status_code == 201:
            device_data = c_device.json()
            return device_data['id']
        else:
            print("创建失败,请检查是否有重名设备")


def delete_device(type_id, device_id):
    """Delete Device"""
    if type_id == 0:
        d_device = requests.delete(
            url=URL + 'controller/' + str(device_id), headers=HEADERS, auth=AUTH)
        return d_device.status_code
    if type_id == 1:
        d_device = requests.delete(
            url=URL + 'sensor/' + str(device_id), headers=HEADERS, auth=AUTH)
        return d_device.status_code
