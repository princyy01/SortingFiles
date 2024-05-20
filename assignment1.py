import os
import shutil

# Define paths
desktop = r"C:\Users\KIIT\OneDrive\Desktop"  
test_folder = os.path.join(desktop, 'test')
mixed_files_folder = os.path.join(desktop, 'mixed files')

# Create folders if they don't exist
os.makedirs(test_folder, exist_ok=True)
os.makedirs(mixed_files_folder, exist_ok=True)

# Create sample files in the mixed files folder
file_content = "Sample content"
file_types = {
    'text_files': ['file1.txt', 'file2.txt'],
    'pdf_files': ['file1.pdf', 'file2.pdf'],
    'image_files': ['file1.jpg', 'file2.jpg', 'file1.png', 'file2.png', 'file1.jpeg']
}

for category, files in file_types.items():
    for file in files:
        file_path = os.path.join(mixed_files_folder, file)
        with open(file_path, 'w') as f:
            f.write(file_content)

# Define the target folders within the test folder
subfolders = {
    'text_files': ['.txt'],
    'pdf_files': ['.pdf'],
    'image_files': ['.jpg', '.jpeg', '.png']
}

# Create subfolders if they don't exist
for folder in subfolders:
    os.makedirs(os.path.join(test_folder, folder), exist_ok=True)

# Move files to their respective subfolders
for filename in os.listdir(mixed_files_folder):
    file_path = os.path.join(mixed_files_folder, filename)
    file_ext = os.path.splitext(filename)[1].lower()

    # Determine the target subfolder based on file extension
    for folder, extensions in subfolders.items():
        if file_ext in extensions:
            target_path = os.path.join(test_folder, folder, filename)
            shutil.move(file_path, target_path)
            print(f"Moved {filename} to {folder}")
            break
