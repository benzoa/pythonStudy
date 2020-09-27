import matplotlib.pyplot as plt
import random

result = []
for i in range(13):
    result.append(random.randint(1, 1000))

print(sorted(result))

plt.style.use('ggplot')
plt.figure(figsize=(5, 2.5), dpi=200)
plt.boxplot(result, showfliers=False)
plt.show()
