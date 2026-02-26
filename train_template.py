# 1️⃣ Import necessary libraries / 載入必要的套件
import torch
import torchvision
import wandb

# 2️⃣ Initialize wandb with project name and config / 初始化 wandb，設定專案名稱與超參數設定
wandb.init(project="your_project_name", config={...})

# 3️⃣ Set device (GPU if available) / 設定裝置（優先使用 GPU）
device = torch.device("cuda" if cuda_available else "cpu")

# 4️⃣ Load dataset with transform / 載入資料集並套用轉換（transform）
dataset = torchvision.datasets.MNIST(..., transform=ToTensor, download=True)

# 5️⃣ Create DataLoader for batch processing / 建立 DataLoader 進行批次處理
loader = DataLoader(dataset, batch_size=..., shuffle=True)

# 6️⃣ Define MLP model / 定義 MLP 模型
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        # define layers... / 定義各層...
    def forward(self, x):
        return output

model = MLP().to(device)

# 7️⃣ Define loss function and optimizer / 定義損失函數與優化器
loss_fn = CrossEntropyLoss()
optimizer = Adam(model.parameters(), lr=...)

# 8️⃣ Training loop for multiple epochs / 執行多個 epoch 的訓練迴圈
for epoch in range(num_epochs):
    for batch in loader:
        images, labels = batch
        # move to device / 移至裝置（GPU/CPU）

        predictions = model(images)
        loss = loss_fn(predictions, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # compute accuracy / 計算準確率
    # log {"loss": ..., "accuracy": ...} to wandb / 將 loss 與 accuracy 記錄至 wandb

# 9️⃣ Save model parameters / 儲存模型參數
torch.save(model.state_dict(), "model.pt")
