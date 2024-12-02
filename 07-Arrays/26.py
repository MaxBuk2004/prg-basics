import numpy as np
import matplotlib.pyplot as plt

angles_degrees = np.arange(0, 361, 1)

angles_radians = np.radians(angles_degrees)

y_values = np.sin(angles_radians)

plt.plot(angles_degrees, y_values)

plt.title("Graph of y = sin(x)")
plt.xlabel("Angle (degrees)")
plt.ylabel("y = sin(x)")

plt.grid(True)

plt.show()