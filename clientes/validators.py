import re #usado para importar expressoes regurares
from validate_docbr import CPF



def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)    
        
def nome_valido(nome):
    return nome.isalpha()

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

def celular_valido(numero_celular):
    """Verifica se o celular é válido (11 98996-2876)"""
    #Ex do modelo [0-9] -> indica que posso colocar numeros de 0 até o 9
    #Ex {2} -> indica que vou colocar dois numeros
    #ex ' ' ou ' - ' se eu colocar espaço ou traço ele identifica que deve aparecer como máscara também
    
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular) # verificando se o numero se enquadra no moelo
    return resposta

