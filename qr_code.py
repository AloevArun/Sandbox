import qrcode
import random
import os

path = 'QR'

if os.path.exists('QR'):
    pass
else:
    os.mkdir('QR')


def qr_code_from_num(str_len, save_path, count):
    ls = list('123456789')
    for i in range(count):
        sid = ''.join([random.choice(ls) for x in range(str_len)])
        filename = f"{sid}.png"
        img = qrcode.make(sid)
        img.save(f'{save_path}/{filename}')


def qr_code_from_symb(str_len, save_path, count):
    str1 = '123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    ls = list(str1 + str2 + str3)
    for i in range(count):
        random.shuffle(ls)
        sid = ''.join([random.choice(ls) for x in range(str_len)])
        filename = f"{sid}.png"
        img = qrcode.make(sid)
        img.save(f'{save_path}/{filename}')


print('Генератор QR-кодов 1.0.0')
print('В изображении случайно кодируется имя файла изображения.')
flag = True
while flag:
    alg = input('Выберите тип генерации(int/str):\n"int" - только числа\n"str" - числа и символы\n~:')
    if alg == 'int' or alg == 'str':
        length = int(input('Количество символов кодирования:'))
        file_count = (int(input('Количество файлов:')))
        print('Процесс запущен, дождитесь окончания...')

        if alg == 'int':
            qr_code_from_num(length, path, file_count)
            flag = False
            print('Генерация завершена!')
            os.system(f'start {os.path.realpath(path)}')

        if alg == 'str':
            qr_code_from_symb(length, path, file_count)
            flag = False
            print('Генерация завершена!')
            os.system(f'start {os.path.realpath(path)}')
    else:
        print('Введите "int" или "str"!')
