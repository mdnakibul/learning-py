import numpy as np
import matplotlib.pyplot as plt

# Define constants for the hyperbola equation
a = 2  # Horizontal stretch
b = 3  # Vertical stretch

# Generate x values (we exclude values near 0 to avoid invalid sqrt)
x_positive = np.linspace(a + 0.1, 10, 500)  # Right branch of the hyperbola
x_negative = np.linspace(-10, -a - 0.1, 500)  # Left branch of the hyperbola

# Compute corresponding y values for both branches
y_positive_right = b * np.sqrt((x_positive**2 / a**2) - 1)
y_negative_right = -b * np.sqrt((x_positive**2 / a**2) - 1)

y_positive_left = b * np.sqrt((x_negative**2 / a**2) - 1)
y_negative_left = -b * np.sqrt((x_negative**2 / a**2) - 1)

# Plot the two branches of the hyperbola
plt.plot(x_positive, y_positive_right, color='b', label='Right Branch')
plt.plot(x_positive, y_negative_right, color='b')
plt.plot(x_negative, y_positive_left, color='r', label='Left Branch')
plt.plot(x_negative, y_negative_left, color='r')

# Customize the graph
plt.title("Hyperbola Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.axhline(0, color='black',linewidth=1)  # Horizontal axis
plt.axvline(0, color='black',linewidth=1)  # Vertical axis
plt.grid(True)
plt.legend()

# Display the graph
plt.show()
