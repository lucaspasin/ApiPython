from validators.util_validator import UtilValidator
import unittest

class TestReceiverValidator(unittest.TestCase):

    def test_valid_email(self):
        self.assertNotEqual(UtilValidator.validate_email_regex('ASD.ASD@GMAIL.COM'), None)

    def test_invalid_email(self):
        self.assertEqual(UtilValidator.validate_email_regex('asd@gmail.com'), None)

    def test_valid_cpf(self):
        self.assertNotEqual(UtilValidator.validate_cpf_regex('01234567890'), None)

    def test_valid_cpf_with_dots(self):
        self.assertNotEqual(UtilValidator.validate_cpf_regex('359.644.020-38'), None)

    def test_invalid_cpf(self):
        self.assertEqual(UtilValidator.validate_cpf_regex('a0123d5f48rt6'), None)

    def test_valid_cnpj(self):
        self.assertNotEqual(UtilValidator.validate_cnpj_regex('61787447000147'), None)

    def test_valid_cnpj_with_dots(self):
        self.assertNotEqual(UtilValidator.validate_cnpj_regex('04.857.938/0001-83'), None)

    def test_invalid_cnpj(self):
        self.assertEqual(UtilValidator.validate_cnpj_regex('a0123d5f48rt6'), None)

    def test_valid_phone(self):
        self.assertNotEqual(UtilValidator.validate_phone_regex('5548999954486'), None)

    def test_invalid_phone(self):
        self.assertEqual(UtilValidator.validate_phone_regex('999954486'), None)

    def test_valid_random_key(self):
        self.assertNotEqual(UtilValidator.validate_random_key_regex('c234ce6d-386a-4d39-8393-8d399e750942'), None)

    def test_invalid_random_key(self):
        self.assertEqual(UtilValidator.validate_random_key_regex('999954486'), None)

    def test_valid_pix_key_type(self):
        self.assertEqual(UtilValidator.validate_pix_key_type('CHAVE_ALEATORIA'), True)

    def test_invalid_pix_key_type(self):
        self.assertEqual(UtilValidator.validate_pix_key_type('999954486'), False)