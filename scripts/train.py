# scripts/train.py
import torch
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import numpy as np
from app.models.encoder import build_encoder
from app.models.decoder import build_decoder
from app.models.diffusion import LatentDiffusionModel

class ImageDataset(Dataset):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.filenames = [f for f in os.listdir(data_dir) if f.endswith('.npy')]

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, idx):
        img_path = os.path.join(self.data_dir, self.filenames[idx])
        img = np.load(img_path)
        return torch.tensor(img, dtype=torch.float32).permute(2, 0, 1) / 255.0

def train_model(data_dir, epochs=10, batch_size=32, lr=0.001):
    dataset = ImageDataset(data_dir)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    encoder = build_encoder()
    decoder = build_decoder()
    diffusion_model = LatentDiffusionModel()

    optimizer = optim.Adam(list(encoder.parameters()) + list(decoder.parameters()) + list(diffusion_model.parameters()), lr=lr)
    criterion = torch.nn.MSELoss()

    for epoch in range(epochs):
        for imgs in dataloader:
            optimizer.zero_grad()
            latents = encoder(imgs)
            latents = diffusion_model(latents)
            outputs = decoder(latents)
            loss = criterion(outputs, imgs)
            loss.backward()
            optimizer.step()
        
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

if __name__ == '__main__':
    train_model('data/preprocessed')
