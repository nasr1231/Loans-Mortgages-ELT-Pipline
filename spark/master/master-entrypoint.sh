#!/bin/bash
set -e

echo "Starting Spark Master..."

# Start Spark master
/spark/bin/spark-class org.apache.spark.deploy.master.Master \
    --ip 0.0.0.0 \
    --port 7077 \
    --webui-port 8080
