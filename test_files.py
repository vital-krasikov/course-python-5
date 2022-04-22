# тестирование функций 7 занятия

import use_functions
from main import save_current_dir

import pickle
import json
import os

# для тестирования функций сохранения логично использовать парные им функции загрузки
# и проверять, совпадает ли сохраненная информация с загруженной


def test_save_settings():
    use_functions.save_settings(1)

    f = open('settings', 'r')
    s = f.read()
    f.close()

    assert s == '11'

    use_functions.save_settings(1,2)

    f = open('settings', 'r')
    s = f.read()
    f.close()

    assert s == '212'


def test_save_account():
    f = open('test.txt', 'w')
    use_functions.save_account(150, f, 1)
    f.close()

    f = open('test.txt', 'r')
    s = f.read()

    assert s == '150\n'

    f = open('test.pickle', 'wb')
    use_functions.save_account(150, f, 2)
    f.close()

    f = open('test.pickle', 'rb')
    s = pickle.load(f)

    assert s == 150

    f = open('test.json', 'w')
    use_functions.save_account(150, f, 3)
    f.close()

    f = open('test.json', 'r')
    s = json.load(f)

    assert s == {'account': 150}


def test_save_history():
    f = open('test.txt', 'w')
    use_functions.save_history([('еда', 20), ('вода', 10)], f, 1)
    f.close()

    f = open('test.txt', 'r')
    s = f.read()

    assert s == 'еда 20\nвода 10\n'

    f = open('test.pickle', 'wb')
    use_functions.save_history([('еда', 20), ('вода', 10)], f, 2)
    f.close()

    f = open('test.pickle', 'rb')
    s = pickle.load(f)

    assert s == [('еда', 20), ('вода', 10)]

    f = open('test.json', 'w')
    use_functions.save_history([('еда', 20), ('вода', 10)], f, 3)
    f.close()

    f = open('test.json', 'r')
    s = json.load(f)

    assert s == {'history': [['еда', 20], ['вода', 10]]}


def test_save_account_history():
    f = open('test.txt', 'w')
    use_functions.save_account_history(120, [('еда', 20), ('вода', 10)], f, 1)
    f.close()

    f = open('test.txt', 'r')
    s = f.read()

    assert s == '120\nеда 20\nвода 10\n'

    f = open('test.pickle', 'wb')
    use_functions.save_account_history(120, [('еда', 20), ('вода', 10)], f, 2)
    f.close()

    f = open('test.pickle', 'rb')
    s1 = pickle.load(f)
    s2 = pickle.load(f)

    assert (s1, s2) == (120, [('еда', 20), ('вода', 10)])

    f = open('test.json', 'w')
    use_functions.save_account_history(120, [('еда', 20), ('вода', 10)], f, 3)
    f.close()

    f = open('test.json', 'r')
    s = json.load(f)

    assert s == {'account': 120, 'history': [['еда', 20], ['вода', 10]]}

#  тестирование функций загрузки


def test_load_settings():
    f = open('settings', 'w')
    f.write('12')
    f.close()

    acc, history = use_functions.load_settings()
    assert acc == 2 and history is None

    f = open('settings', 'w')
    f.write('212')
    f.close()

    acc, history = use_functions.load_settings()
    assert acc == 1 and history == 2


def test_load_account():
    f = open('test.txt', 'w')
    f.write('150')
    f.close()

    f = open('test.txt', 'r')
    acc = use_functions.load_account(f, 1)
    f.close()
    assert acc == 150

    f = open('test.pickle', 'wb')
    pickle.dump(150, f)
    f.close()

    f = open('test.pickle', 'rb')
    acc = use_functions.load_account(f, 2)
    f.close()
    assert acc == 150

    f = open('test.json', 'w')
    json.dump({'account': 150}, f)
    f.close()

    f = open('test.json', 'r')
    acc = use_functions.load_account(f, 3)
    f.close()
    assert acc == 150


def test_load_history():
    f = open('test.txt', 'w')
    f.write('еда 20\nвода 10\n')
    f.close()

    f = open('test.txt', 'r')
    history = use_functions.load_history(f, 1)
    f.close()
    assert history == [['еда', 20], ['вода', 10]]

    f = open('test.pickle', 'wb')
    pickle.dump([['еда', 20], ['вода', 10]], f)
    f.close()

    f = open('test.pickle', 'rb')
    history = use_functions.load_history(f, 2)
    f.close()
    assert history == [['еда', 20], ['вода', 10]]

    f = open('test.json', 'w')
    json.dump({'history': [['еда', 20], ['вода', 10]]}, f)
    f.close()

    f = open('test.json', 'r')
    history = use_functions.load_history(f, 3)
    f.close()
    assert history == [['еда', 20], ['вода', 10]]


def test_load_account_history():
    f = open('test.txt', 'w')
    f.write('120\nеда 20\nвода 10\n')
    f.close()

    f = open('test.txt', 'r')
    acc, history = use_functions.load_account_history(f, 1)
    f.close()
    assert (acc, history) == (120, [['еда', 20], ['вода', 10]])

    f = open('test.pickle', 'wb')
    pickle.dump(120, f)
    pickle.dump([['еда', 20], ['вода', 10]], f)
    f.close()

    f = open('test.pickle', 'rb')
    acc, history = use_functions.load_account_history(f, 2)
    f.close()
    assert (acc, history) == (120, [['еда', 20], ['вода', 10]])

    f = open('test.json', 'w')
    json.dump({'account': 120, 'history': [['еда', 20], ['вода', 10]]}, f)
    f.close()

    f = open('test.json', 'r')
    acc, history = use_functions.load_account_history(f, 3)
    f.close()
    assert (acc, history) == (120, [['еда', 20], ['вода', 10]])

# и, наконец, save_current_dir


def test_save_current_dir():
    save_current_dir('test.txt')
    files = set()
    dirs = set()
    for item in os.scandir():
        if item.is_file():
            files.add(item.name)
        else:
            dirs.add(item.name)
    f = open('test.txt', 'r')
    s = f.readline()
    assert set(s.strip().replace('files: ', '').replace(';', '').split(' ')) == files

    s = f.readline()
    assert set(s.strip().replace('dirs: ', '').replace(';', '').split(' ')) == dirs
