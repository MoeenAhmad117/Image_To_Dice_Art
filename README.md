
# Dice Art from Image

This project allows you to convert any image into a representation of dice faces, transforming the image into a grid where each value corresponds to a dice face (from 1 to 6). This transformation scales the grayscale intensity of the pixels into these discrete dice values. The result can be visualized as a new image, where the grayscale has been adjusted to reflect these dice face values.

## Prerequisites

Before you start, ensure you have Python installed on your machine. You will also need to install the following Python libraries:

```bash
pip install Pillow numpy
```

## How to Use

To use this script, you need an image file in a format that PIL can open (like JPEG, PNG, etc.). Place the image in the same directory as the script or specify the path to the image.

1. **Load and Convert the Image**: The image is loaded and converted to grayscale.
2. **Resize the Image**: Optionally, you can resize the image to your preferred dimensions. It is resized to a square to maintain aspect ratio simplicity.
3. **Convert Image to Array**: The grayscale image is then converted into a numpy array.
4. **Scale the Array**: The array values are scaled to range from 1 to 6, corresponding to dice faces.
5. **Visualize the Result**: The scaled array can be visualized by mapping the dice numbers back to a grayscale range and converting it back to an image.
6. **Save and Display**: The result can be saved and displayed.

### File Descriptions

- `script.py`: The main Python script to transform the image.
- `messi_image.jpeg`: Example input image file.
- `processed_image.png`: The output image showing the dice representation.
- `scaled_image_array.txt`: Text file containing the scaled array values.

### Example Usage

```python
python script.py
```

This will process the image named `messi_image.jpeg` in the same directory as the script and output `processed_image.png` and `scaled_image_array.txt`.

## Customization

You can customize the input image and the size to which the image is resized by modifying the following lines in the script:

```python
img = Image.open("your_image.jpeg").convert('L')
new_width = 300  # change this to desired width
new_height = 300  # change this to desired height
```

## Output

The output includes:
- A visual representation of the image scaled to dice values (`processed_image.png`).
- A text file containing the matrix of dice values (`scaled_image_array.txt`).

## Contributing

Feel free to fork this project and make changes. You can submit pull requests if you want to add features or fix bugs.
