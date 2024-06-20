import amqpstorm
from amqpstorm import Message

def publish_threshold_alert():
    connection = amqpstorm.Connection('localhost', 'guest', 'guest')
    channel = connection.channel()
    channel.exchange.declare(exchange='topic_logs', exchange_type='topic')
    
    routing_key = 'alert.threshold'
    message_body = 'Threshold Alert: Temperature exceeded the limit!'
    
    message = Message.create(channel, message_body)
    message.publish('topic_logs', routing_key)
    
    channel.close()
    connection.close()

if __name__ == "__main__":
    publish_threshold_alert()
