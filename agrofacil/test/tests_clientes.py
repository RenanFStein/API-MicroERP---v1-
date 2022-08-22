from urllib import response
from rest_framework.test import APITestCase
from ..models import *
from django.urls import reverse
from rest_framework import status

class ClienteTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Clientes-list')
        self.cliente = Cliente.objects.create(
            nome_cliente =  "cliente Teste 01",      #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            cnpj_cliente =  "12345678901234",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            cep_cliente =   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            endereco_cliente = "Rua de Teste",          #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            numero_endereco_cliente =  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            complemento_endereco_cliente =  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            telefone_cliente =  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            email_cliente =   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            cidade_cliente =  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            uf_cliente =      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        )    

    def test_request_get_clientees(self):
        """Testes para verificar a requisição do GET para listar os cliente"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_create_cliente(self):
        """Testes para verificar a requisição do POST para criar um cliente"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901230",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua de Teste",          #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_request_put_cliente(self):
        """Testes para verificar a requisição PUT não permitida """
        data = {
            'nome_cliente':  "cliente Teste 01",      #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901239",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua de Teste",          #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.put('/api/Clientes/1/', data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)   
        
    def test_request_delete_cliente(self):
        """Testes para verificar a requisição DELETE cliente """
        response = self.client.delete('/api/Clientes/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_request_post_create_cliente_nome_vazio(self):
        """Testes para verificar a requisição do POST para criar um cliente com nome vazio"""
        data = {
            'nome_cliente':  "",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901230",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua de Teste",          #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"nome_cliente":["Este campo não pode ser em branco."]}') 

    def test_request_post_create_cliente_cnpj_existente(self):
        """Testes para verificar a requisição do POST para criar um cliente com CNPJ ja cadastrado"""
        data = {
            'nome_cliente':  "cliente Teste 01",      #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901234",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua de Teste",          #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cnpj_cliente":["Cadastro Cliente com este Cliente CNPJ já existe."]}') 

    def test_request_post_create_cliente_cnpj_vazio(self):
        """Testes para verificar a requisição do POST para criar um cliente com CNPJ vazio"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "",                         #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua de Teste",          #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cnpj_cliente":["Este campo não pode ser em branco."]}') 

    def test_request_post_create_cliente_cnpj_maior_permitido(self):
        """Testes para verificar a requisição do POST para criar um cliente CNPJ maior que 14 caracteres"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "123456789012345",          #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua de Teste",          #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cnpj_cliente":["Certifique-se de que este campo não tenha mais de 14 caracteres."]}') 
   
    def test_request_post_create_cliente_com_CEP_vazio(self):
        """Testes para verificar a requisição do POST para criar um cliente sem CEP"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901231",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "",                         #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua de Teste",          #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cep_cliente":["Este campo não pode ser em branco."]}')

    def test_request_post_create_cliente_com_CEP_maior_permitido(self):
        """Testes para verificar a requisição do POST para criar um cliente sem CEP"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901231",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "123456789",                #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua de Teste",          #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cep_cliente":["Certifique-se de que este campo não tenha mais de 8 caracteres."]}')
        
    def test_request_post_create_cliente_com_endereco_vazio (self):
        """Testes para verificar a requisição do POST para criar um cliente sem Endereço"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901231",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "",                      #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"endereco_cliente":["Este campo não pode ser em branco."]}')

    def test_request_post_create_cliente_com_numero_endereco_vazio (self):
        """Testes para verificar a requisição do POST para criar um cliente sem numero endereço"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901231",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua Teste",             #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "",              #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"numero_endereco_cliente":["Este campo não pode ser em branco."]}')

    def test_request_post_create_cliente_com_numero_endereco_maior (self):
        """Testes para verificar a requisição do POST para criar um cliente numero endereço maior"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901231",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua Teste",             #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "123456789",     #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"numero_endereco_cliente":["Certifique-se de que este campo não tenha mais de 8 caracteres."]}')

    def test_request_post_create_cliente_com_telefone_vazio (self):
        """Testes para verificar a requisição do POST para criar um cliente telefone vazio"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901231",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua Teste",             #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "",                     #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"telefone_cliente":["Este campo não pode ser em branco."]}')

    def test_request_post_create_cliente_com_telefone_maior (self):
        """Testes para verificar a requisição do POST para criar um cliente telefone maior"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901231",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua Teste",             #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "123456789012345",      #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"telefone_cliente":["Certifique-se de que este campo não tenha mais de 14 caracteres."]}')

    def test_request_post_create_cliente_com_email_vazio (self):
        """Testes para verificar a requisição do POST para criar um cliente email vazio"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901231",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua Teste",             #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "" ,                      #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"email_cliente":["Este campo não pode ser em branco."]}')

    def test_request_post_create_cliente_com_cidade_vazio (self):
        """Testes para verificar a requisição do POST para criar um cliente cidade vazio"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901231",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua Teste",             #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "" ,                      #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJ",                     #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cidade_cliente":["Este campo não pode ser em branco."]}')

    def test_request_post_create_cliente_com_UF_vazio (self):
        """Testes para verificar a requisição do POST para criar um cliente UF vazio"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901231",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua Teste",             #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Testes" ,                #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "",                       #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"uf_cliente":["Este campo não pode ser em branco."]}')

    def test_request_post_create_cliente_com_UF_maior (self):
        """Testes para verificar a requisição do POST para criar um cliente UF maior"""
        data = {
            'nome_cliente':  "cliente Teste 01",         #models.CharField(verbose_name="Nome da cliente", max_length=255, blank=False, null=False)
            'cnpj_cliente':  "12345678901231",           #models.CharField(verbose_name="cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_cliente':   "12345678",                 #models.CharField(verbose_name="CEP da cliente", max_length=8, blank=False, null=False)
            'endereco_cliente': "Rua Teste",             #models.CharField(verbose_name="Endereço da cliente", max_length=255, blank=False, null=False)
            'numero_endereco_cliente':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_cliente':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_cliente':  "12345678901234",       #models.CharField(verbose_name="Telefone da cliente", max_length=14, blank=False, null=False)
            'email_cliente':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da cliente", max_length=255, blank=False, null=False)
            'cidade_cliente':  "Testes" ,                #models.CharField(verbose_name="Cidade da cliente", max_length=255, blank=False, null=False)
            'uf_cliente':      "DJJ",                    #models.CharField(verbose_name="UF da cliente", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"uf_cliente":["Certifique-se de que este campo não tenha mais de 2 caracteres."]}')