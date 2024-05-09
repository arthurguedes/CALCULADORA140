import pytest
from calculadora.calculadora.calculadora import somar_dois_numeros,subtrair_dois_numeros,multiplicar_dois_numeros,dividir_dois_numeros
from utils.utils import ler_csv     # função de leitura de arquivos csv

def test_somar_dois_numeros():
    num1 = 5 
    num2 = 7
    resultado_esperado = 12 

    resultado_obtido = somar_dois_numeros(num1,num2) 

    assert resultado_esperado == resultado_obtido

def test_subtrair_dois_numeros():
    num1 = 10 
    num2 = 6 
    resultado_esperado = 4

    resultado_obtido = subtrair_dois_numeros(num1,num2)

    assert resultado_esperado == resultado_obtido

    
def test_multiplicar_dois_numeros():
    num1 = 3 
    num2 = 9 
    resultado_esperado = 27

    resultado_obtido = multiplicar_dois_numeros(num1,num2)

    assert resultado_esperado == resultado_obtido

def test_dividir_dois_numeros():
    num1 = 64
    num2 = 4
    resultado_esperado = 16

    resultado_obtido = dividir_dois_numeros(num1,num2)

    assert resultado_esperado == resultado_obtido


# Test Baseados em Dados = Data Driven Tests (DDT) --> Massa de Teste 
    # Dados em uma lista 
    # Dados em um arquivo, vários formatos: csv , json , xml , dat 

@pytest.mark.parametrize('num1, num2, resultado_esperado',
                         [
                            (5,7,12),
                            (0,8,8),
                            (10, -15, -5),
                            (6, 0.75, 6.75)  
                         ]
                        )

def test_somar_dois_numeros_lista(num1, num2, resultado_esperado):
    #num1 = 5 
    #num2 = 7
    #resultado_esperado = 12 

    resultado_obtido = somar_dois_numeros(num1,num2) 

    assert resultado_esperado == resultado_obtido


@pytest.mark.parametrize('num1, num2, resultado_esperado',
                            ler_csv('./fixtures/massa_somar.csv') 
                         )

def test_somar_dois_numeros_lista_csv(num1, num2, resultado_esperado):
    #num1 = 5 
    #num2 = 7
    #resultado_esperado = 12 

    resultado_obtido = somar_dois_numeros(float(num1),float(num2)) 

    assert float(resultado_esperado) == resultado_obtido

   
def test_dividir_por_zero():
    num1 = 64
    num2 = 0
    resultado_esperado = "Não é possível dividir por zero"

    resultado_obtido = dividir_dois_numeros(num1,num2)

    assert resultado_esperado == resultado_obtido