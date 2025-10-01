#!/bin/bash
set -e

SPARK_MASTER=${SPARK_MASTER:-"spark://spark-master:7077"}

echo "Starting Spark Worker. Connecting to master at $SPARK_MASTER"

/spark/bin/spark-class org.apache.spark.deploy.worker.Worker \
    --webui-port 8081 \
    $SPARK_MASTER
