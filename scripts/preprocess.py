# scripts/preprocess.py
import os
from PIL import Image
import numpy as np

def preprocess_images(input_dir, output_dir, image_size=(128, 128)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path).convert('RGB')
            img = img.resize(image_size)
            img_array = np.array(img)
            output_path = os.path.join(output_dir, filename)
            np.save(output_path, img_array)
            print(f'Processed {filename}')

if __name__ == '__main__':
    preprocess_images('data/observed', 'data/preprocessed')
