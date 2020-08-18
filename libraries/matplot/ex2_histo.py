import matplotlib.pyplot as plt
import random

dice = []
for i in range(10000):
    dice.append(random.randint(1, 6))

# bins : 가로 구간 개수
plt.hist(dice, bins=6, color="r")
plt.show()
