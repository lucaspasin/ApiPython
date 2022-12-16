from app import myapp
from flask import request

from repositories.receiver_repository import ReceiversRepository
from validators.receiver_validator import ReceivedValidator

@myapp.get('/receiver')
def get_all_receivers():

    value = request.args.get('search_value')

    if(value != None):
        return ReceiversRepository.get_receivers_by_value(value)

    return ReceiversRepository.get_all_receivers()

@myapp.post('/receiver')
def insert_new_receiver():
    request_data = request.get_json()

    validations = ReceivedValidator.validate_before_insert(request_data) 
    if(validations != {}):
        return validations, 400

    ReceiversRepository.insert_receiver(request_data)
    result = ReceiversRepository.get_all_receivers()
    result['message'] = 'Receiver inserted successfully'

    return result

@myapp.patch('/receiver')
def update_receiver():
    request_data = request.get_json()
    receiver_id = request.args.get('receiver_id')

    validations = ReceivedValidator.validate_before_insert(request_data)
    if(validations != {}):
        return validations, 400

    ReceiversRepository.update_receiver(receiver_id, request_data)
    result = ReceiversRepository.get_all_receivers()
    result['message'] = 'Receiver updated successfully'

    return result

@myapp.delete('/receiver')
def delete_receiver():
    request_data = request.get_data()
    received_array = request_data.split(b',')

    for id in received_array:
        ReceiversRepository.delete_receiver(id.decode().strip())

    return {'Message': 'Excluido com sucesso'}, 200
