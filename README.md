# Дорога к Хакатону
Наша дорога к Хакатону
## Список Героев
* Владимир Крохин
* Артем Каримуллин
* Дмитрий Удилов
* Варвара Козлова
* Александра Дерябина
## Как установить
### Установка виртуального окружения и зависимостей, создание бд (если ее нет)
1.  С помощью встроенного терминала (integrated terminal)/командной строки (**Ctrl+J**) установите виртуальное окружение (venv):  
Linux/Windows: `python -m venv .venv`  
Важно, чтобы виртуальное окружение было установлено в папку с проектом. Если у вас внутри папки появилась папка .venv, значит все прошло нормально. Если ругается, то вместо "python попробуйте написать "python3". Гугл вам в помощь
2. Активируйте виртуальное окружение (делать из папки проекта):  
Linux: `source .venv/bin/activate`  
Windows: `./.venv/Scripts/activate`  
Признак того, что все хорошо: в консоли сначала отображается (.venv).  
**Активировать виртуальное окружение придется каждый раз, когда вы приступаете к работе с проектом!**
3. Установите все зависимости при помощи пакетного менеджера Питона (pip):  
Linux/Windows: `pip install -r requirements.txt`
4. Создадим бд, если ее еще нет (отсутствует папка instance). Для этого запустим скрипт на питоне  
Linux/Windows: `python create_db.py`
## Как запустить приложение
Нажми Ctrl+F5 когда открыт файл app.py или нажми на треугольник в правом верхнем углу.
Теперь вы можете открыть браузер и перейти по ссылке http://127.0.0.1:5000,
чтобы посмотреть как все работает.
В debug-режиме можно вносить изменения в код, сохраняться (Ctrl+S) и обновлять страницу в браузере - изменеия будут видны сразу, не надо будет перезапускать приложение.
## Как остановить приложение
В открытом терминале с приложением нажать Ctrl+C
## Что есть что
* .gitignore - список игнорируемых файлов git
* app.py - файл приложения
* README.md - этот файл
* requirements.txt - файл с зависимостями
* папка templates содержит набор страниц HTML
* папка static содержит статические файлы (CSS-файлы, картинки и пр.)
* папка instance содержит файл бд hackathon.db
* create_db.py - скрипт на питоне, создающий бд 
5353gfgdfgdfgsdfgsf