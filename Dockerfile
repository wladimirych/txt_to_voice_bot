FROM python:3.12
WORKDIR /app
COPY . .

# Установка зависимостей из PyPI
RUN pip install --no-cache-dir -r requirements.txt

# Указывает, что при запуске контейнера будет выполнена команда python tvbot.py
# Это необязательно, если вы запускаете контейнер вручную и указываете команду.
# Но удобно, если контейнер "сам знает", что запускать.
CMD ["python", "tvbot.py"]