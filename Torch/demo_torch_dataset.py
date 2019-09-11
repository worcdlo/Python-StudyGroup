import torch
import torch.utils.data as Data

# 打亂數據的的隨機種子
torch.manual_seed(1)

# 每個批次的數據個數
BATCH_SIZE = 8

# 打亂數據的的隨機種子
torch.manual_seed(1)

# 每個批次的數據個數
BATCH_SIZE = 8

# generate x, y in type: torch.tensor
x = torch.linspace(1, 10, 10)
y = torch.linspace(21, 30, 10)

# 將資料轉換成 torch 能吃的 Dataset
torch_dataset = Data.TensorDataset(x, y)

# 把 dataset 放入 DataLoader
loader = Data.DataLoader(
    dataset=torch_dataset,       # torch TensorDataset format
    batch_size=BATCH_SIZE,       # mini batch size
    shuffle=True,                # 是否打亂數據
    #num_workers=2,              # Multithread讀取数据，不知道為何總是失敗
)

# 訓練數據3輪
for epoch in range(3):
    # 每一輪的每一步loader都會釋放一小批數據來學習
    for step, (batch_x, batch_y) in enumerate(loader):
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

Epoch: 0 | Step: 0 | batch x: [ 5.  7. 10.  3.  4.  2.  1.  8.] | batch y: [25. 27. 30. 23. 24. 22. 21. 28.]
Epoch: 0 | Step: 1 | batch x: [9. 6.] | batch y: [29. 26.]
Epoch: 1 | Step: 0 | batch x: [ 4.  6.  7. 10.  8.  5.  3.  2.] | batch y: [24. 26. 27. 30. 28. 25. 23. 22.]
Epoch: 1 | Step: 1 | batch x: [1. 9.] | batch y: [21. 29.]
Epoch: 2 | Step: 0 | batch x: [ 4.  2.  5.  6. 10.  3.  9.  1.] | batch y: [24. 22. 25. 26. 30. 23. 29. 21.]
Epoch: 2 | Step: 1 | batch x: [8. 7.] | batch y: [28. 27.]
"""
