### Hexlet tests and linter status:
[![Actions Status](https://github.com/DenisDolgov1991/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/DenisDolgov1991/python-project-50/actions)
[![Action Status](https://github.com/DenisDolgov1991/python-project-50/action/workflows/python-ci.yml/badge.svg)](https://github.com/DenisDolgov1991/python-project-50/action)
[![Maintainability](https://api.codeclimate.com/v1/badges/c24b4427ea61b0e121b0/maintainability)](https://codeclimate.com/github/DenisDolgov1991/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c24b4427ea61b0e121b0/test_coverage)](https://codeclimate.com/github/DenisDolgov1991/python-project-50/test_coverage)


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
