from validators.receiver_validator import ReceivedValidator
import unittest
import copy

dict_receiver_ok = {'account': 
        {
        'account_type':'Conta Poupança',
        'agency':'5431',
        'agency_digit':'5',
        'bank':'Santander',
        'current_account':'57489536',
        'current_account_digit':'2'
        },
        'email':'ABREU@ABREU.COM',
        'name':'josé',
        'registration':'01234567890',
        'key_type': '01234567890',
        'pix_key':'01234567890',
        'pix_key_type': 'CPF',
        'status':'Validado'
        }

class TestReceiverValidator(unittest.TestCase):

    def test_validator_ok(self):
        self.assertEqual(ReceivedValidator.validate_before_insert(dict_receiver_ok), {})

    def test_validator_no_name(self):

        dict_no_name = copy.deepcopy(dict_receiver_ok)
        del dict_no_name['name']

        self.assertIn('name', ReceivedValidator.validate_before_insert(dict_no_name))

        del dict_no_name

    def test_validator_name_empty(self):
        dict_name_empty = copy.deepcopy(dict_receiver_ok)
        dict_name_empty['name'] = ''

        self.assertIn('name', ReceivedValidator.validate_before_insert(dict_name_empty))

        del dict_name_empty

    def test_validator_no_pix_key(self):
        dict_key_no_pix_key = copy.deepcopy(dict_receiver_ok)
        del dict_key_no_pix_key['pix_key']

        self.assertIn('pix_key', ReceivedValidator.validate_before_insert(dict_key_no_pix_key))

        del dict_key_no_pix_key

    def test_validator_pix_key_empty(self):
        dict_pix_key_empty = copy.deepcopy(dict_receiver_ok)
        dict_pix_key_empty['pix_key'] = ''

        self.assertIn('pix_key', ReceivedValidator.validate_before_insert(dict_pix_key_empty))

        del dict_pix_key_empty

    def test_validator_no_pix_key_type(self):
        dict_key_no_pix_key_type = copy.deepcopy(dict_receiver_ok)
        del dict_key_no_pix_key_type['pix_key_type']

        self.assertIn('pix_key_type', ReceivedValidator.validate_before_insert(dict_key_no_pix_key_type))

        del dict_key_no_pix_key_type

    def test_validator_pix_key_type_empty(self):
        dict_pix_key_type_empty = copy.deepcopy(dict_receiver_ok)
        dict_pix_key_type_empty['pix_key_type'] = ''

        self.assertIn('pix_key_type', ReceivedValidator.validate_before_insert(dict_pix_key_type_empty))

        del dict_pix_key_type_empty

    def test_validator_no_registration(self):
        dict_key_no_registration = copy.deepcopy(dict_receiver_ok)
        del dict_key_no_registration['registration']

        self.assertIn('registration', ReceivedValidator.validate_before_insert(dict_key_no_registration))

        del dict_key_no_registration

    def test_validator_registration_empty(self):
        dict_registration_empty = copy.deepcopy(dict_receiver_ok)
        dict_registration_empty['registration'] = ''

        self.assertIn('registration', ReceivedValidator.validate_before_insert(dict_registration_empty))

        del dict_registration_empty

    def test_validator_no_status(self):
        dict_key_no_status = copy.deepcopy(dict_receiver_ok)
        del dict_key_no_status['status']

        self.assertIn('status', ReceivedValidator.validate_before_insert(dict_key_no_status))

        del dict_key_no_status

    def test_validator_status_empty(self):
        dict_status_empty = copy.deepcopy(dict_receiver_ok)
        dict_status_empty['status'] = ''

        self.assertIn('status', ReceivedValidator.validate_before_insert(dict_status_empty))

        del dict_status_empty

    def test_validator_no_email(self):
        dict_key_no_email = copy.deepcopy(dict_receiver_ok)
        del dict_key_no_email['email']

        self.assertIn('email', ReceivedValidator.validate_before_insert(dict_key_no_email))

        del dict_key_no_email

    def test_validator_email_empty(self):
        dict_email_empty = copy.deepcopy(dict_receiver_ok)
        dict_email_empty['email'] = ''

        self.assertIn('email', ReceivedValidator.validate_before_insert(dict_email_empty))

        del dict_email_empty

    

    
    