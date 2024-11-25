# importing required libraries 
import matplotlib.pyplot as plt
import numpy as np
x = [1, 4, 9, 16]
y = [1, 2, 3, 4]
plt.plot(x, y) # Plot the chart
# plt.show() # display

# Generate x values (from 0 to 4π with small steps)
# x = np.linspace(0, 4 * np.pi, 1000)

# Generate y values (sine wave)
# y = np.sin(x)

# Plot the sine wave
# plt.plot(x, y, label='Sine Wave', color='b', linewidth=2)

# Customize the graph
# plt.title("Sine Wave Graph")
# plt.xlabel("X values")
# plt.ylabel("Y values (sin(x))")
# plt.grid(True)
# plt.axhline(0, color='black',linewidth=1)  # Add a horizontal axis
# plt.axvline(0, color='black',linewidth=1)  # Add a vertical axis
# plt.legend()

plt.show()