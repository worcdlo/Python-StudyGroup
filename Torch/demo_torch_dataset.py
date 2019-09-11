import torch
import torch.utils.data as Data

torch.manual_seed(1)    # 打亂數據的的隨機種子

BATCH_SIZE = 8      # 每個批次的數據個數

x = torch.linspace(1, 10, 10)       # x data (torch tensor)
y = torch.linspace(21, 30, 10)       # y data (torch tensor)

# 將資料轉換成 torch 能吃的 Dataset
torch_dataset = Data.TensorDataset(x, y)

# 把 dataset 放入 DataLoader
loader = Data.DataLoader(
    dataset=torch_dataset,      # torch TensorDataset format
    batch_size=BATCH_SIZE,      # mini batch size
    shuffle=True                # 是否打亂數據，可以減少訓練時overfitting產生，也能根據loss觀察是否存在overfitting
)

# 訓練數據3次
for epoch in range(3):
    for step, (batch_x, batch_y) in enumerate(loader):  # 每一步loader都會釋放一小批數據來學習
        print("Epoch: {epoch} | Step: {step} | batch x: {x} | batch y: {y}".format(
                epoch=epoch,
                step=step,
                x=batch_x.numpy(),
                y=batch_y.numpy()
            )
        )

"""Result
每一梯次都隨機挑出 BATCH_SIZE 筆數據為一組訓練
該梯的最一輪不足額的部分可能只有少數幾筆

shuffle除了打亂數據減少訓練時的overfitting外
由於每一梯次的訓練數據都不同
因此若在某個梯次產生over fitting
則在接下來的梯次中
可能會發現loss急速上升

Epoch: 0 | Step: 0 | batch x: [ 9.  7.  2. 10.  8.  4.  6.  1.] | batch y: [29. 27. 22. 30. 28. 24. 26. 21.]
Epoch: 0 | Step: 1 | batch x: [5. 3.] | batch y: [25. 23.]
Epoch: 1 | Step: 0 | batch x: [10.  2.  9.  5.  6.  4.  8.  7.] | batch y: [30. 22. 29. 25. 26. 24. 28. 27.]
Epoch: 1 | Step: 1 | batch x: [1. 3.] | batch y: [21. 23.]
Epoch: 2 | Step: 0 | batch x: [7. 2. 8. 9. 6. 5. 3. 1.] | batch y: [27. 22. 28. 29. 26. 25. 23. 21.]
Epoch: 2 | Step: 1 | batch x: [10.  4.] | batch y: [30. 24.]
"""
