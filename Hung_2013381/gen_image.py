from io import BytesIO
from PIL import Image
import os
import numpy as np

current_directory = os.getcwd()
img_path = os.path.join(
    current_directory, 'gen', '128.jpg')


def create_large_image(width, height, file_size_mb):
    # Tính toán số lượng pixel cần có để đạt được kích thước file mong muốn
    # 3 bytes cho mỗi pixel (RGB)
    pixels = int((file_size_mb * 1024 * 1024) / 3)

    # Tạo ảnh với kích thước và chất lượng cao
    img = Image.new('RGB', (width, height), (255, 255, 255))

    # Tạo một mảng numpy với số lượng pixel cần thiết
    pixel_data = np.random.randint(0, 256, size=(pixels, 3), dtype=np.uint8)

    # Chia nhỏ mảng thành các phần nhỏ
    # Số lượng pixel mỗi lần đặt vào (điều chỉnh nếu cần thiết)
    chunk_size = 65536
    chunks = [pixel_data[i:i + chunk_size]
              for i in range(0, len(pixel_data), chunk_size)]

    # Gán dữ liệu pixel vào ảnh
    for chunk in chunks:
        img.putdata(list(map(tuple, chunk)))

    # Lưu ảnh vào một đối tượng BytesIO để lấy kích thước file
    img_bytes = BytesIO()
    img.save(img_bytes, format='JPEG')

    # Đưa con trỏ về đầu của đối tượng BytesIO để đọc
    img_bytes.seek(0)

    # Lưu ảnh thành file
    with open(img_path, 'wb') as f:
        f.write(img_bytes.read())


# Sử dụng hàm để tạo ảnh 128MB với kích thước 1920x1080
create_large_image(1920, 1080, 128)
