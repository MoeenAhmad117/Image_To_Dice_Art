from PIL import Image, ImageFilter
import numpy as np

# Load the image
img = Image.open("messi_image.jpeg").convert('L')  # Convert to grayscale

# Resize the image (optional)
new_width = 300  # Example width
new_height = 300  # Example height
img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

# Convert the image to a numpy array
img_array = np.array(img)

# Scale the values to 1-6 (corresponding to dice faces)
scaled_img_array = np.floor(img_array / 256 * 6) + 1
scaled_img_array = np.clip(scaled_img_array, 1, 6).astype(int)

# Optionally, visualize the result
visualization_array = (scaled_img_array - 1) * (255 // 5)
result_img = Image.fromarray(np.uint8(visualization_array))

# Save the resulting image
result_img.save("processed_image.png")

# Show the resulting image
result_img.show()

# Save the scaled image array to a text file
np.savetxt("scaled_image_array.txt", scaled_img_array, fmt="%d")

# Print the scaled image array
print(scaled_img_array)
