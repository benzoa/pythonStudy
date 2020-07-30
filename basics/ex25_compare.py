import math, sys
from decimal import Decimal
from fractions import Fraction

print(0.1 + 0.2 == 0.3)

x = 0.1 + 0.2
print(math.fabs(x - 0.3) <= sys.float_info.epsilon)

print(math.isclose(0.1 + 0.2, 0.3))

print(Decimal('0.1') + Decimal('0.2'))

print(Fraction('10/3'))