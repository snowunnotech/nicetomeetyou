import argparse
import pika
import time

parser = argparse.ArgumentParser(description='Check connection.')
parser.add_argument('--server', default='rabbitmq')
parser.add_argument('--virtual_host', default='celery_vhost')
parser.add_argument('--ssl', action='store_true')
parser.add_argument('--port', type=int, default='5672')
parser.add_argument('--username', default='celery')
parser.add_argument('--password', default='pw123456')
args = vars(parser.parse_args())

credentials = pika.PlainCredentials(args['username'], args['password'])
parameters = pika.ConnectionParameters(host=args['server'],
                                       port=args['port'],
                                       virtual_host=args['virtual_host'],
                                       credentials=credentials,
                                       ssl=args['ssl'])

while True:
    try:
        connection = pika.BlockingConnection(parameters)
        if connection.is_open:
            print("RabbitMQ successful connected.")
            connection.close()
            break
    except Exception as e:
        print("RabbitMQ not responds... :{}".format(e))
        time.sleep(1.0)
