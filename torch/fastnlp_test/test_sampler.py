"""测试数据集采样模式"""
import torch
import numpy as np


if __name__ == "__main__":
    # RandomSampler
    data_set = list(range(10))
    print(data_set)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    np.random.seed(2020)
    sampler_test = list(np.random.permutation(len(data_set)))
    print(sampler_test)  # [2, 4, 9, 1, 5, 7, 6, 3, 8, 0]
    data_set = torch.tensor(data_set)
    print(data_set)
    # inps = torch.arange(10 * 5, dtype=torch.float32).view(10, 5)
    # tgts = torch.arange(10 * 5, dtype=torch.float32).view(10, 5)
    dataset = torch.utils.data.TensorDataset(data_set, data_set)
    print(type(dataset))
    sampler = torch.utils.data.RandomSampler(dataset)
    dataiter = torch.utils.data.DataLoader(dataset=dataset, batch_size=3, sampler=sampler, drop_last=False)
    print(len(dataiter))
    for data in dataiter:
        print(data)
    """
    [tensor([5, 3, 2]), tensor([5, 3, 2])]
    [tensor([0, 8, 7]), tensor([0, 8, 7])]
    [tensor([4, 1, 9]), tensor([4, 1, 9])]
    [tensor([6]), tensor([6])]
    """
