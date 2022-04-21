import os
from shutil import copy
from main import author_info
from victory import date_to_text
from use_functions import add_purchase

# тесты чистых функций


def test_author_info():
    assert author_info() == 'Создатель программы: Красиков Виталий Александрович, в рамках задания на курсе Python+'


def test_date_to_text():
    assert date_to_text('01.01.1999') == 'первое января 1999 года'
    assert date_to_text('26.08.1986') == 'двадцать шестое августа 1986 года'
    assert date_to_text('10.11.1991') == 'десятое ноября 1991 года'
    assert date_to_text('17.09.2020') == 'семнадцатое сентября 2020 года'


def test_add_purchase():
    assert add_purchase([], 120, 'еда', 70) == ([('еда', 70)], 50)
    assert add_purchase([('еда', 70)], 50, 'вода', 20) == ([('еда', 70), ('вода', 20)], 30)
    assert add_purchase([('еда', 70), ('вода', 20)], 30, 'метро', 30) == ([('еда', 70), ('вода', 20), ('метро', 30)], 0)

# тесты "грязных" функций


def test_mkdir():
    # не сработает, если уже существует непустая директория с таким именем в текущей директории
    if 'input' in os.listdir():
        for item in os.scandir('./input'):
            if item.is_file():
                os.remove('./input/'+item.name)
            else:
                os.rmdir('./input/'+item.name)
        os.rmdir('input')
    os.mkdir('input')
    assert 'input' in os.listdir()


def test_remove():
    if '1.txt' in os.listdir():
        os.remove('1.txt')
        assert not('1.txt' in os.listdir())


def test_rmdir():
    if 'input' in os.listdir():
        os.rmdir('input')
        assert not('input' in os.listdir())


def test_copy():
    if not('1.txt' in os.listdir()):
        open('1.txt', 'w+')
    if not('input' in os.listdir()):
        os.mkdir('input')
    copy('1.txt', 'input')
    assert '1.txt' in os.listdir('./input')



