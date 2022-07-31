from django.db import models
from django.utils.translation import gettext_lazy as _

class Empresa(models.Model):
    razaoSocial = models.CharField(max_length=200)
    nomeFantasia = models.CharField(max_length=120)
    cnpj = models.PositiveIntegerField(blank=True,null=False)
    telefone = models.PositiveIntegerField(blank=True,null=True)
    email = models.CharField(max_length=80)

    # Informações abaixo dependem do API Correios

    cep = models.PositiveIntegerField(blank=True,null=False)
    tipoCep = models.CharField(max_length=20)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=80)
    bairro = models.CharField(max_length=140)
    endereco = models.CharField(max_length=140)
    complemento = models.CharField(max_length=190)

    def __str__(self):
        return self

class Veiculo(models.Model):

    class DisponibilidadeVeiculo(models.IntegerChoices):
        ATIVO = 1, _("Ativo")
        VENDIDO = 2, _("Vendido")

    placa = models.CharField(max_length=7)
    renavam = models.CharField(max_length=9)
    chassi = models.CharField(max_length=17)
    antt = models.CharField(max_length=11)
    disponibilidade = models.IntegerField(
        choices=DisponibilidadeVeiculo.choices,
        default=DisponibilidadeVeiculo.ATIVO
        )
    pesoCubagem = models.PositiveIntegerField(blank=True, null=True)
    pesoTotal = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self

