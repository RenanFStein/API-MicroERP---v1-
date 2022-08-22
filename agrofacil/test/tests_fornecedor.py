from urllib import response
from rest_framework.test import APITestCase
from ..models import *
from django.urls import reverse
from rest_framework import status

class FornecedorTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Fornecedor-list')
        self.fornecedor = Fornecedor.objects.create(
            nome_fornecedor =  "Fornecedor Teste 01",      #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            cnpj_fornecedor =  "12345678901234",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            cep_fornecedor =   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            endereco_fornecedor = "Rua de Teste",          #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            numero_endereco_fornecedor =  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            complemento_endereco_fornecedor =  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            telefone_fornecedor =  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            email_fornecedor =   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            cidade_fornecedor =  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            uf_fornecedor =      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        )    

    def test_request_get_fornecedores(self):
        """Testes para verificar a requisição do GET para listar os fornecedor"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_create_fornecedor(self):
        """Testes para verificar a requisição do POST para criar um fornecedor"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901230",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua de Teste",          #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_request_put_fornecedor(self):
        """Testes para verificar a requisição PUT não permitida """
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",      #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901239",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua de Teste",          #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.put('/api/Fornecedor/1/', data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)   
        
    def test_request_delete_fornecedor(self):
        """Testes para verificar a requisição DELETE fornecedor """
        response = self.client.delete('/api/Fornecedor/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_request_post_create_fornecedor_nome_vazio(self):
        """Testes para verificar a requisição do POST para criar um fornecedor com nome vazio"""
        data = {
            'nome_fornecedor':  "",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901230",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua de Teste",          #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"nome_fornecedor":["Este campo não pode ser em branco."]}') 

    def test_request_post_create_fornecedor_cnpj_existente(self):
        """Testes para verificar a requisição do POST para criar um fornecedor com CNPJ ja cadastrado"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",      #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901234",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua de Teste",          #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cnpj_fornecedor":["Cadastro Fornecedor com este Fornecedor CNPJ já existe."]}') 

    def test_request_post_create_fornecedor_cnpj_vazio(self):
        """Testes para verificar a requisição do POST para criar um fornecedor com CNPJ vazio"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "",                         #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua de Teste",          #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cnpj_fornecedor":["Este campo não pode ser em branco."]}') 

    def test_request_post_create_fornecedor_cnpj_maior_permitido(self):
        """Testes para verificar a requisição do POST para criar um fornecedor CNPJ maior que 14 caracteres"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "123456789012345",          #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua de Teste",          #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cnpj_fornecedor":["Certifique-se de que este campo não tenha mais de 14 caracteres."]}') 
   
    def test_request_post_create_fornecedor_com_CEP_vazio(self):
        """Testes para verificar a requisição do POST para criar um fornecedor sem CEP"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901231",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "",                         #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua de Teste",          #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cep_fornecedor":["Este campo não pode ser em branco."]}')

    def test_request_post_create_fornecedor_com_CEP_maior_permitido(self):
        """Testes para verificar a requisição do POST para criar um fornecedor sem CEP"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901231",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "123456789",                #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua de Teste",          #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cep_fornecedor":["Certifique-se de que este campo não tenha mais de 8 caracteres."]}')
        
    def test_request_post_create_fornecedor_com_endereco_vazio (self):
        """Testes para verificar a requisição do POST para criar um fornecedor sem Endereço"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901231",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "",                      #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"endereco_fornecedor":["Este campo não pode ser em branco."]}')

    def test_request_post_create_fornecedor_com_numero_endereco_vazio (self):
        """Testes para verificar a requisição do POST para criar um fornecedor sem numero endereço"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901231",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua Teste",             #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "",              #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"numero_endereco_fornecedor":["Este campo não pode ser em branco."]}')

    def test_request_post_create_fornecedor_com_numero_endereco_maior (self):
        """Testes para verificar a requisição do POST para criar um fornecedor numero endereço maior"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901231",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua Teste",             #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "123456789",     #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"numero_endereco_fornecedor":["Certifique-se de que este campo não tenha mais de 8 caracteres."]}')

    def test_request_post_create_fornecedor_com_telefone_vazio (self):
        """Testes para verificar a requisição do POST para criar um fornecedor telefone vazio"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901231",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua Teste",             #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "",                     #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"telefone_fornecedor":["Este campo não pode ser em branco."]}')

    def test_request_post_create_fornecedor_com_telefone_maior (self):
        """Testes para verificar a requisição do POST para criar um fornecedor telefone maior"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901231",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua Teste",             #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "123456789012345",      #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"telefone_fornecedor":["Certifique-se de que este campo não tenha mais de 14 caracteres."]}')

    def test_request_post_create_fornecedor_com_email_vazio (self):
        """Testes para verificar a requisição do POST para criar um fornecedor email vazio"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901231",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua Teste",             #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "" ,                      #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"email_fornecedor":["Este campo não pode ser em branco."]}')

    def test_request_post_create_fornecedor_com_cidade_vazio (self):
        """Testes para verificar a requisição do POST para criar um fornecedor cidade vazio"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901231",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua Teste",             #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "" ,                      #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJ",                     #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cidade_fornecedor":["Este campo não pode ser em branco."]}')

    def test_request_post_create_fornecedor_com_UF_vazio (self):
        """Testes para verificar a requisição do POST para criar um fornecedor UF vazio"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901231",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua Teste",             #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Testes" ,                #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "",                       #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"uf_fornecedor":["Este campo não pode ser em branco."]}')

    def test_request_post_create_fornecedor_com_UF_maior (self):
        """Testes para verificar a requisição do POST para criar um fornecedor UF maior"""
        data = {
            'nome_fornecedor':  "Fornecedor Teste 01",         #models.CharField(verbose_name="Nome da fornecedor", max_length=255, blank=False, null=False)
            'cnpj_fornecedor':  "12345678901231",           #models.CharField(verbose_name="fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_fornecedor':   "12345678",                 #models.CharField(verbose_name="CEP da fornecedor", max_length=8, blank=False, null=False)
            'endereco_fornecedor': "Rua Teste",             #models.CharField(verbose_name="Endereço da fornecedor", max_length=255, blank=False, null=False)
            'numero_endereco_fornecedor':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_fornecedor':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_fornecedor':  "12345678901234",       #models.CharField(verbose_name="Telefone da fornecedor", max_length=14, blank=False, null=False)
            'email_fornecedor':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da fornecedor", max_length=255, blank=False, null=False)
            'cidade_fornecedor':  "Testes" ,                #models.CharField(verbose_name="Cidade da fornecedor", max_length=255, blank=False, null=False)
            'uf_fornecedor':      "DJJ",                    #models.CharField(verbose_name="UF da fornecedor", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"uf_fornecedor":["Certifique-se de que este campo não tenha mais de 2 caracteres."]}')