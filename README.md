# Open-source ML observability course

Course information: [link](https://www.evidentlyai.com/ml-observability-course).

## Requirments
- scikit-learn   0.24.2
- jupyter        1.0.0
- pandas         2.0.3
- numpy          1.20.3
- evidently      0.4.8
- pillow         10.1.0
- nltk           3.8.1
- prefect        2.14.9
- mlflow         2.4.2
- pyarrow
- psycopg        3.1.13
- psycopg_binary 3.1.13

### To allow reports, use jupyter nbextensions
jupyter nbextension install --sys-prefix --symlink --overwrite --py evidently

### To enable, run:
jupyter nbextension enable evidently --py --sys-prefix

### Running airflow on Docker for later in the series
- The instructions can be found in the airflow documentation [here](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#running-airflow-in-docker).

### Resolving jinja import error
- In section 5 the jinja import error required a flask up date as found in this [link](https://sebhastian.com/python-importerror-cannot-import-name-escape-from-jinja2/)