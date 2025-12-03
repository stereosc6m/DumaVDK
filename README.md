Парсер новостей Думы города Владивостока
Скрипт собирает новости с сайта Думы Владивостока, фильтрует по ссылкам вида /news/2... и сохраняет в CSV файл dumavlad_news.csv.

Требования
Python 3.8+

requests-cache, beautifulsoup4, tqdm, lxml

Установка и запуск

# Создать venv
Находясь в папке с исполянемым файлом
```python -m venv venv```

# Активировать (Windows)
```source venv\Scripts\activate```

# Активировать (Linux/Mac)
```source venv/bin/activate```

2. Установка зависимостей из requirements.txt
```pip install -r requirements.txt```

3. Запуск программы
```python DumaVDK.py```

Быстрый старт (одной командой)
```python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python DumaVDK.py```
