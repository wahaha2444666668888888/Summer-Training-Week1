# 🧠 Summer Training Week 1 — MNIST MLP 實作與開發工具實戰

## 🎯 課程目標

本週目標為完成一個手寫數字辨識模型（使用 MNIST 或 FashionMNIST 資料集），並實作機器學習專案常見工具的整合與實作流程：

- 熟悉 TWCC 環境建置與 GPU 使用
- 使用 GitHub 進行開發協作與版本控制
- 使用 tmux 管理訓練任務不中斷
- 使用 `nvidia-smi` 監控 GPU 使用狀況
- 使用 Weights & Biases（wandb）進行訓練記錄與可視化

---

## 🧪 作業內容

請完成一個使用 PyTorch 架設的簡單 MLP 模型，訓練資料集為 `FashionMNIST`（如有問題可改為 `MNIST`）。

實作功能需包含：

- 基本資料讀取與前處理
- 模型架構建立（可自訂層數）
- 訓練與計算 loss / accuracy
- 使用 wandb.log 記錄實驗結果
- 模型儲存為 `model.pt`

可參考範例程式：`train_mnist.py`  
或學生模板：`template/train_template.py`

---

## 🧰 工具要求

| 工具        | 使用說明                                                                 |
|-------------|--------------------------------------------------------------------------|
| TWCC        | 建立 GPU 計算環境並執行訓練任務                                           |
| tmux        | 使用 `tmux new -s <name>` 開啟 session，訓練不中斷                         |
| nvidia-smi  | 監控 GPU 使用情況，請附上執行時截圖或 log                                |
| wandb       | 使用 `wandb.log()` 上傳 loss / acc，登入後可產生線上儀表板               |
| GitHub      | 使用 branch → commit → PR → review → merge 的開發流程提交作業             |

---

## 👨‍💻 GitHub 作業繳交方式

### 🪜 操作流程（Clone → Branch → Commit → PR）

```bash
git clone https://github.com/ccuvislab/Summer-Training-Week1.git
cd Summer-Training-Week1
git checkout -b student_你的名字/week1

# 在 student_name/ 中實作你的程式
git add student_name/
git commit -m "完成 Week1 MLP 訓練"
git push origin student_name/week1
