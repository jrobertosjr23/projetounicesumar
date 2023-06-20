# from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UnidadeJudiciaria(models.Model):

    codigo = models.IntegerField(unique=True)
    nome = models.CharField(max_length=50, unique=True)
    observacao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        self.codigo = str(self.codigo)
        return self.codigo + " - " + self.nome

    class Meta:
        verbose_name_plural = "Unidade Judiciária"


class Estado(models.Model):

    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=2, null=True, blank=True)
    observacao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Estado"


class Tribunal(models.Model):

    codigo = models.IntegerField(unique=True)
    regiao = models.CharField(max_length=50, unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    observacao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        codigo = f'{self.codigo:0>2}'
        estado = str(self.estado)
        return codigo + " - " + self.regiao + " - " + estado

    class Meta:
        verbose_name_plural = "Tribunal"


class Nicho(models.Model):

    unidade_judiciaria = models.ForeignKey(UnidadeJudiciaria, on_delete=models.CASCADE)
    tribunal = models.ForeignKey(Tribunal, on_delete=models.CASCADE)

    def __str__(self):
        cod_uj = str(self.unidade_judiciaria.codigo)
        tribunal = str(self.tribunal)
        return cod_uj + "." + tribunal

    class Meta:
        verbose_name_plural = "Nicho"


class Cliente(models.Model):

    segmento = models.ForeignKey(UnidadeJudiciaria, on_delete=models.CASCADE)
    nicho = models.ForeignKey(Nicho, on_delete=models.CASCADE)
    codigo = models.IntegerField()
    identificador = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=200)
    municipio_uf = models.CharField(max_length=50)
    email = models.EmailField()
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        identificador = str(self.identificador)
        return identificador


class Colaborador(models.Model):

    STATUS = (
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO')
    )

    nome_completo = models.CharField(max_length=200)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    sigla = models.CharField(max_length=3)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    email_institucional = models.EmailField()
    email_pessoal = models.EmailField()
    telefone = models.CharField(max_length=20)
    cargo = models.CharField(max_length=20)
    data_admissao = models.DateField()
    data_rescisao = models.DateField(null=True, blank=True)
    contatos_emergencia = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='ATIVO')

    def __str__(self):
        return self.nome + " " + self.sobrenome

    class Meta:
        verbose_name_plural = "Colaborador"

class Processo(models.Model):

    TIPO_ATUACAO = (
        ('PERÍCIA LIQUIDAÇÃO', 'PERÍCIA LIQUIDAÇÃO'),
        ('PERÍCIA INSTRUÇÃO', 'PERÍCIA INSTRUÇÃO'),
        ('PERÍCIA CONHECIMENTO', 'PERÍCIA CONHECIMENTO'),
        ('PERÍCIA CÍVEL', 'PERÍCIA CÍVEL'),
        ('ASSISTÊNCIA TÉCNICA PARTE 1', 'ASSISTÊNCIA TÉCNICA PARTE 1'),
        ('ASSISTÊNCIA TÉCNICA PARTE 2', 'ASSISTÊNCIA TÉCNICA PARTE 2'),
        ('ASSISTÊNCIA CONTRATO TRABALHO', 'ASSISTÊNCIA CONTRATO TRABALHO'),
        ('TERCEIRIZAÇÃO', 'TERCEIRIZAÇÃO'),
        ('ADMINISTRAÇÃO JUDICIAL', 'ADMINISTRAÇÃO JUDICIAL'),
        ('MUTIRÃO TRT6', 'MUTIRÃO TRT6'),
        ('EXECUÇÃO DE TÍTULO JUDICIAL', 'EXECUÇÃO DE TÍTULO JUDICIAL'),
    )
    TIPO_ACAO = (
        ('RECLAMAÇÃO TRABALHISTA', 'RECLAMAÇÃO TRABALHISTA'),
        ('EXECUÇÃO PROVISÓRIA', 'EXECUÇÃO PROVISÓRIA'),
        ('CONSIGNAÇÃO EM PAGAMENTO', 'CONSIGNAÇÃO EM PAGAMENTO'),
        ('AÇÃO DE CUMPRIMENTO', 'AÇÃO DE CUMPRIMENTO'),
        ('CUMPRIMENTO DE SENTENÇA', 'CUMPRIMENTO DE SENTENÇA'),
        ('PROCEDIMENTO COMUM CÍVEL', 'PROCEDIMENTO COMUM CÍVEL'),
        ('AÇÃO MONITÓRIA', 'AÇÃO MONITÓRIA'),
        ('AÇÃO CIVIL COLETIVA', 'AÇÃO CIVIL COLETIVA'),
        ('AÇÃO CIVIL PÚBLICA', 'AÇÃO CIVIL PÚBLICA'),
    )
    TIPO_PROCESSO = (
        ('PJe', 'PJe'),
        ('PJe-n', 'PJe-n'),
        ('CSV', 'CSV'),
        ('CSV-n', 'CSV-n'),
        ('CSV-AF', 'CSV-AF'),
        ('Físico', 'Físico'),
    )

    responsavel_cadastrado = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    data_cadastrado = models.DateField()
    id_processo = models.IntegerField(unique=True)
    tipo_atuacao = models.CharField(max_length=50, choices=TIPO_ATUACAO)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_processo = models.CharField(max_length=25, unique=True)
    tipo_acao = models.CharField(max_length=50, choices=TIPO_ACAO)
    tipo_processo = models.CharField(max_length=50, choices=TIPO_PROCESSO)
    parte_1 = models.TextField()
    parte_2 = models.TextField()
    processos_associados = models.IntegerField()
    comentarios = models.TextField(null=True, blank=True)

    def __str__(self):
        id_processo = str(self.id_processo)
        return id_processo

    class Meta:
        verbose_name_plural = "Processo"