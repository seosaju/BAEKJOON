cryptogram = input().replace(" ", "").upper()
plain_text = list(input().replace(" ", "").upper())
alphabet = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
crypto_list = list()

for i in cryptogram:
    if i not in crypto_list:
        crypto_list.append(i)

for i in alphabet:
    if i not in crypto_list:
        crypto_list.append(i)

i = 0
while i < len(plain_text):
    try:
        if plain_text[i] == plain_text[i + 1]:
            plain_text.insert(i + 1, 'X')
    except IndexError:
        pass
    finally:
        i += 2

if len(plain_text) % 2:
    plain_text.append('X')

word_list = list()
for i in range(0, len(plain_text), 2):
    word_list.append(f'{plain_text[i]}{plain_text[i + 1]}')

for index, text in enumerate(word_list):
    i, j = text[0], text[1]
    if i == 'Q':
        i = 'Z'
    if j == 'Q':
        j = 'Z'
    i_index = crypto_list.index(i)
    j_index = crypto_list.index(j)
    i_x, i_y = i_index // 5, i_index % 5
    j_x, j_y = j_index // 5, j_index % 5

    if i_x == j_x:
        i = crypto_list[(i_x * 5) + ((i_y + 1) % 5)]
        j = crypto_list[(j_x * 5) + ((j_y + 1) % 5)]
        word_list[index] = f'{i}{j}'
    elif i_y == j_y:
        i = crypto_list[((i_x * 5 + 5) + i_y) % 25]
        j = crypto_list[((j_x * 5 + 5) + j_y) % 25]
        word_list[index] = f'{i}{j}'
    else:
        i = crypto_list[((i_x * 5) + j_y) % 25]
        j = crypto_list[((j_x * 5) + i_y) % 25]
        word_list[index] = f'{i}{j}'

print("".join(word_list))
