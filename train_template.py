# 1️⃣ Import necessary libraries
import torch
import torchvision
import wandb

# 2️⃣ Initialize wandb with project name and config
wandb.init(project="your_project_name", config={...})

# 3️⃣ Set device (GPU if available)
device = torch.device("cuda" if cuda_available else "cpu")

# 4️⃣ Load dataset with transform
dataset = torchvision.datasets.MNIST(..., transform=ToTensor, download=True)

# 5️⃣ Create DataLoader for batch processing
loader = DataLoader(dataset, batch_size=..., shuffle=True)

# 6️⃣ Define MLP model
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        define layers...
    def forward(self, x):
        return output

model = MLP().to(device)

# 7️⃣ Define loss function and optimizer
loss_fn = CrossEntropyLoss()
optimizer = Adam(model.parameters(), lr=...)

# 8️⃣ Training loop for multiple epochs
for epoch in range(num_epochs):
    for batch in loader:
        images, labels = batch
        move to device

        predictions = model(images)
        loss = loss_fn(predictions, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    compute accuracy
    log {"loss": ..., "accuracy": ...} to wandb

# 9️⃣ Save model parameters
torch.save(model.state_dict(), "model.pt")
