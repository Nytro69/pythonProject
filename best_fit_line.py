import matplotlib.pyplot as plt
import numpy as np

coordinates = [(1, 1.5), (2, 3.8), (3, 6.7), (4, 9), (5, 11.2), (6, 13.6), (7, 16)]

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0
n = len(coordinates)

for (x, y) in coordinates:
    sum_y += y
    sum_x += x
    sum_xy += x * y
    sum_x_squared += x**2

m = n*sum_xy - sum_x * sum_y
m = m/(n*sum_x_squared-sum_x**2)

def my_function(x):
    return m*x + b

b = (sum_y - m * sum_x)/n

x_values = [x for x, _ in coordinates]
y_values = [y for _, y in coordinates]

plt.plot(x_values, y_values, 'bo', label='Coordinates')

x = np.linspace(min(x_values), max(x_values), 100)
y = my_function(x)
plt.plot(x, y, 'r-', label='Function')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('My Graph')
plt.legend()

plt.show()