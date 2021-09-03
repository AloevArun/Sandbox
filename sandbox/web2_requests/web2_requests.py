import json
import socket

import web2_requests


class UserData:
    """Класс пользовательских данных(логин, пароль, IP, порт)"""

    def __init__(self):
        self.ports = dict(web1=80, web2=8085, auto_rest=8091, rest_ip='127.0.0.1')
        self.current_ip = socket.gethostbyname(socket.gethostname())
        self.current_host = socket.gethostname()
        self.auth = ('user', 'pass')
        self.host = f'{self.current_ip}:{self.ports.get("port")}'

    def set_data(self):  # собираем иноформацию
        pass

    def get_data(self):
        return self.auth, self.host


class Web2Request(UserData):
    """Класс запросов на объект 'Веб-Сервер 2.0'"""
    def get_all_objects_on_server(self, auth, host):
        self.url = f'http://{host}/web2/secure/configuration'
        payload = {}
        headers = {}
        response = web2_requests.request("GET", url, headers=headers, data=payload, auth=auth)
        parsed = json.loads(response.content)
        for dict_n in parsed:
            print('\n')
            for item in dict_n.items():
                print(item)


def set_xyz(self):
    """Класс координат для камеры"""
    x = str(140)  # str(input('X:'))
    y = str(-100)  # str(input('Y:'))
    z = str(50)  # str(input('Zoom:'))
    return x, y, z


def cam_set_pos(self, auth, host, x, y, z):  # наведение лазера смерти через http запрос
    url = f'http://{host}/execute?cameraID=3&action=setposition&x={x}&y={y}&z={z}'
    payload = {}
    headers = {}
    response = web2_requests.request("GET", url, headers=headers, data=payload, auth=auth)
    print(response)
