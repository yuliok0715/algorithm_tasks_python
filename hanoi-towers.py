"""Даны три стержня A, B, C, на один из которых нанизаны N колец, причём кольца
 отличаются размером и лежат меньшее на большем.
Задача состоит в том, чтобы перенести пирамиду из N колец за наименьшее число
 ходов на другой стержень. За один раз разрешается
переносить только одно кольцо, причём нельзя класть большее кольцо на меньшее.
Напишите функцию разбора для N колец. Функция должна выводить на экран каждый шаг."""


def hanoi(n, a, b, c):
    """
    n:  количество колец
    a:  имя первого стержня
    b:  имя второго стержня
    c:  имя третьего стержня
	переносим эн колец из первого на третий, используя второй как промежуточный
    """
    if n != 0: 
        hanoi(n - 1, a, c, b)#n - 1 кольцо из A в B
        print('Перенести кольцо из', a, 'в', c)#одно кольцо из A в C
        hanoi(n - 1, b, a, c)#n - 1 кольцо из B в С


#test
hanoi(3, 'A', 'B', 'C')
