import os
import re
from datetime import datetime, timedelta

from dags.config import Environment


def clean_logs():
    delta = int(Environment.LOG_DURATION)
    last_date = datetime.now() - timedelta(days=delta)

    for el in os.walk("logs/"):
        for file in el[2]:
            if date := re.findall(r"\d{4}-\d{2}-\d{2}", os.path.join(el[0], file)):
                try:
                    if datetime.strptime(str(date[0]), "%Y-%m-%d") < last_date:
                        print(os.path.join(el[0], file))
                        os.remove(os.path.join(el[0], file))
                except Exception as e:
                    print(e)


if __name__ == "__main__":
    clean_logs()
