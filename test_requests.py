import requests


def read_data():
    login = 'ArunAloev'  # str(input('Login'))
    password = '0512'  # str(input('Password:'))
    ip = '172.19.3.61'  # str(input('IP:'))
    port = str(80)  # str(input('Port:'))
    x = str(140)  # str(input('X:'))
    y = str(-100)  # str(input('Y:'))
    z = str(50)  # str(input('Zoom:'))
    return login, password, ip, port, x, y, z


def cam_set_pos(in_log, in_pass, in_ip, in_port, in_x, in_y, in_z):
    url = f'http://{in_log}:{in_pass}@{in_ip}:{in_port}/\
                                                     execute?cameraID=3&action=setposition&x={in_x}&y={in_y}&z={in_z}'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)  # feedback


cam_set_pos(*read_data())
