import zipfile
import os

# Define the path to the file and the output zip file
input_file = 'data/ais_train.csv'
output_zip = 'data/ais_train.zip'

# Ensure the directory exists
output_dir = os.path.dirname(output_zip)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a ZipFile object with compression enabled
with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Add the file to the zip file with compression
    zipf.write(input_file, os.path.basename(input_file))

print(f"Zipped {input_file} to {output_zip} with compression")
