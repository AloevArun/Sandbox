with open('text.txt', 'r', encoding='UTF-8') as text_file:
    coding_text = text_file.readline()

coding_result = ''
coding_list = list(coding_text)

print(coding_text)  # test
print(coding_list)  # test

with open('new_text.txt', 'w', encoding='UTF-8') as new_text_file:
    new_text_file.write(str(coding_result))
