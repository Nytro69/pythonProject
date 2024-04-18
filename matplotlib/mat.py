import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

plt.plot(x, y1, label="Numbers")
plt.plot(x, y2, label="Square of numbers")
plt.legend()
plt.show()