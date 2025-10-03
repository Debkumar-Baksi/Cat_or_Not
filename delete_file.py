import os
folder_path = "dataset/train/not_cats"
num_files_to_delete = 3326

files = os.listdir(folder_path)

files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

for file in files[:num_files_to_delete]:
    file_path = os.path.join(folder_path, file)
    try:
        os.remove(file_path)
        # print(f"Deleted: {file}")
    except Exception as e:
        print(f"Error deleting {file}: {e}")

print(f"Deleted {min(num_files_to_delete, len(files))} files.")