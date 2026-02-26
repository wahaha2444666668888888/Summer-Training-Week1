# 🧠 Summer Training Week 1 — MNIST MLP 實作與開發工具實戰 / MNIST MLP Implementation & Dev Tools Bootcamp

## 🎯 課程目標 / Course Objectives

本週目標為完成一個手寫數字辨識模型（使用 MNIST 或 FashionMNIST 資料集），並實作機器學習專案常見工具的整合與實作流程：

This week's goal is to build a handwritten digit recognition model (using the MNIST or FashionMNIST dataset) and integrate the common tools used in machine learning projects:

- 熟悉 TWCC 環境建置與 GPU 使用 / Set up and use GPUs in the TWCC environment
- 使用 GitHub 進行開發協作與版本控制 / Use GitHub for collaborative development and version control
- 使用 tmux 管理訓練任務不中斷 / Use tmux to keep training jobs running without interruption
- 使用 `nvidia-smi` 監控 GPU 使用狀況 / Monitor GPU usage with `nvidia-smi`
- 使用 Weights & Biases（wandb）進行訓練記錄與可視化 / Log and visualize training results with Weights & Biases (wandb)

---

## 🧪 作業內容 / Assignment

請完成一個使用 PyTorch 架設的簡單 MLP 模型，訓練資料集為 `FashionMNIST`（如有問題可改為 `MNIST`）。

Please implement a simple MLP model using PyTorch, trained on `FashionMNIST` (you may switch to `MNIST` if needed).

實作功能需包含：/ Required features:

- 基本資料讀取與前處理 / Basic data loading and preprocessing
- 模型架構建立（可自訂層數）/ Define a model architecture (customizable number of layers)
- 訓練與計算 loss / accuracy / Training loop with loss and accuracy computation
- 使用 `wandb.log()` 記錄實驗結果 / Log experiment results using `wandb.log()`
- 模型儲存為 `model.pt` / Save the model as `model.pt`

可參考範例程式：`train_template.py` / Reference template: `train_template.py`

---

## 🧰 工具要求 / Required Tools

| 工具 / Tool | 使用說明 / Description                                                                                        |
|-------------|---------------------------------------------------------------------------------------------------------------|
| TWCC        | 建立 GPU 計算環境並執行訓練任務 / Set up a GPU compute environment and run training jobs                      |
| tmux        | 使用 `tmux new -s <name>` 開啟 session，訓練不中斷 / Open a session with `tmux new -s <name>` to keep jobs running |
| nvidia-smi  | 監控 GPU 使用情況，請附上執行時截圖或 log / Monitor GPU usage; attach a screenshot or log                    |
| wandb       | 使用 `wandb.log()` 上傳 loss / acc，登入後可產生線上儀表板 / Upload loss/acc with `wandb.log()`; generates an online dashboard after login |
| GitHub      | 使用 branch → commit → PR → review → merge 的開發流程提交作業 / Submit via the branch → commit → PR → review → merge workflow |

---

## 👨‍💻 GitHub 作業繳交方式 / How to Submit via GitHub

請依照以下步驟提交作業：/ Please follow these steps to submit your assignment:

### 🪜 操作流程（Clone → Branch → Commit → PR）/ Workflow (Clone → Branch → Commit → PR)

```bash
# 1. Clone 作業倉庫 / Clone the assignment repository
git clone https://github.com/ccuvislab/Summer-Training-Week1.git
cd Summer-Training-Week1

# 2. 建立你的個人分支（命名建議：student_你的名字/week1）
#    Create your personal branch (suggested name: student_yourname/week1)
git checkout -b student_yourname/week1

# 3. 建立個人資料夾（命名建議：student_你的名字_week1）
#    Create your personal folder (suggested name: student_yourname_week1)
mkdir student_yourname_week1
# 將所有作業內容放入該資料夾 / Place all assignment files inside this folder

# 範例資料夾結構 / Example folder structure
Summer-Training-Week1/
├── train_template.py
└── student_david_week1/
    ├── train_mnist.py
    ├── wandb_link.txt
    ├── nvidia-smi.png
    ├── result_log.txt
    └── requirements.txt

# 推送與發 PR / Push and open a PR
git add student_yourname_week1/
git commit -m "完成 Week1 作業 - MLP 模型與訓練記錄 / Complete Week1 assignment - MLP model and training log"
git push origin student_yourname/week1
```

### 📋 注意事項 / Important Notes

- 每位學生只能修改自己的資料夾 / Each student may only modify their own folder
- 請確保程式碼可以順利執行 / Ensure your code runs successfully
- 請附上你的 `requirements.txt`，建議在虛擬環境中完成作業（如 conda）/ Include your `requirements.txt`; using a virtual environment (e.g., conda) is recommended
- 模型訓練過程建議使用 tmux 執行，避免 TWCC 連線中斷 / Run training inside tmux to avoid interruption caused by TWCC disconnections
