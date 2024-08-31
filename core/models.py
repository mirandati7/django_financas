from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100) 

    def __str__(self):
        return self.nome

class Conta(models.Model):
    nome = models.CharField(max_length=100) 

    def __str__(self):
        return self.nome
    
ATIVO_INATIVO = (
    ('A', 'Ativo'),
    ('I', 'Inativo')
)   

CREDITO_DEBITO = (
    ('C', 'Crédito'),
    ('D', 'Débito')
)


class LancamentoFinanceiro(models.Model):
    valor = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    data = models.DateField()
    # C = Credito   | D = Debito
    credito_debito = models.CharField(("Operação"),max_length=1,choices=CREDITO_DEBITO, default='C')
    historico = models.CharField(max_length=100, default=None)
    # A = Ativo  | I - Inativo
    ativo_inativo = models.CharField(max_length=1,choices=ATIVO_INATIVO, default='A')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)

    def __str__(self):
        return self.historico 




