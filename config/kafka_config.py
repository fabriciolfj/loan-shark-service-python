import configparser


class KafkaConfig:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        url = config['kafka']['url']

        conf = {
            'bootstrap.servers': url,
        }

        self.config = conf