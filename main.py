import os
import sys
import shutil
import victory
import use_functions


def print_menu():
    print('Текущая директория: '+os.getcwd())
    print('1. Создать папку')
    print('2. Удалить файл/папку')
    print('3. Копировать файл/папку')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Просмотр папок в рабочей директории')
    print('6. Просмотр файлов в рабочей директории')
    print('7. Просмотр информации об операционной системе')
    print('8. Просмотр информации о создателе программы')
    print('9. Игра Викторина')
    print('10. Программа Мой банковский счет')
    print('11. Смена рабочей директории')
    print('12. Сохранить содержимое рабочей директории в файл')
    print('13. Выход')

    return None


def author_info():
    return 'Создатель программы: Красиков Виталий Александрович, в рамках задания на курсе Python+'


def save_current_dir(file_name):
    """
    сохранение данных о содержимом текущей директории в текстовый файл
    :param file_name: имя файла
    :return:
    """
    f = open(file_name, 'w')
    files = 'files: '
    dirs = 'dirs: '
    for item in os.scandir():
        if item.is_file():
            files += item.name + '; '
        else:
            dirs += item.name + '; '
    f.write(files+'\n'+dirs)


def main():
    option = 1
    while option != 13:

        print_menu()

        is_file = {True: 'file', False: 'dir'}

        try:
            option = int(input('Введите вариант: '))
            if option == 1:
                name = input('Введите имя директории: ')
                os.mkdir(name)
                print('Директория ' + name + ' создана!')
            elif option == 2:
                name = input('Введите имя файла/директории: ')
                os.remove(name)
                print('Файл ' + name + ' удален!')
            elif option == 3:
                name = input('Введите имя файла/директории: ')
                name2 = input('Куда копировать? ')
                shutil.copy(name, name2)
                print('Файл ' + name + ' скопирован!')
            elif option == 4:
                for item in os.scandir(os.getcwd()):
                    print(item.name + '\t' + is_file[item.is_file()])
            elif option == 5:
                for item in os.scandir(os.getcwd()):
                    if not item.is_file():
                        print(item.name)
            elif option == 6:
                for item in os.scandir(os.getcwd()):
                    if item.is_file():
                        print(item.name)
            elif option == 7:
                print('Операционная система: ', sys.platform, '(', os.name, ')')
            elif option == 8:
                print(author_info())
            elif option == 9:
                victory.start_quiz()
            elif option == 10:
                use_functions.my_account()
            elif option == 11:
                os.chdir(input('Введите путь к новой рабочей папке: '))
            elif option == 12:
                save_current_dir('listdir.txt')
        except ValueError:
            print('Введено не число! Попробуйте еще раз')
        except OSError:
            if option == 1:
                print('Директория с таким именем уже существует!')
            else:
                if len(os.listdir(name)) == 0:
                    os.rmdir(name)
                    print('Директория ' + name + ' удалена!')
                else:
                    print('Директория не пуста, сначала удалите из нее все файлы')
        finally:
            input('Нажмите Enter..')


if __name__ == "__main__":
    main()

