# ▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▀ ▔ ▏ ▎ ▍ ▌ ▋ ▊ ▉ ▐ ▕ ▖ ▗ ▘ ▙ ▚ ▛ ▜ ▝ ▞ ▟ ░ ▒ ▓
#  ╌ ╍ ╎ ╏ ╭ ╮ ╯ ╰ ╱ ╲ ╳ ╴ ╵ ╶ ╷ ╸ ╹ ╺ ╻ ╼ ╽ ╾ ╿
# ┌ └ ┐ ┘ ┼ ┬ ┴ ├ ┤ ─ │ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪

print('Вводимые числа должны быть меньше 100!')

y, x = 2, 2   # int(input('Введите количество строк:')), int(input('Введите количество столбцов:'))

digits = '0123456789'
alphabet = 'ABCDEFGHIJ'


def print_desk(lines, column):
    if lines < 100 and column < 100:  # проверка на границы < 100

        # Рассчет и запись данных о доске
        size_of = ('║ Размер шахматной доски: ' + str(lines) + ' X ' + str(column) + '. ║')
        count_of = ('║ Количество ячеек: ' + str(lines * column) + '.')
        if lines == column:
            q_or_r = '║ Доска - квадратная.'
        else:
            q_or_r = '║ Доска - прямоугольная.'
        head = ('╔════' + ('═══' * (column + 1)) + '╗')

        print(head)  # Верхняя грань доски

        # Нумерация столбцов сверху
        print('║   ', end='')
        for n in range(1, column + 1):
            print(' ', digits[n // 10] + digits[n % 10], sep='', end='')
        print('    ║')

        #  игровая область
        for i in range(1, lines + 1):  # Цикл по строкам
            print('║', alphabet[(i - 1) // 10] + alphabet[(i - 1) % 10], end=' ')  # Левая грань строки и символы
            for j in range(1, column + 1):  # Цикл вывода одной строки
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):  # Если i и J оба четные,или оба нечетны
                    print('▓▓ ', end='')
                else:
                    print('░░ ', end='')
            print(alphabet[(i - 1) // 10] + alphabet[(i - 1) % 10], '║')  # Правая грань строки и символы
        print('║   ', end='')

        # Нумерация столбцов снизу
        for m in range(1, column + 1):
            print(' ', digits[m // 10] + digits[m % 10], sep='', end='')
        # Граница между 2мя блоками
        if len(head) > len(size_of):  # Если верхний блок шире чем нижний: ╠══╦══╝
            print('    ║\n╠═', '═' * (len(size_of) - 3) + '╦', '═' * ((len(head)) - len(size_of) - 1), '╝\n', sep='',
                  end='')

        elif len(head) < len(size_of):  # Если верхний блок уже чем нижний: ╠══╩══╗
            print('    ║\n╠═', '═' * (len(head) - 3), '╩', '═' * (len(size_of) - len(head) - 1) + '╗\n', sep='', end='')

        else:  # Если равны: '╠═════╣'
            print('    ║\n╠═', '═' * (len(head) - 3), '╣', sep='', end='')

        # Вывод информации и оформление нижнего блока
        print(size_of)  # Размер
        print(count_of, ' ' * ((len(size_of) - len(count_of)) - 1), '║', sep='')  # Количество
        print(q_or_r, ' ' * ((len(size_of) - len(q_or_r)) - 1), '║', sep='')  # Форма
        # Нижняя грань нижнего блока
        print('╚', '═' * (len(size_of) - 2) + '╝', sep='')
        return 0
    else:
        print('Вы ввели число больше 99!!')

        return 0


print_desk(y, x)
