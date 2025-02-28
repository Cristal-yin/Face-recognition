import torch
from torch.autograd import Variable

tensor = torch.FloatTensor([[1,2],[3,4]])
variable = Variable(tensor, requires_grad = True)


t_out = torch.mean(tensor*tensor)
v_out = torch.mean(variable * variable)
print(t_out)
print(v_out)

#  Tensor不可以反向传播   varible可以反向传播
v_out.backward()
print(variable.grad)