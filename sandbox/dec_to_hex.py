list_blyat = [1, 255, 223]


def my_hex(n):
    symbols = '0123456789abcdef'
    hex_elem = n // 16
    hex_list = [symbols[n % 16]]
    while hex_elem > 0:
        hex_list.insert(0, symbols[hex_elem % 16])
        hex_elem = hex_elem // 16
    hexed_n = '0x' + ''.join(hex_list)
    return hexed_n


def list_to_hex_format(data_list):
    hex_format_list = []
    for element in range(0, len(data_list)):
        hex_format_list.append(my_hex(data_list[element]))
    return hex_format_list


print(list_to_hex_format(list_blyat), type(list_to_hex_format(list_blyat)))
