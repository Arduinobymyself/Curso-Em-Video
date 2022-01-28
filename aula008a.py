#import math
from math import sqrt, floor
num = int(input('Digite um número'))
#raiz = math.sqrt(num)
raiz = sqrt(num)
#print('A rais de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A rais de {} é igual a {}'.format(num, floor(raiz)))
