import math
ang = int(input('Digite um angulo em °: '))
rad = math.radians(ang)
print('Para o ângulo de {}°, o seno vale {:.3f}, o cosseno vale {:.3f} e a tangente vale {:.3f}'.format(ang, math.sin(rad), math.cos(rad), math.tan(rad)))
