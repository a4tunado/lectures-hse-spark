FROM ubuntu:14.04

MAINTAINER  Vyacheslav Murashkin <mvjacheslav@gmail.com>

RUN apt-get update && apt-get -y install curl git-core

# PYTHON3
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN apt-get -y install build-essential python3-dev python3-setuptools python3-distutils-extra 
RUN easy_install3 pip

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade awscli \
                           jupyter \
                           matplotlib \
                           mrjob \
                           tweepy \
                           numpy \
                           sklearn \
                           scipy

# JAVA
ENV JAVA_VER 8
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >> /etc/apt/sources.list && \
    echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \
    apt-get update && \
    echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections && \
    apt-get install -y --force-yes --no-install-recommends oracle-java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default && \
    apt-get clean && \
    rm -rf /var/cache/oracle-jdk${JAVA_VER}-installer

# SPARK
ARG SPARK_ARCHIVE=http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
RUN curl -s $SPARK_ARCHIVE | tar -xz -C /usr/local/

ENV SPARK_HOME /usr/local/spark-2.1.0-bin-hadoop2.7
ENV PATH $SPARK_HOME/bin:$PATH
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/build:$PYTHONPATH
ENV PYTHONPATH $SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH

RUN echo "#!/bin/bash \n\
aws emr create-cluster --release-label emr-5.5.0\
  --name 'emr-5.5.0 sparklyr + jupyter cli example'\
  --applications Name=Hadoop Name=Hive Name=Spark Name=Pig Name=Tez Name=Ganglia Name=Presto\
  --ec2-attributes KeyName=\${1},InstanceProfile=EMR_EC2_DefaultRole\
  --service-role EMR_DefaultRole\
  --instance-groups\
    InstanceGroupType=MASTER,InstanceCount=1,InstanceType=c3.4xlarge\
    InstanceGroupType=CORE,InstanceCount=4,InstanceType=c3.4xlarge\
  --region us-east-1\
  --log-uri s3://\${2}/emr-logs/\
  --bootstrap-actions Name='Install Jupyter notebook',Path='s3://aws-bigdata-blog/artifacts/aws-blog-emr-jupyter/install-jupyter-emr5.sh',\
Args=[--ds-packages,--ml-packages,--python-packages,'matplotlib tweepy sklearn scipy',--port,8880,--password,jupyter,--jupyterhub,--jupyterhub-port,8001,--cached-install,--notebook-dir,s3://\${2}/notebooks/,--copy-samples]" > /usr/local/bin/create-emr-cluster

RUN chmod +x /usr/local/bin/create-emr-cluster

# USER
RUN useradd --create-home --shell /bin/bash student
USER student

# GITHUB
RUN cd /home/student && git clone https://github.com/a4tunado/lectures-hse-spark.git

EXPOSE 4040 6066 7077 8080 8888

WORKDIR /home/student/lectures-hse-spark

CMD jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser --NotebookApp.token=''

