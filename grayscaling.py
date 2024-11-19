# from PIL import Image
# import os
# import csv
# import numpy as np

# # Define the dataset directory
# dataset_dir = r"C:\Users\IdeaPad\Downloads\dataset2\Dataset BISINDO\datatrain\NOTHING"

# # CSV file to save the pixel data
# csv_file = "dataset2_train_NOTHING.csv"

# # Open the CSV file for writing
# with open(csv_file, mode="w", newline="") as file:
#     writer = csv.writer(file)
    
#     # Write the header (label, filename, pixel_1 to pixel_784)
#     writer.writerow(["label"] + [f"pixel_{i}" for i in range(1, 785)])
    
#     # Loop through the dataset folder
#     for subdir, _, files in os.walk(dataset_dir):
#         label = os.path.basename(subdir)  # Use folder name as label
#         if not label:  # Skip the root folder or empty labels
#             continue
#         for filename in files:
#             if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#                 try:
#                     # Load and process the image
#                     img_path = os.path.join(subdir, filename)
#                     image = Image.open(img_path).convert('L').resize((28, 28))  # Grayscale and resize to 28x28
#                     pixels = np.array(image).flatten()  # Flatten the image into a 1D array

#                     # Write label and pixel data to CSV
#                     writer.writerow(["27"] + pixels.tolist())
#                 except Exception as e:
#                     print(f"Error processing {filename}: {e}")

# print(f"Image pixel data saved to {csv_file}")

from PIL import Image
import os
import csv
import numpy as np
import pillow_heif  # Enables HEIC/HEIF support

# Define the dataset directory
dataset_dir = r"C:\Users\IdeaPad\Downloads\bisindo-dataset-noise"

# CSV file to save the pixel data
csv_file = "dataset_noise.csv"

# Open the CSV file for writing
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Write the header (label, filename, pixel_1 to pixel_784)
    writer.writerow(["label", "filename"] + [f"pixel_{i}" for i in range(1, 785)])
    
    # Loop through the dataset folder
    for subdir, dirs, files in os.walk(dataset_dir):
        for folder_name in sorted(dirs):  # Process subdirectories alphabetically
            print(f"Processing {folder_name}")
            folder_path = os.path.join(subdir, folder_name)
            if folder_name == 'NOTHING':
                label = 26
            else:
                label = ord(folder_name.upper()) - ord('A')  # Convert folder name to label (A=0, B=1, ..., Z=25)
            if 0 <= label <= 26:  # Ensure the folder is A-Z
                for filename in os.listdir(folder_path):
                    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.heic', '.heif')):
                        try:
                            # Load the image
                            img_path = os.path.join(folder_path, filename)
                            if filename.lower().endswith(('.heic', '.heif')):
                                heif_file = pillow_heif.read_heif(img_path)
                                image = Image.frombytes(
                                    heif_file.mode, heif_file.size, heif_file.data
                                )
                            else:
                                image = Image.open(img_path)
                            
                            # Process the image
                            image = image.convert('L').resize((28, 28))  # Grayscale and resize to 28x28
                            pixels = np.array(image).flatten()  # Flatten the image into a 1D array
                            
                            # Write label and pixel data to CSV
                            writer.writerow([label, filename] + pixels.tolist())
                        except Exception as e:
                            print(f"Error processing {img_path}: {e}")

print(f"Image pixel data saved to {csv_file}")
