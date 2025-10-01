# Base image: نفس الإصدار زي master
FROM bde2020/spark-base:3.3.0-hadoop3.3

# Set environment variables
ENV SPARK_HOME=/spark
ENV HADOOP_HOME=/hadoop
ENV PATH=$SPARK_HOME/bin:$HADOOP_HOME/bin:$PATH

# Install useful tools (debugging + python for pyspark jobs)
RUN apk update && apk add --no-cache \
    bash \
    curl \
    wget \
    python3 \
    python3-dev \
    py3-pip \
    build-base \
    gcc \
    gfortran \
    musl-dev \
    linux-headers \
    libffi-dev \
    openblas-dev \
    && pip3 install --upgrade pip setuptools wheel


# Clean up build tools (optional to reduce size)
RUN apk del build-base gcc gfortran musl-dev linux-headers libffi-dev

# Create working directory
WORKDIR /opt/spark-worker

# Copy entrypoint script (to start worker & connect to master)
COPY worker-entrypoint.sh /opt/spark-worker/worker-entrypoint.sh
RUN chmod +x /opt/spark-worker/worker-entrypoint.sh

# Default command
CMD ["/opt/spark-worker/worker-entrypoint.sh"]
