from PIL import Image
import os
import csv
import numpy as np

# Define the dataset directory
dataset_dir = r"C:\Users\IdeaPad\Documents\ML\American-Sign-Language-Recognition-master\American-Sign-Language-Recognition-master\DATASET"
output_csv = "sign_language_dataset_pixels.csv"  # Update with the path to your images

# CSV file to save the pixel data
csv_file = "image_pixels.csv"

# Open the CSV file for writing
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Write the header (label, pixel_1 to pixel_784)
    writer.writerow(["label"] + ["filename"] + [f"pixel_{i}" for i in range(1, 785)])  # From pixel_1 to pixel_784
    
    # Loop through the dataset folder
    for subdir, _, files in os.walk(dataset_dir):
        label = os.path.basename(subdir)  # Use folder name as label
        for filename in files:
            if filename.endswith(".jpg"):
                # Load and process the image
                img_path = os.path.join(subdir, filename)
                image = Image.open(img_path).convert('L').resize((28, 28))  # Grayscale and resize to 28x28
                pixels = np.array(image).flatten()  # Flatten the image into a 1D array
                
                # Write label and pixel data to CSV
                writer.writerow([label] + [filename] + pixels.tolist())

print(f"Image pixel data saved to {csv_file}")
