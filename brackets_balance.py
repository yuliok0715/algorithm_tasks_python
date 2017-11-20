"""Дана строка, содержащая скобки ( ) и { }.
Скобочное выражение считается правильным, если:
1. для каждой открывающей скобки справа от нее есть закрывающая скобка и наоборот.
2. соответствующие пары скобок разным типов правильно вложены друг в друга.
Длина строки не больше 128 символов.
Написать функцию, ктр проверит баланс скобок в заданной строке."""
import re
def brackets_balance(input_string):
    if (input_string.count("(") != input_string.count(")"))\
            or input_string.count("{") != input_string.count("}"):
        return False
    new_string = input_string
    while re.search("(\([^\(\)\{\}]*\))+|(\{[^\(\)\{\}]*\})+", new_string) and new_string:#пока в строке есть парные
        #  скобки и между ними что-либо и она не пустая
        new_string = re.sub("(\([^\(\)\{\}]*\))+|(\{[^\(\)\{\}]*\})+", "", new_string)#удаляем вся рядом стоящие скобки
    return False if new_string else True#если после этой процедуры
    #  получаем пустую строку - все ок
#test
print(brackets_balance("({(lolik){}ytb(nhy)})()"))
print(brackets_balance("({(vse ravno}){})"))