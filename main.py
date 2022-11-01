# Arquivo principal das soluções do trabalho final proposto

import pontos_equidistantes as pe
import area_das_secoes_spline as adss
import area_das_secoes as ads
import orbita_simples as os
import orbita_pontual as op
import spline_cubica as sc
import numpy as np
import integracaoSpline
import integracao
import matriz


ABC = matriz.calculaABC()  # Recebe a matriz dos sistemas lineares já resolvida
# Faz-se o cálculo para achar os parâmetros xc, a, b
yc = 0  # coordenada y do centro
xc = - ABC[1] / float(2 * ABC[0])  # coordenada x do centro
a = np.sqrt(xc**2 - ABC[2] / ABC[0])  # calcula semi-eixo maior
b = a * np.sqrt(- ABC[0])  # calcula semi-eixo menor


# Chama a função que constrói o gráfico da órbita simples do satélite
angle = np.linspace(0, 2 * np.pi, 75)
e = np.sqrt(1 - (b ** 2 / a ** 2))  # calcula a excentricidade
f = a * e  # calcula o foco
print("Coordenada Y do centro: ", str(yc) + "km")
print("Coordenada X do centro: ", str(xc) + "km")
print("Semi-eixo maior: ", str(a) + "km")
print("Semi-eixo menor: ", str(b) + "km")
print("Excentricidade: ", e)
print("Distância focal: ", str(f) + "km")
os.orbitaSimples(xc, a, b, f, angle)


# Chama a função que faz todos os cálculos necessários para construir os pontos equidistantes em tempo
a *= 1000  # transformando a em metros
b *= 1000  # transformando b em metros
xc *= 1000  # transformando xc em metros
f *= 1000  # transformando f em metros
x, y = pe.calculaPontosEquidistantes(a, e, xc, f)


# Chama a função que constrói o gráfico da órbita pontual do satélite
op.orbitaPontual(xc, a, b, f, angle, x, y)


# Provando que o satélite percorre áreas iguais em tempos iguais com a função da elipse
def funcaoDaElipse(X):
    # np.sqrt(ABC[0]*X*X + ABC[1]*X + ABC[2]  Equação da elipse com os parâmetros em km
    return np.sqrt(ABC[0]*X*X + ABC[1]*1e3*X + ABC[2]*1e6)  # Equação manipulada para os parâmetros em m


# Área de uma seção entre dois pontos equidistantes em tempo
area1 = integracao.integral(funcaoDaElipse, x[2], x[1])
area2 = (((f + xc) - x[1]) * funcaoDaElipse(x[1])) / 2.0
area3 = (((f + xc) - x[2]) * funcaoDaElipse(x[2])) / 2.0
areatotal1 = area1 + area2 - area3
print("Área da seção Tx1x2: ", str(areatotal1) + "m^2")
# Área de outra seção entre dois pontos equidistantes em tempo aos pontos anteriores
area4 = integracao.integral(funcaoDaElipse, x[8], x[7])
area5 = (((f + xc) - x[7]) * funcaoDaElipse(x[7])) / 2.0
area6 = (((f + xc) - x[8]) * funcaoDaElipse(x[8])) / 2.0
areatotal2 = area4 + area5 - area6
print("Área da seção Tx7x8: ", str(areatotal2) + "m^2")
# OBS: PARA O CÁLCULO DE SEÇÕES ABAIXO DO EIXO X, INVERTER O INTERVALO DE INTEGRAÇÃO
# EXEMPLO: AO INVÉS DE INTEGRAR DE X[2] A X[1], INTEGRAR DE X[18] A X[19]
# SE SE DESEJA UTILIZAR O PONTO X[15] PARA CALCULAR UMA SEÇÃO, É NECESSÁRIO ADOTAR
# UM NOVO MÉTODO PARA CALCULAR A ÁREA

ads.calculoDaArea(xc, a, b, f, angle, x, y)
ads.areaDasSecoes(xc, a, b, f, angle, x, y, ABC)


# Chama a função de spline cúbica que interpola os pontos 1, 2, 3 e 4 equidistantes da elipse
vetorX = [x[1], x[2], x[3], x[4]]
vetorY = [y[1], y[2], y[3], y[4]]
matriz = sc.splineCubica(vetorX, vetorY)  # Matriz dos coeficientes da Spline Cúbica
print("Matriz dos Coeficientes: ", matriz)


# Função da Spline com alguns parâmetros(Polinômio de terceiro grau)
def funcaoSpline(X, vetorX, matriz, k):
    h = X - vetorX[k]
    return matriz[k, 0] + h*(matriz[k, 1] + h*(matriz[k, 2] + h*matriz[k, 3]))


# Área da integral entre os pontos 1 e 4
AreaSpline1 = 0
AreaSpline1 += integracaoSpline.integral(funcaoSpline, vetorX[1], vetorX[0], vetorX, matriz, 0)
AreaSpline1 += integracaoSpline.integral(funcaoSpline, vetorX[2], vetorX[1], vetorX, matriz, 1)
AreaSpline1 += integracaoSpline.integral(funcaoSpline, vetorX[3], vetorX[2], vetorX, matriz, 2)
Area2 = (((f + xc) - x[1]) * y[1]) / 2.0
Area3 = (((f + xc) - x[4]) * y[4]) / 2.0

AreaSplineTotal = AreaSpline1 + Area2 - Area3
print("Área da seção Tx1x4 pela Spline Cúbica: ", str(AreaSplineTotal) + "m^2")

# Calculando a área entre os pontos 1 e 4 pela função da elipse
AreaEquacao = integracao.integral(funcaoDaElipse, x[10], x[7])
Area4 = (((f + xc) - x[7]) * y[7]) / 2.0
Area5 = (((f + xc) - x[10]) * y[10]) / 2.0
AreaEquacaoTotal = AreaEquacao + Area4 - Area5
print("Área da seção Tx7x10 pela Equação da Elipse: ", str(AreaEquacaoTotal) + "m^2")

adss.areaPelaSpline(xc, a, b, f, angle, funcaoSpline, vetorX, vetorY, matriz)
