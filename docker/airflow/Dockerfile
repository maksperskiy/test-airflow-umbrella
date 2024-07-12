ARG AIRFLOW_VERSION="2.9.2"
ARG BASE_PYTHON_VERSION="3.10"

FROM apache/airflow:${AIRFLOW_VERSION}-python${BASE_PYTHON_VERSION} as airflow-image

USER root

COPY --chown=airflow:root requirements.txt ./

USER airflow

RUN python -m pip install --upgrade pip setuptools
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r ./requirements.txt
