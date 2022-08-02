FROM confluentinc/cp-kafka-connect:latest

USER root

RUN mkdir -p /opt/confluent-hub-client \
    && curl "http://client.hub.confluent.io/confluent-hub-client-latest.tar.gz" \
    | tar -xzv -C /opt/confluent-hub-client
ENV PATH="/opt/confluent-hub-client/bin:${PATH}"

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.2.1

