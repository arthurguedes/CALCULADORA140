import pytest
from calculadora.calculadora.calculoarea import calcular_quadrado,calcular_retangulo,calcular_triangulo
from utils.utils import ler_csv

def test_calcular_quadrado():
    lado = 10
    area_esperada = 100

    area_calculada = calcular_quadrado(lado)

    assert area_calculada == area_esperada

def test_calcular_retangulo():
    largura = 10
    comprimento = 20
    area_esperada = 200

    area_calculada = calcular_retangulo(largura,comprimento)

    assert area_calculada == area_esperada

def test_calcular_triangulo():
    base = 10
    altura = 20
    area_esperada = 100

    area_calculada = calcular_triangulo(base,altura)

    assert area_calculada == area_esperada

@pytest.mark.parametrize('lado, resultado_esperado',
                         [
                            (5,25),
                            (8,64),
                            (10,100),
                            (6,36)  
                         ]
                        )

def test_calcular_quadrado_lista(lado, resultado_esperado):

    resultado_obtido = calcular_quadrado(lado) 

    assert resultado_esperado == resultado_obtido


@pytest.mark.parametrize('base, altura, area_esperada',
                            ler_csv('./fixtures/massa_triangulo.csv') 
                         )

def test_calcular_triangulo_csv(base, altura, area_esperada):
    
    resultado_obtido = calcular_triangulo(int(base),int(altura))

    assert resultado_obtido == int(area_esperada)
