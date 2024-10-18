import matplotlib
matplotlib.use('TkAgg')  # Use an interactive backend
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(2 * x)
y2 = np.cos(x)
y3 = np.sin(x + np.pi / 4)

# Create the plot
plt.figure()

plt.plot(x, y1, label='sin(2 * x)')
plt.plot(x, y2, label='cos(x)')
plt.plot(x, y3, label='sin(x + π/4)')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Graph with Intersecting Lines')

# Save the plot to a file
plt.savefig('intersecting_rgb.png')

# load graph from image and convert to black and white
image = Image.open('intersecting_rgb.png')
grey_image = image.convert('L')   # applies greyscale not b/w
print(grey_image.getpixel((0, 0)))

threshold = 255
bw_image = grey_image.point(lambda p: 255 if p >= threshold else 0)
bw_image.save('intersecting_bw.png')

# crop image to remove axes
crop_image = bw_image.crop((82, 60, 562, 420))
crop_image.save('intersecting_cropped.png')
crop_image.show()




