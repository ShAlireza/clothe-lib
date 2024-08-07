import json

from clothe_lib.utils import RabbitmqHandler


class ConsumerKinds:
    DIVAR = 'divar'
    BAMA = 'bama'
    SHEYPOOR = 'sheypoor'
    NIKE = 'nike'


class Consumer:
    def __init__(self, *args, **kwargs):
        self.kind = kwargs.get('kind')
        rabbitmq_host = kwargs.get('rabbitmq_host')
        rabbitmq_port = kwargs.get('rabbitmq_port')
        self.rabbitmq_handler = RabbitmqHandler(
            rabbitmq_host=rabbitmq_host,
            rabbitmq_port=rabbitmq_port
        )

    def consume(self):
        self.rabbitmq_handler.pull(self.kind, self.callback)

    def callback(self, ch, method, properties, body):
        ch.basic_ack(delivery_tag=method.delivery_tag)
        self.process(json.loads(body.decode('utf-8')))

    def process(self, data):
        raise NotImplementedError
