import configparser
from http.client import HTTPException

import requests

from client.customer.customer_response import CustomerResponse


class CustomerClient:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.url = config['customer']['url']


    def get_data(self, document):
        url = f'{self.url}/{document}'
        result = requests.get(url)
        if result.status_code == 200:
            return CustomerResponse(**result.json())

        raise HTTPException(result.status_code, result.text)

