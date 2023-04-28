 
import os

# Define the root directory
root_dir = os.getcwd()

# Define the subdirectories to be created
subdirs = ['data', 'models', 'reports']

# Loop through the subdirectories and create them if they don't exist
for subdir in subdirs:
    dir_path = os.path.join(root_dir, subdir)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    # Add empty files to each subdirectory
    file_names = ['data.txt', 'model.pkl', 'report.txt']
    for file_name in file_names:
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'w') as f:
            pass
