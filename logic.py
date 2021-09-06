# import nltk
from nltk import word_tokenize
from setuptools._vendor.ordered_set import is_iterable


def flatten(l):
    """
    Преобразование из списка списков в список
    :param l: список списков
    :return: список
    """
    if is_iterable(l):
        flat = []
        for i in l:
            if is_iterable(i):
                flat.extend(flatten(i))
            else:
                flat.append(i)
        return flat
    return [l]


def open_file(filename):
    """
    Чтение данных с текстового файла
    :param filename: текстовый файл
    :return: список, разбитый на предложения
    """
    with open(filename, encoding='utf-8') as file:
        # nltk.download('punkt')
        a = [word_tokenize(i) for i in file.readlines()]
        return flatten(a)


def is_find(obj_file, word, quantity):
    find = False
    count = 0
    for word_file in obj_file:
        if word_file == word:
            find = True
            count += 1

        if count == int(quantity):
            break
        else:
            find = False
    return find
