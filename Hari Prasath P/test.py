import numpy as np
import matplotlib.pyplot as plt

# Create a range of values for theta
theta = np.linspace(0, 2 * np.pi, 1000)

# Parametric equations for the heart shape
x = 16 * np.sin(theta)**3
y = 13 * np.cos(theta) - 5 * np.cos(2 * theta) - 2 * np.cos(3 * theta) - np.cos(4 * theta)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='red')
plt.fill(x, y, color='red', alpha=0.6)

# Set equal scaling and remove axes
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')

# Show the plot
plt.show()
