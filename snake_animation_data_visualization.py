import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Load Data
df = pd.read_csv("C:/Users/sharm/Downloads/2025-01-29 Modern Bhatti june-month_ vegetables prices(Sheet1).csv")

# Ensure proper column names
df.columns = df.columns.str.strip()

# Dummy Data for Animation (Replace with your actual DataFrame processing)
x_data = np.linspace(0, 10, num=50)  # X values (e.g., Dates)
y_data = np.sin(x_data)  # Y values (e.g., Prices)

# Create Figure
fig, ax = plt.subplots()
ax.set_xlim(min(x_data), max(x_data))
ax.set_ylim(min(y_data) - 1, max(y_data) + 1)
ax.set_xlabel("Dates")
ax.set_ylabel("Price per kg (Rs)")
ax.set_title("Vegetables Price Animation")

# Snake-like effect
num_points = 10  # Number of trailing points
snake_x = np.full(num_points, x_data[0])
snake_y = np.full(num_points, y_data[0])

# Create a line that will move
(line,) = ax.plot([], [], "ro-", markersize=8)  # 'ro-' -> Red circles connected

# Mouse tracking function
def on_mouse_move(event):
    if event.xdata is not None and event.ydata is not None:
        snake_x[:-1] = snake_x[1:]  # Shift x-values
        snake_y[:-1] = snake_y[1:]  # Shift y-values
        snake_x[-1] = event.xdata  # Update last x
        snake_y[-1] = event.ydata  # Update last y
        line.set_data(snake_x, snake_y)

# Connect mouse movement
fig.canvas.mpl_connect("motion_notify_event", on_mouse_move)

# Animation function (not needed for mouse tracking, but can smooth updates)
def animate(frame):
    line.set_data(snake_x, snake_y)
    return line,

ani = animation.FuncAnimation(fig, animate, interval=0.5, blit=True)


plt.grid(True)
plt.show()