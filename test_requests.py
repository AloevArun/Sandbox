import requests
import json
import socket

ports = dict(web1=80, web2=8085, auto_rest=8091, rest_ip='127.0.0.1')


def get_ip():
    ip = socket.gethostbyname(socket.gethostname())
    print(f'[{socket.gethostname()} | {ip}]', end='')
    return ip


def set_data(login='user', password='pass', ip=get_ip(), port=ports.get('web2')):  # собираем иноформацию
    auth = f'{login}:{password}'
    host = f'{ip}:{port}'
    return auth, host


def get_all_objects_on_server(auth, host):
    url = f'http://{auth}@{host}/web2/secure/configuration'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    parsed = json.loads(response.content)
    for dict_n in parsed:
        print('\n')
        for item in dict_n.items():
            print(item)


def set_xyz():
    x = str(140)  # str(input('X:'))
    y = str(-100)  # str(input('Y:'))
    z = str(50)  # str(input('Zoom:'))
    return x, y, z


get_all_objects_on_server(*set_data())


# def cam_set_pos(auth, host, x, y, z):  # наведение лазера смерти через http запрос
#     url = f'http://{auth}@{host}/\
#                                                      execute?cameraID=3&action=setposition&x={x}&y={y}&z={z}'
#     payload = {}
#     headers = {}
#     response = requests.request("GET", url, headers=headers, data=payload)
#     print(response)  # feedback
