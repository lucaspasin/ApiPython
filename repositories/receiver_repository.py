import requests
import json
from helper.constant_manager import ConstantManager

linkReceiver = ConstantManager.URL_FIREBASE + 'receivers'

class ReceiversRepository:

    def get_all_receivers(next_index, limit):

        if(limit == None):
            limit = 10

        query = f'{linkReceiver}/.json?orderBy="$key"'

        if(next_index != None):
            query = f'{query}&startAt="{next_index}"&limitToFirst={limit+1}'

        response = requests.get(query)

        dict = json.loads(response.text)
        last_item = dict.popitem()
        dict['next_index'] = last_item[0]

        return dict

    def get_receivers_by_value(value):

        query = f'{linkReceiver}/.json?orderBy="$value"&equalTo="{value}"'
        response = requests.get(query)

        return json.loads(response.text)
    
    def insert_receiver(receiver):
        response = requests.post(f'{linkReceiver}/.json', data=json.dumps(receiver))
        return response.text

    def delete_receiver(receiver_id):
        requests.delete(f'{linkReceiver}/{receiver_id}/.json')

    def update_receiver(receiver_id, receiver):
        response = requests.patch(f'{linkReceiver}/{receiver_id}/.json', data=json.dumps(receiver))
        return response.text

