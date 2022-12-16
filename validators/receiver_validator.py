from .util_validator import UtilValidator

class ReceivedValidator:

    def validate_before_insert(request_data):

        result = {}

        name = request_data.get('name', "") 
        if( name ==  "" ):
            result['name'] = "name not sent"

        status = request_data.get('status', "") 
        if( status ==  "" ):
            result['status'] = "status not sent"

        status = request_data.get('registration', "") 
        if( status ==  "" ):
            result['registration'] = "registration not sent"

        email = request_data.get('email', "") 
        if( email ==  "" ):
            result['email'] = "email not sent"
        
        if(email !=  ""):
            if(UtilValidator.validate_email_regex(email) == None):
                result['email'] = "email is invalid"

        pix_key_type = request_data.get('pix_key_type', "") 
        if( pix_key_type ==  "" ):
            result['pix_key_type'] = "pix_key_type not sent"

        if(pix_key_type !=  ""):
            if(UtilValidator.validate_pix_key_type(pix_key_type) == False):
                result['pix_key_type'] = "pix_key_type is invalid"

        pix_key = request_data.get('pix_key', "") 
        if( pix_key ==  "" ):
            result['pix_key'] = "pix_key not sent"
        
        if(pix_key_type != "" and pix_key !=  ""):
            match = ''
            match pix_key_type:
                case 'CPF':
                    match = UtilValidator.validate_cpf_regex(pix_key)
                case 'CNPJ':
                    match = UtilValidator.validate_cnpj_regex(pix_key)
                case 'EMAIL':
                    match = UtilValidator.validate_email_regex(pix_key)
                case 'TELEFONE':
                    match = UtilValidator.validate_phone_regex(pix_key)
                case 'CHAVE_ALEATORIA':
                    match = UtilValidator.validate_random_key_regex(pix_key)
            if(match == ''):
                result['pix_key'] = "pix_key is invalid"
                
        return result