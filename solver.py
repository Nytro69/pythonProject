import matplotlib.pyplot as plt
import numpy as np

# Define the range for x
x_values = np.linspace(-5, 2, 400)
y_values = func(x_values)

# Plot the function
plt.plot(x_values, y_values, label='f(x) = x - (x + 3)**90')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = x - (x + 3)^90')
plt.legend()
plt.grid(True)
plt.show()