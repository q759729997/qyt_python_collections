# torch常规操作

## tensor常用

- tensor重要参数

~~~
requires_grad=True  # 自动微分，默认为false
dim, 在指定维度dim上进行操作，例如，tensor的shape为[2, 3]，max求值时，dim表示该维度会消失：
torch.max(torch.Tensor([[1, 4, 0], [2, 3, 0]]), dim=0)[0] # 返回 tensor([2., 4., 0.])，变为一行
torch.max(torch.Tensor([[1, 4, 0], [2, 3, 0]]), dim=1)[0] # 返回 tensor([4., 3.])，变为一列
~~~

- tensor属性

~~~
# 返回的torch.Size其实就是一个tuple, 支持所有tuple的操作
torch.Tensor(3, 4, 5).size()  # tensor的大小，返回：torch.Size([3, 4, 5])
torch.Tensor(3, 4, 5).shape  # tensor的大小，返回：torch.Size([3, 4, 5])
torch.LongTensor([1, 2, 3]).dtype  # tensor的数据类型，返回：torch.int64
torch.tensor([[2]]).device  # tensor所在设备，返回cpu或cuda
~~~

- tensor创建

~~~
Tensor(*sizes)  # 基础构造
eye(*sizes)，如torch.eye(2, 2)  # 对角线为1，其他为0，返回：tensor([[1., 0.],[0., 1.]])
arange(s,e,step)，如torch.arange(0, 10, 2)  # 从s到e，步长为step，返回：tensor([0, 2, 4, 6, 8])
linspace(s,e,steps)，如torch.linspace(0, 10, 2)  # 从s到e，均匀切分成steps份，返回：tensor([ 0., 10.])
normal(mean,std)/uniform(from,to)  # 正态分布/均匀分布
randperm(m)，如torch.randperm(10)  # 随机排列，返回：tensor([8, 3, 4, 6, 5, 9, 1, 0, 2, 7])
~~~

- tensor获取内容数据

~~~
torch.tensor([[2]]).item()  # 包含一个标量数值的tensor，获取内容，返回：2
.data 仍保留，但建议使用 .detach(), 区别在于 .data 返回和 x 的相同数据 tensor, 但不会加入到x的计算历史里，且require s_grad = False, 这样有些时候是不安全的, 因为 x.data 不能被 autograd 追踪求微分 。 
.detach() 返回相同数据的 tensor ,且 requires_grad=False ,但能通过 in-place 操作报告给 autograd 在进行反向传播的时候
~~~

- 加法

~~~
x + y
torch.add(x, y)  # 还可以指定输出 torch.add(x, y, out=result)
y.add_(x)  # inplace版本都有后缀_, 例如x.copy_(y), x.t_()
~~~

- tensor操作

~~~
# 返回输入张量中所有元素的最大值
torch.max(torch.Tensor([[1, 2], [3, 4]]), dim=1)  # 返回：torch.return_types.max(values=tensor([2., 4.]), indices=tensor([1, 1]))
~~~