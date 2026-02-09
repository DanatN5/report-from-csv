[![Python CI](https://github.com/DanatN5/report-from-csv/actions/workflows/build.yml/badge.svg)](https://github.com/DanatN5/report-from-csv/actions/workflows/build.yml)

# Демонстрация работы программы:
    [Смотреть на asciinema.org](https://asciinema.org/a/e6fZ1Udis6AOJoii)

# Установка:

``` 
git clone git@github.com:DanatN5/report-from-csv.git
```

````
cd report-from-csv
````

`````
uv build
``````

````````
uv tool install dist/*.whl
````````

# Запуск:

``` 
report-from-csv -h
```
``` 
report-from-csv --files путь_к_файлу --report average-gdp
```

# Удаление:
````
make uninstall
````