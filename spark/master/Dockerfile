# Base image: Spark master مع Hadoop 3.2
FROM bde2020/spark-base:3.3.0-hadoop3.3

# Set environment variables
ENV SPARK_HOME=/spark
ENV SQOOP_HOME=/opt/sqoop
ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_COMMON_HOME=$HADOOP_HOME
ENV HADOOP_MAPRED_HOME=$HADOOP_HOME
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$SQOOP_HOME/bin

# Install useful tools + python
RUN apk update && apk add --no-cache \
    wget \
    openjdk8 \
    python3 \
    py3-pip \
    unzip \
    nano \
    vim \
    netcat-openbsd \
 && rm -rf /var/cache/apk/*

# Create working directory
WORKDIR /opt/spark-master

# Copy entrypoint script
COPY master-entrypoint.sh /opt/spark-master/master-entrypoint.sh
RUN chmod +x /opt/spark-master/master-entrypoint.sh

# Default command
CMD ["/opt/spark-master/master-entrypoint.sh"]
