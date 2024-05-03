import pytest
from calculadora.calculadora import somar_dois_numeros,subtrair_dois_numeros,multiplicar_dois_numeros,dividir_dois_numeros

def test_somar_dois_numeros():
    num1 = 5 
    num2 = 7
    resultado_esperado = 12 

    resultado_obtido = somar_dois_numeros(num1,num2) 

    assert resultado_esperado == resultado_obtido

    
    


