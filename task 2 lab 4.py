def get_count_char(str_):
    str_ = ''.join(str_.lower().split())
    char_dict = {}

    for i in str_:
        if i.isalpha():
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1

    return char_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
