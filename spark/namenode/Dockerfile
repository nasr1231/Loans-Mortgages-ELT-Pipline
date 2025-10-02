FROM bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8

# Switch to root user
USER root

# Install basic tools first
RUN apt-get update && apt-get install -y wget gnupg tar && rm -rf /var/lib/apt/lists/*
# Add JDBC driver For Postgres
RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.20.jar -O /opt/sqoop/lib/postgresql.jar