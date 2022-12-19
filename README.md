ApiPython:

Para rodar o projeto primeiramente deve ser executado o comando pip install -r requirements.txt

Os testes podem ser executador com o comando python -m unittest

Esta api foi desenvolvida com o intuito de testar novas tecnologias(pra mim). 
São inicialmente 4 endpoints formando um CRUD simples em um banco não relacional.

POST:
    Espera um JSON body com os dados do recebedor:
    {
        "account": {
            "account_type": "Conta Poupança",
            "agency": "5431",
            "agency_digit": "5",
            "bank": "Santander",
            "current_account": "57489536",
            "current_account_digit": "2"
        },
        "email": "ABR@BREU.COM",
        "name": "josé",
        "pix_key": "5548999985564",
        "pix_key_type": "TELEFONE",
        "registration": "ABR@BREU.COM",
        "status": "Rascunho"
    }

PATCH:
    Espera o receiver_id como query parameter e um JSON body com os dados a serem alterados do recebedor:
    {
        "account": {
            "account_type": "Conta Poupança",
            "agency": "5431",
            "agency_digit": "5",
            "bank": "itau",
            "current_account": "57489536",
            "current_account_digit": "2"
        },
        "email": "ABREU@ABREU.COM",
        "name": "josé",
        "pix_key": "01234567890",
        "pix_key_type": "CPF",
        "registration": "01234567890",
        "status": "Validado"
    }

GET:
    Pode ser chamado sem nenhum parametro e será retornado uma lista contendo 10 registros e o index para a próxima página.
    Para requisitar a próxima página o mesmo endpoint pode ser usado informando o query parameter next_index na URL.
    para modificar a quantidade de itens na paginação pode ser enviado o parametro limit com o numero de itens desejado.

DELETE:
    Espera o receiver_id a ser deletado como uma string no body. 
    Pode ser enviado uma lista de ids separados por vírgula.

