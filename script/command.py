from function import *

def comand():
    str = input("Введите команду: ")

    # Разделение строки на слова
    words = str.split(", ") #список слов

    if 'пересчитать' in words:
        if words[1] == 'буквы':
            print(code_string_p_a)
        else:
            print(code_string_p_l)
        if words[1] == 'вариации':
            if words[2] == 'различны':
                print(code_string_v_pr)
            if words[2] == 'повторяются':
                print(code_string_v_per)

    if 'создать' in  words:
        if words[1] == 'список':
            print(spisok(words[2], words[3]))

    if 'удалить' in  words:
        if words[1] == 'символ':
            print(code_string_del)
        if words[1] == 'символы':
            print(code_string_del_all)

    if 'программа' in  words:
        if words[1] == 'калькулятор':
            print(code_string_calc)
        if words[1] == 'окно':
            if len(words) >= 3:
                if words[2] == "базовые виджеты":
                    print(code_string_basic_vid)
            else: print(code_string_window)

    if 'добавить' in  words: 
        if words[1] == 'команда':
            your_modul = input()
            add_command(your_modul)


    if 'использовать' in  words: 
        if words[1] == 'f':
            print(code_string_f)