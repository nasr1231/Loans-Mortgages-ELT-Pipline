FROM bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8

# Switch to root user
USER root

# Fix Debian Stretch sources (use archive.debian.org instead of deb.debian.org)
RUN sed -i 's|deb.debian.org|archive.debian.org|g' /etc/apt/sources.list && \
    sed -i 's|security.debian.org|archive.debian.org|g' /etc/apt/sources.list && \
    sed -i '/stretch-updates/d' /etc/apt/sources.list

# Install wget + tar
RUN apt-get update && apt-get install -y postgresql-client wget tar && rm -rf /var/lib/apt/lists/*

# ============================
# Install Sqoop
# ============================
ENV SQOOP_HOME=/opt/sqoop
RUN wget https://archive.apache.org/dist/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz -O /tmp/sqoop.tar.gz \
    && tar -xvzf /tmp/sqoop.tar.gz -C /opt \
    && mv /opt/sqoop-1.4.7.bin__hadoop-2.6.0 $SQOOP_HOME \
    && rm /tmp/sqoop.tar.gz

# Add JDBC driver (Postgres example)
RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.20.jar -O $SQOOP_HOME/lib/postgresql.jar

# Update PATH
ENV PATH=$PATH:$SQOOP_HOME/bin
