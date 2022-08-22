from urllib import response
from rest_framework.test import APITestCase
from ..models import *
from django.urls import reverse
from rest_framework import status

class EmpresasTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Empresa-list')
        self.empresa = Empresa.objects.create(
            nome_empresa =  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            cnpj_empresa =  "12345678901234",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            cep_empresa =   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            endereco_empresa = "Rua de Teste",          #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            numero_endereco_empresa =  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            complemento_endereco_empresa =  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            telefone_empresa =  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            email_empresa =   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            cidade_empresa =  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            uf_empresa =      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        )    

    def test_request_get_empresas(self):
        """Testes para verificar a requisição do GET para listar os Empresa"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_create_empresa(self):
        """Testes para verificar a requisição do POST para criar um Empresa"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901230",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua de Teste",          #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_request_put_empresa(self):
        """Testes para verificar a requisição PUT não permitida """
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901230",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua de Teste",          #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.put('/api/Empresa/1/', data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)   
        
    def test_request_delete_empresa(self):
        """Testes para verificar a requisição DELETE empresa """
        response = self.client.delete('/api/Empresa/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_request_post_create_empresa_nome_vazio(self):
        """Testes para verificar a requisição do POST para criar um Empresa com nome vazio"""
        data = {
            'nome_empresa':  "",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901230",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua de Teste",          #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"nome_empresa":["Este campo não pode ser em branco."]}') 

    def test_request_post_create_empresa_cnpj_existente(self):
        """Testes para verificar a requisição do POST para criar um Empresa com CNPJ ja cadastrado"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901234",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua de Teste",          #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cnpj_empresa":["Cadastro Empresa com este Empresa CNPJ já existe."]}') 

    def test_request_post_create_empresa_cnpj_vazio(self):
        """Testes para verificar a requisição do POST para criar um Empresa com CNPJ vazio"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "",                         #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua de Teste",          #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cnpj_empresa":["Este campo não pode ser em branco."]}') 

    def test_request_post_create_empresa_cnpj_maior_permitido(self):
        """Testes para verificar a requisição do POST para criar um Empresa CNPJ maior que 14 caracteres"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "123456789012345",          #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua de Teste",          #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cnpj_empresa":["Certifique-se de que este campo não tenha mais de 14 caracteres."]}') 
   
    def test_request_post_create_empresa_com_CEP_vazio(self):
        """Testes para verificar a requisição do POST para criar um Empresa sem CEP"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901231",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "",                         #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua de Teste",          #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cep_empresa":["Este campo não pode ser em branco."]}')

    def test_request_post_create_empresa_com_CEP_maior_permitido(self):
        """Testes para verificar a requisição do POST para criar um Empresa sem CEP"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901231",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "123456789",                #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua de Teste",          #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cep_empresa":["Certifique-se de que este campo não tenha mais de 8 caracteres."]}')
        
    def test_request_post_create_empresa_com_endereco_vazio (self):
        """Testes para verificar a requisição do POST para criar um Empresa sem Endereço"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901231",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "",                      #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"endereco_empresa":["Este campo não pode ser em branco."]}')

    def test_request_post_create_empresa_com_numero_endereco_vazio (self):
        """Testes para verificar a requisição do POST para criar um Empresa sem numero endereço"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901231",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua Teste",             #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "",              #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"numero_endereco_empresa":["Este campo não pode ser em branco."]}')

    def test_request_post_create_empresa_com_numero_endereco_maior (self):
        """Testes para verificar a requisição do POST para criar um Empresa numero endereço maior"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901231",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua Teste",             #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "123456789",     #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"numero_endereco_empresa":["Certifique-se de que este campo não tenha mais de 8 caracteres."]}')

    def test_request_post_create_empresa_com_telefone_vazio (self):
        """Testes para verificar a requisição do POST para criar um Empresa telefone vazio"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901231",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua Teste",             #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "",                     #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"telefone_empresa":["Este campo não pode ser em branco."]}')

    def test_request_post_create_empresa_com_telefone_maior (self):
        """Testes para verificar a requisição do POST para criar um Empresa telefone maior"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901231",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua Teste",             #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "123456789012345",      #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"telefone_empresa":["Certifique-se de que este campo não tenha mais de 14 caracteres."]}')

    def test_request_post_create_empresa_com_email_vazio (self):
        """Testes para verificar a requisição do POST para criar um Empresa email vazio"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901231",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua Teste",             #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "" ,                      #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Cidade do Teste" ,       #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"email_empresa":["Este campo não pode ser em branco."]}')

    def test_request_post_create_empresa_com_cidade_vazio (self):
        """Testes para verificar a requisição do POST para criar um Empresa cidade vazio"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901231",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua Teste",             #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "" ,                      #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJ",                     #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"cidade_empresa":["Este campo não pode ser em branco."]}')

    def test_request_post_create_empresa_com_UF_vazio (self):
        """Testes para verificar a requisição do POST para criar um Empresa UF vazio"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901231",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua Teste",             #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Testes" ,                #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "",                       #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"uf_empresa":["Este campo não pode ser em branco."]}')

    def test_request_post_create_empresa_com_UF_maior (self):
        """Testes para verificar a requisição do POST para criar um Empresa UF maior"""
        data = {
            'nome_empresa':  "Empresa Teste 01",         #models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
            'cnpj_empresa':  "12345678901231",           #models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
            'cep_empresa':   "12345678",                 #models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
            'endereco_empresa': "Rua Teste",             #models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
            'numero_endereco_empresa':  "12345678",      #models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
            'complemento_endereco_empresa':  "",         #models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
            'telefone_empresa':  "12345678901234",       #models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
            'email_empresa':   "teste@teste.com" ,       #models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
            'cidade_empresa':  "Testes" ,                #models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
            'uf_empresa':      "DJJ",                    #models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.content.decode("utf-8"), 
            '{"uf_empresa":["Certifique-se de que este campo não tenha mais de 2 caracteres."]}')