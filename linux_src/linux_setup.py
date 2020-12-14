#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess
import shutil

border = '============='

print 'Добро пожаловать в установку приложения Карточки v.0.1 for Linux.'
usrName = subprocess.check_output('whoami')
if usrName[:-1] != 'root':
    print '''Ошибка! Обратите внимание на то, что установщик должен быть запущен
    от имени пользователя root.'''
else:
    print border
    print 'Выберите свой пакетный менеджер для продолжения.'
    print '[1] apt (Debian/Ubuntu/Mint/Deepin/...)'
    print '[2] dnf (RedHat/Fedora/CentOS)'
    print '[3] pacman (Arch Linux)'
    print '[4] zypper (openSUSE)'
    print '[5] portage (Gentoo)'

    pkgManChoice = input()
    if pkgManChoice == 1:
        os.system('apt update')
        os.system('apt install -y python3 python3-pip')
    elif pkgManChoice == 2:
        os.system('dnf install python3 python3-pip')
    elif pkgManChoice == 3:
        os.system('pacman -Syu python3 python3-pip')
    elif pkgManChoice == 4:
        os.system('zypper in python3 python3-pip')
    elif pkgManChoice == 5:
        os.system('emerge python3 python3-pip')

    os.system('pip3 install PyQt5 xlwt python-docx')
    os.system('clear')

    print border
    print 'Укажите путь, куда нужно установить программу [/opt/thm_flashcards/]: '
    installPath = raw_input()
    if not(bool(installPath)):
        installPath = '/opt/thm_flashcards/'
    else:
        installPath = installPath if installPath[:-1] == '/' else installPath + '/'


    while ' ' in installPath:
        print 'Нельзя использовать пробелы и спец. значки [/opt/thm_flashcards/]: '
        installPath = raw_input()
        if not(bool(installPath)):
            installPath = '/opt/thm_flashcards/'
        else:
            installPath = installPath if installPath[:-1] == '/' else installPath + '/'


    print 'Удаление остатков старой инсталляции...'
    if os.path.exists(installPath):
        if os.path.exists(installPath + 'user_data/'):
            if len(os.listdir(installPath + 'user_data/')) != 0:
                print 'Вы уверены, что хотите удалить сохраненные Вами стопки карт? (y/n): '
                ans = raw_input()
                if ans == 'y':
                    shutil.rmtree(installPath)
                else:
                    print('Скопируйте файлы из ' + installPath + 'user_data/ и запустите установку снова.')
                    exit()
            else:
                shutil.rmtree(installPath)
        else:
            shutil.rmtree(installPath)


    print 'Копирование файлов программы...'
    os.mkdir(installPath)

    os.mkdir(installPath + 'user_data')
    os.mkdir(installPath + 'tmp')
    os.mkdir(installPath + 'about_window')

    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            currentFile = os.path.join(root, file)
            shutil.copyfile(currentFile, installPath + file)
            print('Скопировано: ' + currentFile)

    os.system('mv ' + installPath + 'myemail.png ' + installPath + 'about_window/myemail.png')
    os.system('mv ' + installPath + 'name.png ' + installPath + 'about_window/name.png')
    os.system('mv ' + installPath + 'person.png ' + installPath + 'about_window/person.png')
    os.system('mv ' + installPath + 'website.png ' + installPath + 'about_window/website.png')
    os.system('mv ' + installPath + 'writtenin.png ' + installPath + 'about_window/writtenin.png')

    os.system('clear')

    print 'Установка шрифта...'
    if not('ubuntu' in os.listdir('/usr/share/fonts/truetype/') or 'Ubuntu' in os.listdir('/usr/share/fonts/truetype/')):
        shutil.copyfile('Ubuntu-R.ttf', '/usr/share/fonts/truetype/Ubuntu-R.ttf')
    print 'Готово.'

    print 'Установка прав доступа...'
    os.system('chmod 777 ' + installPath)
    os.system('chmod 777 ' + installPath + '*')
    print 'Готово.'

    print 'Создание файла *.desktop...'
    caption = '[Desktop Entry]'
    name = 'Name=Карточки'
    comment = 'Comment=Изучение материала в форме карточек.'
    type = 'Type=Application'
    terminal = 'Terminal=false'
    icon = 'Icon=' + installPath + 'icon.png'
    path = 'Path=' + installPath
    myExec = 'Exec=python3 ' + installPath + 'main.pyw'
    cat = 'Categories=Game'

    desktopFileWriter = open('/usr/share/applications/thm_flashcards.desktop', 'w')
    desktopFileWriter.write(caption + '\n')
    desktopFileWriter.write(name + '\n')
    desktopFileWriter.write(comment + '\n')
    desktopFileWriter.write(type + '\n')
    desktopFileWriter.write(terminal + '\n')
    desktopFileWriter.write(icon + '\n')
    desktopFileWriter.write(path + '\n')
    desktopFileWriter.write(myExec + '\n')
    desktopFileWriter.write(cat + '\n')
    desktopFileWriter.close()

    print 'Готово.'

    print 'Установка успешно завершена!'
    print 'Вы можете запустить программу из главного меню своего DE, категория Игры'
