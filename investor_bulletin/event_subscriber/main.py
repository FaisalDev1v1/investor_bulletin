# from pika import BlockingConnection
# Create a connection object to start consuming events

# def init_subscriber()
  # return BlockingConnection(..)

# def on_event(ch, method, properties, body):
      # pass

# if __name__ == "__main__":
    # subscriber = init_subscriber()
    # .basic_consume(queue=queue_name, on_message_callback=on_event)
# event_subscriber/main.py
import pika
from resource.alert.alert_service import create_alert

def callback(ch, method, properties, body):
    print(f"Received {body}")
    create_alert(body)

def consume_threshold_alert():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key='alert.threshold')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_threshold_alert()
