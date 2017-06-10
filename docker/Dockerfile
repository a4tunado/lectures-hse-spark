FROM ubuntu:14.04

RUN apt-get update && apt-get -y install curl

# JAVA
ARG JAVA_ARCHIVE=http://download.oracle.com/otn-pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/server-jre-8u121-linux-x64.tar.gz
ENV JAVA_HOME /usr/local/jdk1.8.0_121

ENV PATH $PATH:$JAVA_HOME/bin
RUN curl -sL --retry 3 --insecure \
  --header "Cookie: oraclelicense=accept-securebackup-cookie;" $JAVA_ARCHIVE \
  | tar -xz -C /usr/local/ && ln -s $JAVA_HOME /usr/local/java

# SPARK
ARG SPARK_ARCHIVE=http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
RUN curl -s $SPARK_ARCHIVE | tar -xz -C /usr/local/

ENV SPARK_HOME /usr/local/spark-2.1.0-bin-hadoop2.7
ENV PATH $PATH:$SPARK_HOME/bin

# JUPYTER
RUN apt-get -y install python3-setuptools && easy_install3 pip
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade awscli \
                           jupyter \
                           matplotlib \
                           mrjob \
                           tweepy \
                           numpy \
                           sklearn \
                           scipy

# BASHRC
RUN echo "export SPARK_HOME=/usr/local/spark-2.1.0-bin-hadoop2.7 \n\
export PYTHONPATH=\$SPARK_HOME/python:\$SPARK_HOME/python/build:\$PYTHONPATH \n\
export PYTHONPATH=\$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:\$PYTHONPATH" >> /root/.bashrc

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


EXPOSE 4040 6066 7077 8080 8888

WORKDIR $SPARK_HOME
