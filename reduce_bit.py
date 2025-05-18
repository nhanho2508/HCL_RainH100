import os
from PIL import Image

def reduce_bit_depth_to_8(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            
            # Chuyển ảnh về chế độ 8-bit (256 màu)
            img_8bit = img.convert('P', palette=Image.ADAPTIVE, colors=256)
            
            # Lưu ảnh vào folder output
            output_path = os.path.join(output_folder, filename)
            img_8bit.save(output_path)
            print(f"Processed and saved: {output_path}")

# Sử dụng hàm
input_folder = 'C:/Users/ADMIN/source/repos/HCL_new/HCL/mask'

reduce_bit_depth_to_8(input_folder, input_folder)