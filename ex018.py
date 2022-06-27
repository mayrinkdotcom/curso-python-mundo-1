import math

ANGULO = float(input('Digite um ângulo(em graus): '))
ANGULO_RAD = math.radians(ANGULO)
SEN = math.sin(ANGULO_RAD)
COS = math.cos(ANGULO_RAD)
TAN = math.tan(ANGULO_RAD)

print('Ângulo: {}.\nSeno: {:.3f}.\nCosseno: {:.3f}.\nTangente: {:.3f}.'.format(ANGULO, SEN, COS, TAN))
