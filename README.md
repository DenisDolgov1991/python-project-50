### Hexlet tests and linter status:
[![Actions Status](https://github.com/DenisDolgov1991/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/DenisDolgov1991/python-project-50/actions)


###  Установка

1. Клонируйте репозиторий git на свой локальный компьютер: git@github.com:DenisDolgov1991/python-project-50.git
2. Перейдите в каталог утилиты: `cd python-project-50`
3. Используйте команду make build для создания пакета.
4. Для установки используйте команду `python3 -m pip install --user dist/*.whl` или `make package-install`


**Вычислитель отличий**

Запускается из командной строки и вычисляет отличия между двумя файлами. На данный момент работает с JSON и YAML.

**Запуск справки:**

`gendiff -h`

**Запуск скрипта c настройками по-умолчанию:**

`gendiff <file1> <file2>`

**Сравнение двух плоских файлов: JSON.**
[![asciicast](https://asciinema.org/a/5JsAtd566rzXuzkTT2Q93aQDt.svg)](https://asciinema.org/a/5JsAtd566rzXuzkTT2Q93aQDt)
