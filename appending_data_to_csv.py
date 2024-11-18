import pandas as pd

# File paths
existing_file = "bisindo_dataset_image_pixels_test.csv"  # The file you want to append data to
new_file = "dataset1_test.csv"            # The file containing new data
output_file = "bisindo_dataset_test_2data.csv"     # Output file (optional, can overwrite existing_file)

# Read the existing data
try:
    existing_data = pd.read_csv(existing_file)
except FileNotFoundError:
    print(f"{existing_file} not found. Creating a new file.")
    existing_data = pd.DataFrame()  # If the file doesn't exist, create an empty DataFrame

# Read the new data
new_data = pd.read_csv(new_file)

# Append the new data to the existing data
combined_data = pd.concat([existing_data, new_data], ignore_index=True)

# Save the combined data back to a CSV file
combined_data.to_csv(output_file, index=False)
print(f"Data appended and saved to {output_file}")
