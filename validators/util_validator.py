import re

class UtilValidator:

    def validate_cpf_regex(cpf):
        cpfRegex = re.compile('^[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}$')
        return cpfRegex.search(cpf)
    
    def validate_cnpj_regex(cnpj):
        cnpjRegex = re.compile('^[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2}$')
        return cnpjRegex.search(cnpj)

    def validate_email_regex(email):
        emailRegex = re.compile('^[A-Z0-9+_.-]+@[A-Z0-9.-]+$')
        return emailRegex.search(email)

    def validate_phone_regex(phone):
        phoneRegex = re.compile('^((?:\+?55)?)([1-9][0-9])(9[0-9]{8})$')
        return phoneRegex.search(phone)

    def validate_random_key_regex(random_key):
        random_key_regex = re.compile('^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
        return random_key_regex.search(random_key)

    def validate_pix_key_type(pix_key_type):
        allowed_types_pix_key = ['CPF', 'CNPJ', 'EMAIL', 'TELEFONE', 'CHAVE_ALEATORIA']
        if(pix_key_type in allowed_types_pix_key):
            return True
        return False