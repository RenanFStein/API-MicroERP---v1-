from venv import create
from django.forms import ValidationError
from rest_framework.views import exception_handler
from rest_framework import serializers
from .models import *

class EmpresaSerializer(serializers.ModelSerializer):
    """ Serialização do model Empresa """
    class Meta:
        model = Empresa
        fields = ['id',
                'nome_empresa',
                'cnpj_empresa',
                'cep_empresa',
                'endereco_empresa',
                'numero_endereco_empresa',
                'complemento_endereco_empresa',
                'telefone_empresa',
                'email_empresa',
                'cidade_empresa',
                'uf_empresa']
        

class ClientesSerializer(serializers.ModelSerializer):
    """ Serialização do model Clientes """
    class Meta:
        model = Cliente
        fields = ['id',
                'nome_cliente',
                'cnpj_cliente',
                'telefone_cliente',
                'email_cliente',
                'endereco_cliente',
                'numero_endereco_cliente',
                'cep_cliente',
                'complemento_endereco_cliente',
                'cidade_cliente',
                'uf_cliente',]

class FornecedorSerializer(serializers.ModelSerializer):
    """ Serialização do model Fornecedor """
    class Meta:
        model = Fornecedor
        fields = ['id',
                'nome_fornecedor',
                'cnpj_fornecedor',
                'telefone_fornecedor',
                'email_fornecedor',
                'endereco_fornecedor',
                'numero_endereco_fornecedor',
                'cep_fornecedor',
                'complemento_endereco_fornecedor',
                'cidade_fornecedor',
                'uf_fornecedor',]

class ProdutosSerializer(serializers.ModelSerializer):
    """ Serialização do model Vendas """
    class Meta:
        model = Produto
        fields = ['id','nomeProduto','descricao_produto', 'quantidade_estoque', 'custo_medio', 'valor_estoque']

class EstoquesSerializer(serializers.ModelSerializer):
    """ Serialização do model Vendas """
    class Meta:
        model = Estoque
        fields = ['id', 'produto','quantidade','valor']

class VendasSerializer(serializers.ModelSerializer):
    """ Serialização do model Vendas """
    estoque = EstoquesSerializer()
    class Meta:
        model = Vendas
        fields = ['id','cliente', 'estoque', 'nome_cliente','produto', 'quantidade','valor','total_venda']

    def create(self, validated_data):
        profile_data = validated_data.pop('estoque')
        produto=Estoque.objects.create(produto= profile_data['produto'], 
                                    quantidade  = profile_data['quantidade'] * -1, 
                                    valor  = profile_data['valor'])
        vendas = Vendas.objects.create(estoque=produto, **validated_data)
        Caixa.objects.create(status= False, vendas = vendas)
        return vendas

    def update(self, instance, validated_data):
        data = dict(self.data)
        validated = dict((validated_data)) 
        compra = Vendas.objects.get(id=data['id']) 
        compra.fornecedor = validated['fornecedor']
        compra.save()   
        atualiza_estoque = Estoque.objects.get(id=data['produto']['estoque'][0][0])  
        estq = dict(validated['estoque'])
        atualiza_estoque.produto = estq['produto']
        atualiza_estoque.quantidade = estq['quantidade']
        atualiza_estoque.valor = estq['valor']
        atualiza_estoque.save()               
        return instance

class ComprasSerializer(serializers.ModelSerializer):
    """ Serialização do model Compras """
    #
    estoque = EstoquesSerializer()
    
    class Meta:
        model = Compras
        fields = ['id','fornecedor', 'estoque', 'nome_fornecedor','produto', 'quantidade','valor','total_compra']

    def create(self, validated_data):
        profile_data = validated_data.pop('estoque')

        produto=Estoque.objects.create(produto= profile_data['produto'], 
                                    quantidade  = abs(profile_data['quantidade']), 
                                    valor  = profile_data['valor'])
        compra=Compras.objects.create(estoque=produto, **validated_data)
        Caixa.objects.create(status= False, compras = compra)
        return compra

    
    def update(self, instance, validated_data):
        data = dict(self.data)
        validated = dict((validated_data)) 
        compra = Compras.objects.get(id=data['id']) 
        compra.fornecedor = validated['fornecedor']
        compra.save()   
        atualiza_estoque = Estoque.objects.get(id=data['produto']['estoque'][0][0])  
        estq = dict(validated['estoque'])
        atualiza_estoque.produto = estq['produto']
        atualiza_estoque.quantidade = estq['quantidade']
        atualiza_estoque.valor = estq['valor']
        atualiza_estoque.save()               
        return instance      
        
class CaixaSerializer(serializers.ModelSerializer):
    """ Serialização do model Caixa """
    class Meta:
        model = Caixa
        fields = ['id','venda','compra','status']


          