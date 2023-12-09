import os

def create_file(file_name, size, folder):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(current_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'wb') as f:
        f.seek(size - 1)
        f.write(b'0')

# def create_multiple_files(num_files, file_size, folder):
#     for i in range(1, num_files + 1):
#         file_name = f"{i}.txt"
#         create_file(file_name, file_size, folder)


