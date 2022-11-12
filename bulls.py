import random


def get_dict_words(): # возвращаем сюда готовый словарь

    result = {x: [] for x in range(4,11)}
    with open("dictionary.txt", "r", encoding="utf-8") as file:
        data = file.read()
        words_list = data.split()
        for word in words_list:
            if 4 <= len(word) <= 10:
                result[len(word)].append(word)

    return result

# def  get_random_word(key,dict_w):  #### Генерируем слово по длине
#
#     word = random.choice(dict_w[key])
#     return word
#
# ################### Начало игры / ввод данных / генерация слова /
# dict_words = get_dict_words()

# num = int(input("Введите количество букв в слове от 4 до 10 ==>"))
# if 4 <= num <= 10:
#     word = get_random_word(num,dict_words)
# else:
#     print("Введено не верное значение")
#     exit

# print(word)
# print(f"Слово состоит из {len(word)} букв ")
# insert = ""
# slovo = list(('*'*len(word)))
# print(slovo)

######################### Игра
# while insert != word:
#     cows = []
#     insert = input('Введите слово ==>')
#     if insert not in dict_words[num]:
#         print("Введите существующее слово")
#         continue
#     for index, letter in enumerate(word):
#         if letter == insert[index]:
#             slovo[index] = letter
#         if letter in insert and letter not in slovo:
#             cows.append(letter)
#     if word == insert:
#         print("Угадал")
#     else:
#         print(slovo)
#         if len(cows) >= 1:
#             print(f"Так же вы нашли эти коровки - {cows}")
