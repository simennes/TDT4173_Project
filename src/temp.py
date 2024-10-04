import zipfile
import os

# Define the path to the file and the output zip file
input_file = '/data/ais_train.csv'
output_zip = '/data/ais_train.zip'

print("hei")

# Create a ZipFile object
with zipfile.ZipFile(output_zip, 'w') as zipf:
    # Add the file to the zip file
    zipf.write(input_file, os.path.basename(input_file))

print(f"Zipped {input_file} to {output_zip}")