import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Open an image file
image = Image.open('intersecting_cropped.png')
image_array = np.array(image)

# Display the image
fig, ax = plt.subplots()
ax.imshow(image_array)

# Function to handle click events
def onclick(event):
    x, y = int(event.xdata), int(event.ydata)
    pixel_value = image_array[y, x]
    print(f'Pixel selected at ({x}, {y}) with value {pixel_value}')

# Connect the click event to the handler
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()