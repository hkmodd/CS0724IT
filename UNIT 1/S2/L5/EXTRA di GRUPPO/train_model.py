import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from simple_cnn import SimpleCNN  # Importa SimpleCNN dal nuovo file

def train_model():
    transform = transforms.Compose([transforms.Resize((32, 32)), transforms.ToTensor()])
    train_dataset = datasets.ImageFolder('dataset/train', transform=transform)
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)

    model = SimpleCNN()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(10):  # Numero di epoche
        for data, target in train_loader:
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
        print(f"Epoca {epoch + 1}, Loss: {loss.item()}")

    torch.save(model.state_dict(), 'pattern_recognition_model.pth')

if __name__ == "__main__":
    train_model()
