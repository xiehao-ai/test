# import torch

# x = torch.randint(1, 10, (2, 2, 3))
# x = x.view(2, -1)
# print(x)
# print(x.size())
# x1 = torch.argmax(x, 1)
# x1 = x1.view(-1, 1)
# print(x1)
# x2 = x1.repeat(1, 10).view(-1, 1)
# print(x2)
# print(x2.size())


# how to use torch.gather
# x = torch.arange(24).reshape(4, 6).float()
# print(x)
# indices = torch.tensor([1, 4, 2, 3]).unsqueeze(-1)
# indices = torch.tensor([[1, 2, 2, 3, 1, 0]])
# print(indices)
# t = torch.gather(x, 1, indices)
# print(t)
# print(t.squeeze(1))
# print(t.t())
# print(t.t().shape)

# print(torch.max(x, 1))
# print(torch.argmax(x, 1))

# print(21 % 8, 21 // 8)
# xx = torch.randn_like(x).fill_(0.2)
# xx += x
# print(xx)
# print(xx.dtype, xx.device)
# xx /= 1.0*256/32
# # xx //= 5
# print(xx)
# print(torch.mean(xx, 0))

num = 2.3214
print(f'num is {num:.2f}')

from multiprocessing import cpu_count

print("CPU的核数为：{}".format(cpu_count()))





