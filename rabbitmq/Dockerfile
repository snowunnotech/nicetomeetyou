FROM rabbitmq:3.7-management
COPY . /etc/rabbitmq/
RUN rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_federation_management rabbitmq_stomp

EXPOSE 15671 15672
