import os

from airflow.models import Variable


class Environment:
    LOG_DURATION = Variable.get("LOG_DURATION", default_var=14)
