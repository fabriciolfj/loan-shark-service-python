import configparser


class ProducerConfig:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        url = config['kafka']['url']

        conf = {
            'bootstrap.servers': url,
        }

        self.config = conf

class ConsumerConfig:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        url = config['kafka']['url']
        group_id = config['kafka']['group_id']

        conf = {
            'bootstrap.servers': url,
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
        }

        self.config = conf