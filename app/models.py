from django.db import models

class Empresa(models.Model):
    razao_social = models.CharField(max_length=255)
    nome_responsavel = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=18)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.razao_social

class Vaga(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    funcao = models.CharField(max_length=255)
    escolaridade_minima = models.CharField(max_length=50)
    experiencia_necessaria = models.BooleanField(default=False)
    quantidade_vagas = models.IntegerField()
    descricao = models.TextField()
    data_limite = models.DateField()
    sexo_desejado = models.CharField(max_length=20, blank=True, null=True)
    jornada_trabalho = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    beneficios = models.TextField()

    def __str__(self):
        return self.funcao