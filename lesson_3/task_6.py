# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

symbols_upper = {
    "a": "A",
    "b": "B",
    "c": "C",
    "d": "D",
    "e": "E",
    "f": "F",
    "g": "G",
    "h": "H",
    "i": "I",
    "j": "J",
    "k": "K",
    "l": "L",
    "m": "M",
    "n": "N",
    "o": "O",
    "p": "P",
    "q": "Q",
    "r": "R",
    "s": "S",
    "t": "T",
    "u": "U",
    "v": "V",
    "w": "W",
    "x": "X",
    "y": "Y",
    "z": "Z",
}


def int_func(word):
    if word.islower():
        return word.title()
    else:
        print("строка состоит не из меленьких букв")


def int_func_2(word):
    """

    :param word:
    :return:
    """
    list_words = word.split()
    result_words = []
    result_text = " "
    for item in list_words:
        symbol = symbols_upper[item[0]]
        word_temp = f"{symbol}{item[1:]}"
        result_words.append(word_temp)

    return result_text.join(result_words)


words = "sadsa dsadsda dssaddsa dsasdasa"
print(int_func(words))
print(int_func_2(words))
