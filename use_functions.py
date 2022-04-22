"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы
"""


import pickle
import json

SAVE_OPTIONS = {1: 'txt', 2: 'pickle', 3: 'json'}


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper


@counter
def save_settings(account_settings, history_settings=None):
    """
    Функция сохранения настроек сохранения в файл
    :param account_settings: настройки сохранения данных счета
    :param history_settings: настройки сохранения данных истории покупок, если он равен None, то данные счета и истории
    сохраняются в 1 файл
    :return:
    """
    f = open('settings', 'w')
    f.write('1'+str(account_settings) if history_settings is None else '2'+str(account_settings)+str(history_settings))
    f.close()


@counter
def load_settings():
    """
    Функция загрузки настроек сохранения из файла
    :return: настройки сохранения счета и истории покупок, если данные сохраняются в одном файле, вместо настроек
    для истории покупок возвращает None
    """
    f = open('settings', 'r')
    try:
        n = int(f.read(1))
    except ValueError:
        n = 1
    try:
        account_settings = int(f.read(1))
    except ValueError:
        account_settings = 1
    if n == 2:
        try:
            history_settings = int(f.read(1))
        except ValueError:
            history_settings = 1
    f.close()

    return (account_settings, history_settings) if n == 2 else (account_settings, None)


@counter
def save_account(account, f, file_type):
    """
    Функция сохранения данных счета в файл
    :param account: данные счета
    :param f: ссылка на файл
    :param file_type: тип файла - число
    :return:
    """
    if file_type == 1:  # текст
        f.write(str(account)+'\n')
    elif file_type == 2:  # pickle
        pickle.dump(account, f)
    else:  # json
        json.dump({'account': account}, f)


@counter
def load_account(f, file_type):
    """
     Функция загрузки данных счета из файла
     :param f: ссылка на файл
     :param file_type: тип файла - число
     :return: данные счета
     """
    if file_type == 1:  # текст
        account = int(f.readline())
    elif file_type == 2:  # pickle
        account = int(pickle.load(f))
    else:  # json
        account = int(json.load(f)['account'])
    return account


@counter
def save_history(history, f, file_type):
    """
     Функция сохранения истории покупок в файл
     :param history: данные истории покупок
     :param f: ссылка на файл
     :param file_type: тип файла - число
     :return:
     """
    if file_type == 1:  # текст
        for i in history:
            f.write(str(i[0])+' '+str(i[1])+'\n')
    elif file_type == 2:  # pickle
        pickle.dump(history, f)
    else:  # json
        json.dump({'history': history}, f)


@counter
def load_history(f, file_type):
    """
     Функция загрузки истории продаж из файла
     :param f: ссылка на файл
     :param file_type: тип файла - число
     :return: данные истории покупок
     """
    if file_type == 1:  # текст
        history = []
        while True:
            s = f.readline()
            if s == '':
                break
            else:
                s1 = s.strip().split(' ')
                history.append([s1[0], int(s1[1])])
    elif file_type == 2:  # pickle
        history = pickle.load(f)
    else:  # json
        history = json.load(f)['history']
    return history


@counter
def save_account_history(account, history, f, file_type):
    """
    Функция сохранения сразу счета и истории покупок в файл
    необходимо, поскольку при сохранении json в один файл работать будет не просто
    как вызов save_account и save_history по очереди
    :param account: данные счета
    :param history: данные истории покупок
    :param f: ссылка на файл
    :param file_type: тип файла - число
    :return:
    """
    if file_type == 3:
        json.dump({'account': account, 'history': history}, f)
    else:
        save_account(account, f, file_type)
        save_history(history, f, file_type)


@counter
def load_account_history(f, file_type):
    """
    Функция сохранения сразу счета и истории покупок в файл
    необходимо, поскольку при сохранении json в один файл работать будет не просто
    как вызов save_account и save_history по очереди
    :param f: ссылка на файл
    :param file_type: тип файла - число
    :return: данные счета, данные истории покупок
    """
    if file_type == 3:
        result = json.load(f)
        return int(result['account']), result['history']
    else:
        return load_account(f, file_type), load_history(f, file_type)


@counter
def add_purchase(history, account, name, s):
    history.append([name, s])
    account -= s
    return history, account


@counter
def my_account():

    history = []

    account_settings, history_settings = load_settings()
    different_files = (False if history_settings is None else True)

    if different_files:
        try:
            mode = ('rb' if account_settings == 2 else 'r')
            f = open('account_data.'+SAVE_OPTIONS[account_settings], mode)
        except OSError:
            print('файл счета не найден! количество денег на счету равно 0')
            account = 0
        else:
            try:
                account = load_account(f, account_settings)
            except ValueError:
                print('данные в файле счета имеют неверный формат! количество денег на счету равно 0')
                account = 0

        try:
            mode = ('rb' if history_settings == 2 else 'r')
            f = open('history_data.'+SAVE_OPTIONS[history_settings], mode)
        except OSError:
            print('файл истории покупок не найден! история покупок пуста')
            history = []
        else:
            try:
                history = load_history(f, history_settings)
            except ValueError:
                print('данные в файле истории покупок имеют неверный формат! история покупок пуста')
                history = []
    else:
        try:
            mode = ('rb' if account_settings == 2 else 'r')
            f = open('data.'+SAVE_OPTIONS[account_settings], mode)
        except OSError:
            print('файл счета не найден! количество денег на счету равно 0')
            account = 0
        else:
            try:
                account, history = load_account_history(f, account_settings)
            except ValueError:
                print('данные в файле счета имеют неверный формат! количество денег на счету равно 0')
                account = 0

    while True:
        print('0. настройка сохранения/загрузки данных')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '0':
            choice2 = input('Организовать хранение данных счета и истории покупок в одном файле? (y/n) ')
            if choice2 == 'y':
                print('Данные счета и истории покупок будут храниться в одном файле!')
                different_files = False
            else:
                print('Данные счета и истории покупок будут храниться в разных файлах!')
                different_files = True
            account_settings = 0
            while account_settings not in (1, 2, 3):
                print('Выберите вариант сохранения данных счета:' if different_files else 'Выберите вариант сохранения данных:')
                print('1. текст\n2. pickle\n3. json')
                try:
                    account_settings = int(input())
                except ValueError:
                    account_settings = 0
                print('Выберите вариант от 1 до 3!' if account_settings not in (1, 2, 3)
                      else 'Данные будут сохранены в формате '+SAVE_OPTIONS[account_settings]+'!')

            if different_files:
                history_settings = 0
                while history_settings not in (1, 2, 3):
                    print('Выберите вариант сохранения данных истории покупок:')
                    print('1. текст\n2. pickle\n3. json')
                    try:
                        history_settings = int(input())
                    except ValueError:
                        history_settings = 0
                    print('Выберите вариант от 1 до 3!' if history_settings not in (1, 2, 3)
                          else 'Данные будут сохранены в формате ' + SAVE_OPTIONS[history_settings] + '!')
                save_settings(account_settings, history_settings)
            else:
                save_settings(account_settings)
        elif choice == '1':
            account += int(input('Введите сумму пополнения: '))
        elif choice == '2':
            s = int(input('Введите сумму покупки: '))
            if s <= account:
                name = input('Введите название товара: ')
                history, account = add_purchase(history, account, name, s)
            else:
                print('Не хватает средств на счете для покупки!')
        elif choice == '3':
            for i in history:
                print(i[0]+': '+str(i[1]))
        elif choice == '4':
            if different_files:
                mode = ('wb' if account_settings == 2 else 'w')

                f = open('account_data.'+SAVE_OPTIONS[account_settings], mode)
                save_account(account, f, account_settings)
                f.close()

                mode = ('wb' if history_settings == 2 else 'w')

                f = open('history_data.'+SAVE_OPTIONS[history_settings], mode)
                save_history(history, f, history_settings)
                f.close()
            else:
                mode = ('wb' if account_settings == 2 else 'w')

                f = open('data.'+SAVE_OPTIONS[account_settings], mode)
                save_account_history(account, history, f, account_settings)
                f.close()
            break
        else:
            print('Неверный пункт меню')


if __name__ == "__main__":
    my_account()