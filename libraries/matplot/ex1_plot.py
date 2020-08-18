import matplotlib.pyplot as plt

plt.figure(figsize = (10, 3))
plt.rc('font', family = 'Malgun Gothic')
plt.title('legend')

plt.plot([10, 20, 30, 40], color='skyblue', linestyle='--', label = 'asc')
plt.plot([40, 30, 20, 10], 'green', ls=':', label = 'desc')
plt.plot([5, 15, 25, 35], 'r.', label = 'cicle')
plt.plot([37, 27, 17, 7], 'y^', label = 'triangle')

plt.legend()
plt.show()
