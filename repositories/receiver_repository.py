import requests
import json
from helper.constant_manager import ConstantManager

linkReceiver = ConstantManager.URL_FIREBASE + 'receivers'

class ReceiversRepository:

    def get_all_receivers():
        response = requests.get(f'{linkReceiver}/.json')
        return json.loads(response.text)

    def get_receivers_by_value(value):
        response = requests.get(f'{linkReceiver}/.json?orderBy="$value"&equalTo="{value}"')
        return json.loads(response.text)
    
    def insert_receiver(receiver):
        response = requests.post(f'{linkReceiver}/.json', data=json.dumps(receiver))
        return response.text

    def delete_receiver(receiver_id):
        requests.delete(f'{linkReceiver}/{receiver_id}/.json')

    def update_receiver(receiver_id, receiver):
        response = requests.patch(f'{linkReceiver}/{receiver_id}/.json', data=json.dumps(receiver))
        return response.text

