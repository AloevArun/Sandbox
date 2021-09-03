def numbered(x):
    row, numbers, cells, size = '', '', ['▓', '░'], len(str(x))
    row_size = round((size + 1) / 2)
    for i in range(0, x):
        row += cells[i % 2] * size
        numbers += ' ' * (size - len(str(i + 1))) + str(i + 1)
    print(numbers)
    for j in range(0, row_size):
        print(row)


numbered(999)
