''' programa sem importação de bibliotecas

CO = float(input('Comprimento do cateto oposto: '))
CA = float(input('Comprimento do cateto adjacente: '))

HIP = ((CO)**2 + (CA)**2)**(1/2)
print('A hipotenusa vai medir {:.3f}.'.format(HIP))


 programa com importação de biblioteca MATH '''
from math import hypot

CO = float(input('Comprimento do cateto oposto: '))
CA = float(input('Comprimento do cateto adjacente: '))

HIP = hypot(CO, CA)
print('A hipotenusa vai medir {:.3f}.'.format(HIP))
