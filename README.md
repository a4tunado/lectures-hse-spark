# Масштабируемое машинное обучение и анализ больших данных с Apache Spark

[Инструкция по установке Docker](https://github.com/a4tunado/lectures-hse-spark#Инструкция-по-установке-docker-)

[Образ с предустановленным Apache Spark](https://github.com/a4tunado/lectures-hse-spark#Образ-с-предустановленным-apache-spark-)

[Инструкция по установке Apache Spark](https://github.com/a4tunado/lectures-hse-spark#Инструкция-по-установке-apache-spark-)

### Инструкция по установке Docker [](#docker)
1. Установите Docker Engine на вашу локальную машину: https://docs.docker.com/engine/installation/
2. В директории ```lectures-hse-spark/docker``` выполните команду: ```docker build .``` для создания образа
3. Запустите контейнер: ```docker run -it -v <local path to lectures-hse-spark>:/lectures-hse-spark -p 8888:8888 <docker image id>```
4. После запуска контейнера, перейдите в директорию ```/lectures-hse-spark``` и запустите jupyter: ```jupyter notebook --allow-root --ip 0.0.0.0```

### Образ с предустановленным Apache Spark [](#virtualbox)
* Образ [Virtual Box](https://www.virtualbox.org/wiki/Downloads) доступен для скачивания по [ссылке](https://goo.gl/PrNTSJ)
* Пароль для входа в систему: 123

### Инструкция по установке Apache Spark [](#manual-setup)
1. Для работы с Apache Spark необходимо наличие следующих пакетов 
  * Java SE Development Kit [https://www.java.com](https://www.java.com)
  * Scala Build Tool [http://www.scala-sbt.org](http://www.scala-sbt.org/)
  * Python 2.7 [https://www.python.org](https://www.python.org/download/releases/2.7/)
  * Jupiter Notebook [http://jupyter.org](http://jupyter.org/install.html)
2. Скачать дистрибутив Apache Spark с [официального сайта](http://spark.apache.org/downloads.html)
3. Распаковать скаченный дистрибутив в директорию /opt/spark-2.1.0-bin-hadoop2.7
4. В файл ~/.bashrc добавить следующие строки
```bash
export SPARK_HOME=/opt/spark-2.1.0-bin-hadoop2.7
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/build:$PYTHONPATH
export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH
```
5. Проверить корректность установки можно с помощью следующего кода
```python
from pyspark import SparkContext
sc = SparkContext('local', 'test app')
a = range(10)
a = sc.parallelize(a)
print a.reduce(lambda x, y: x + y)
```
