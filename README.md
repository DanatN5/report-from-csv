[![Python CI](https://github.com/DanatN5/report-from-csv/actions/workflows/build.yml/badge.svg)](https://github.com/DanatN5/report-from-csv/actions/workflows/build.yml)

# Демонстрация работы программы:
    https://asciinema.org/a/VBD1lP52dUB5AyTS\

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