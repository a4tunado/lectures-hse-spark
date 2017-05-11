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

RUN pip3 install --upgrade pip \
      && pip3 install jupyter \
                       matplotlib \
                       mrjob \
                       tweepy \
                       numpy \
                       sklearn

# BASHRC
RUN echo "export SPARK_HOME=/usr/local/spark-2.1.0-bin-hadoop2.7" >> /root/.bashrc
RUN echo "export PYTHONPATH=\$SPARK_HOME/python:\$SPARK_HOME/python/build:\$PYTHONPATH" >> /root/.bashrc
RUN echo "export PYTHONPATH=\$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:\$PYTHONPATH" >> /root/.bashrc

EXPOSE 4040 6066 7077 8080 8888

WORKDIR $SPARK_HOME
