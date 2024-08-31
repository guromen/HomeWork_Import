from application.salary import calculate_salary as c
from application.db.people import get_employees as g
from datetime import datetime as dt
from basic_bar import bar
import time

# Example basic_bar
data = range(100)
for item in bar(data):
    time.sleep(0.01)

# Datetime
now = dt.now()
print(f"Текущее время {now:%d.%m.%Y %H:%M}")


if __name__ == '__main__':
    f'{g()}{c()}'
    